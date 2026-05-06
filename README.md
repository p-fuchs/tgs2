# pres3

Standalone LaTeX Beamer presentation for the survey paper
"A Survey of Adversarial Learning on Graphs."

## Build

From `pres3/`:

```bash
make pdf
```

or:

```bash
latexmk -lualatex -interaction=nonstopmode -file-line-error -outdir=build main.tex
```

## Structure

- `main.tex`: thin document entrypoint
- `config/`: packages, metadata, and reusable macros
- `theme/`: custom Beamer theme, palette, and font setup
- `sections/`: slide content
- `assets/`: paper source files and visual references
