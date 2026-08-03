<#
.SYNOPSIS
  Optimiza imágenes (PNG/JPG/JPEG/WebP) para la web usando ffmpeg.

.DESCRIPTION
  Convierte cada imagen a WebP (por defecto) o AVIF, redimensionándola si
  supera un ancho máximo. NUNCA modifica los archivos originales: todo se
  escribe en una carpeta de salida independiente, preservando la estructura
  de subcarpetas. Es seguro por diseño: si algo falla, los originales
  permanecen intactos.

.PARAMETER Source
  Carpeta con las imágenes de entrada. Obligatorio.

.PARAMETER Out
  Carpeta de salida (se crea si no existe). Por defecto: .\optimized junto a Source.

.PARAMETER MaxWidth
  Ancho máximo en píxeles (se reduce si la imagen excede; se respeta la
  proporción). Por defecto: 1600 (bueno para web).

.PARAMETER Quality
  Calidad de compresión (1-100, más alto = mejor calidad/más peso).
  Por defecto: 82.

.PARAMETER Format
  Formato de salida: "webp" (recomendado) o "avif".

.PARAMETER FfmpegPath
  Ruta al ejecutable ffmpeg si no está en el PATH.

.EXAMPLE
  .\optimize-images.ps1 -Source "D:\fotos" -Out "D:\fotos-web"
  Convierte todas las imágenes de D:\fotos a WebP (max 1600px, calidad 82)
  en D:\fotos-web sin tocar los originales.

.EXAMPLE
  .\optimize-images.ps1 -Source ".\public\assets\images" -MaxWidth 1200 -Quality 80 -Format avif
#>
param(
  [Parameter(Mandatory = $true)][string]$Source,
  [string]$Out,
  [int]$MaxWidth = 1600,
  [ValidateRange(1, 100)][int]$Quality = 82,
  [ValidateSet("webp", "avif")][string]$Format = "webp",
  [string]$FfmpegPath = "ffmpeg"
)

$ErrorActionPreference = "Stop"

if (-not (Test-Path -LiteralPath $Source)) {
  Write-Error "La carpeta de origen no existe: $Source"
  exit 1
}
if (-not $Out) { $Out = Join-Path $Source "optimized" }

# Verifica que ffmpeg exista
$ffmpegOk = $true
try { & $FfmpegPath -version 2>&1 | Out-Null } catch { $ffmpegOk = $false }
if (-not $ffmpegOk) {
  Write-Error "No se encontró ffmpeg. Instálalo (winget install ffmpeg) o usa -FfmpegPath."
  exit 1
}

New-Item -ItemType Directory -Force -Path $Out | Out-Null

$sourceRoot = (Resolve-Path $Source).Path
$outRoot = (Resolve-Path $Out).Path

$extensions = @(".png", ".jpg", ".jpeg", ".webp")
$files = Get-ChildItem -LiteralPath $Source -Recurse -File | Where-Object {
  $extensions -contains $_.Extension.ToLowerInvariant() -and
  $_.FullName.StartsWith($outRoot, [System.StringComparison]::OrdinalIgnoreCase) -eq $false
}

if ($files.Count -eq 0) {
  Write-Host "No se encontraron imágenes en $Source"
  exit 0
}

$totalBefore = 0
$totalAfter = 0
$converted = 0
$failed = @()

Write-Host "Optimizando $($files.Count) imágenes -> $Format (max ${MaxWidth}px, calidad $Quality)"
Write-Host "Originales intactos (no se modifica $Source)"

foreach ($file in $files) {
  $rel = $file.FullName.Substring((Resolve-Path $Source).Path.Length).TrimStart("\", "/")
  $outDir = Split-Path (Join-Path $Out $rel) -Parent
  New-Item -ItemType Directory -Force -Path $outDir | Out-Null

  $baseName = [System.IO.Path]::GetFileNameWithoutExtension($file.Name)
  $outFile = Join-Path $outDir "$baseName.$Format"

  # vf scale: reduce a MaxWidth conservando la proporción, sin ampliar imágenes pequeñas
  $filter = "scale='min($MaxWidth,iw)':-2"
  if ($Format -eq "webp") {
    $codecArgs = @("-c:v", "libwebp", "-quality", "$Quality", "-preset", "picture")
  } else {
    $codecArgs = @("-c:v", "libaom-av1", "-crf", "$(31 - [int]($Quality / 6.5))", "-b:v", "0")
  }

  $args = @("-y", "-i", $file.FullName, "-vf", $filter, "-loglevel", "error") + $codecArgs + @($outFile)
  & $FfmpegPath $args 2>$null
  if ($LASTEXITCODE -ne 0 -or -not (Test-Path -LiteralPath $outFile)) {
    $failed += $file.FullName
    Write-Host "  [FALLO] $rel"
    continue
  }

  $before = $file.Length
  $after = (Get-Item -LiteralPath $outFile).Length
  $totalBefore += $before
  $totalAfter += $after
  $converted++
  $savedPct = if ($before -gt 0) { [math]::Round((1 - $after / $before) * 100, 1) } else { 0 }
  $argsFmt = @($savedPct, $rel, [math]::Round($before / 1KB, 0), [math]::Round($after / 1KB, 0))
  Write-Host ("  [OK {0,5:0.0}% ] {1}  {2:N0} KB -> {3:N0} KB" -f $argsFmt)
}

Write-Host ""
Write-Host "Resumen: $converted convertidas, $($failed.Count) fallidas"
if ($totalBefore -gt 0) {
  $saved = $totalBefore - $totalAfter
  $savedPct = [math]::Round($saved / $totalBefore * 100, 1)
  Write-Host ("Tamaño: {0:N2} MB -> {1:N2} MB  (ahorraste {2:N2} MB, {3}%)" -f ($totalBefore / 1MB), ($totalAfter / 1MB), ($saved / 1MB), $savedPct)
}
Write-Host "Salida: $Out"

if ($failed.Count -gt 0) {
  Write-Host ""
  Write-Warning "$($failed.Count) imágenes no se pudieron convertir (se omitieron sin tocar):"
  $failed | ForEach-Object { Write-Host "  - $_" }
}
