# ─────────────────────────────────────────────────────────────
# Script: knit-to-astro.R
# Uso:   source("scripts/knit-to-astro.R")
#
# Este script toma un archivo .Rmd y lo renderiza a .md
# en la carpeta correcta de src/content/classes/ para que
# Astro lo use automáticamente.
# ─────────────────────────────────────────────────────────────

library(rmarkdown)

# ── Configuración ───────────────────────────────────────────
# Cambia esto por el curso correspondiente:
COURSE_SLUG <- "estadistica-i"

# El archivo .Rmd a renderizar (puedes pasarlo como argumento)
RMD_FILE <- commandArgs(trailingOnly = TRUE)
if (length(RMD_FILE) == 0) {
  stop("Uso: Rscript scripts/knit-to-astro.R nombre-del-archivo.Rmd")
}

# ── Renderizar ──────────────────────────────────────────────
output_dir <- file.path("src", "content", "classes")

rmarkdown::render(
  input = RMD_FILE,
  output_dir = output_dir,
  output_format = "md_document",
  encoding = "UTF-8"
)

cat(sprintf("✅ Renderizado completado: %s → %s/\n", RMD_FILE, output_dir))
cat("📝 Recuerda verificar el frontmatter y ajustar 'course:', 'order:', 'classType:'\n")
