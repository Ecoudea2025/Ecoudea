<#
.SYNOPSIS
  Optimiza videos (MP4/WebM/MOV) para la web usando ffmpeg.
  Genera H.264 MP4 con -movflags +faststart (CRÍTICO para seeking en GitHub Pages)
  y, opcionalmente, WebM VP9. NUNCA toca los originales.

.DESCRIPTION
  Para GitHub Pages: cada archivo no debe exceder ~100MB (límite por archivo).
  H.264 (crf 28) es el formato más compatible; WebM VP9 comprime mejor pero
  pesa más en CPU de codificación.

.PARAMETER Source
  Carpeta con los videos de entrada. Obligatorio.

.PARAMETER Out
  Carpeta de salida (se crea si no existe). Por defecto: .\optimized junto a Source.

.PARAMETER Crf
  Calidad H.264 (18=alta, 28=buena web, 32=baja). Por defecto: 28.

.PARAMETER MaxWidth
  Ancho máximo en píxeles (respeta proporción). Por defecto: 1280.

.PARAMETER Webm
  Switch: también genera versión .webm (VP9) junto al .mp4.

.EXAMPLE
  .\optimize-videos.ps1 -Source "D:\videos-curso" -Out "D:\videos-web"
  Genera MP4 H.264 (crf 28, max 1280px, faststart) en D:\videos-web.
#>
param(
  [Parameter(Mandatory = $true)][string]$Source,
  [string]$Out,
  [ValidateRange(0, 51)][int]$Crf = 28,
  [int]$MaxWidth = 1280,
  [switch]$Webm
)

$ErrorActionPreference = "Stop"

if (-not (Test-Path -LiteralPath $Source)) {
  Write-Error "La carpeta de origen no existe: $Source"
  exit 1
}
if (-not $Out) { $Out = Join-Path $Source "optimized" }

$ffmpegOk = $true
try { & ffmpeg -version 2>&1 | Out-Null } catch { $ffmpegOk = $false }
if (-not $ffmpegOk) {
  Write-Error "No se encontró ffmpeg. Instálalo (winget install ffmpeg)."
  exit 1
}

New-Item -ItemType Directory -Force -Path $Out | Out-Null
$sourceRoot = (Resolve-Path $Source).Path
$outRoot = (Resolve-Path $Out).Path

$extensions = @(".mp4", ".webm", ".mov", ".mkv")
$files = Get-ChildItem -LiteralPath $Source -Recurse -File | Where-Object {
  $extensions -contains $_.Extension.ToLowerInvariant() -and
  $_.FullName.StartsWith($outRoot, [System.StringComparison]::OrdinalIgnoreCase) -eq $false
}

if ($files.Count -eq 0) {
  Write-Host "No se encontraron videos en $Source"
  exit 0
}

$totalBefore = 0
$totalAfter = 0
$converted = 0
$failed = @()
$filter = "scale='min($MaxWidth,iw)':-2"

Write-Host "Optimizando $($files.Count) videos -> H.264 MP4 (crf $Crf, max ${MaxWidth}px)$(if ($Webm) { ' + WebM VP9' })"

foreach ($file in $files) {
  $rel = $file.FullName.Substring($sourceRoot.Length).TrimStart("\", "/")
  $outDir = Split-Path (Join-Path $Out $rel) -Parent
  New-Item -ItemType Directory -Force -Path $outDir | Out-Null

  $baseName = [System.IO.Path]::GetFileNameWithoutExtension($file.Name)

  # 1) MP4 H.264 + faststart (seeking en streaming HTTP)
  $mp4 = Join-Path $outDir "$baseName.mp4"
  $args1 = @("-y", "-i", $file.FullName, "-vf", $filter, "-c:v", "libx264", "-preset", "medium", "-crf", "$Crf", "-movflags", "+faststart", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "128k", "-loglevel", "error", $mp4)
  & ffmpeg $args1 2>$null
  if ($LASTEXITCODE -ne 0 -or -not (Test-Path -LiteralPath $mp4)) {
    $failed += $file.FullName
    Write-Host "  [FALLO] $rel"
    continue
  }
  $converted++
  $afterMp4 = (Get-Item -LiteralPath $mp4).Length
  $totalAfter += $afterMp4
  $savedPct = if ($file.Length -gt 0) { [math]::Round((1 - $afterMp4 / $file.Length) * 100, 1) } else { 0 }
  Write-Host ("  [OK {0,5:0.0}% ] {1}  {2:N1} MB -> {3:N1} MB" -f @($savedPct, $rel, ($file.Length / 1MB), ($afterMp4 / 1MB)))
  $totalBefore += $file.Length

  # 2) WebM VP9 opcional
  if ($Webm) {
    $webm = Join-Path $outDir "$baseName.webm"
    $args2 = @("-y", "-i", $file.FullName, "-vf", $filter, "-c:v", "libvpx-vp9", "-crf", "32", "-b:v", "0", "-c:a", "libopus", "-loglevel", "error", $webm)
    & ffmpeg $args2 2>$null
    if ($LASTEXITCODE -eq 0 -and (Test-Path -LiteralPath $webm)) {
      Write-Host "  [WEBM] $rel -> $([math]::Round((Get-Item $webm).Length / 1MB, 1)) MB"
    } else {
      Write-Host "  [WEBM FALLO] $rel (se omite, MP4 listo)"
    }
  }
}

Write-Host ""
Write-Host "Resumen: $converted convertidos, $($failed.Count) fallidos"
if ($totalBefore -gt 0) {
  $saved = $totalBefore - $totalAfter
  $savedPct = [math]::Round($saved / $totalBefore * 100, 1)
  Write-Host ("Tamaño: {0:N1} MB -> {1:N1} MB  (ahorraste {2:N1} MB, {3}%)" -f @(($totalBefore / 1MB), ($totalAfter / 1MB), ($saved / 1MB), $savedPct))
}
Write-Host "Salida: $Out"
Write-Host "RECUERDA: en GitHub Pages cada archivo debe ser < 100MB."

if ($failed.Count -gt 0) {
  Write-Host ""
  Write-Warning "$($failed.Count) videos no se pudieron convertir (sin tocar):"
  $failed | ForEach-Object { Write-Host "  - $_" }
}
