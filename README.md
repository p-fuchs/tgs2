# pres2

Standalone LaTeX Beamer presentation scaffold for a talk on the paper
"Women's Connectivity in Extreme Networks."

## Build

Use either of these commands from `pres2/`:

```bash
make pdf
```

```bash
latexmk -lualatex -interaction=nonstopmode -file-line-error -outdir=build main.tex
```

## Structure

- `main.tex`: thin document entrypoint
- `config/`: packages, metadata, and reusable frame macros
- `theme/`: custom Beamer theme, palette, and font setup
- `sections/`: one file per presentation section
- `references/`: `biblatex` bibliography database
- `assets/`: figures and tables for the deck
- `materials/`: source paper and supporting reference documents

## Notes

- The deck targets `lualatex` + `biber`.
- The current files are a backbone only; section content is placeholder text.
- The original source paper is stored at `materials/womens-connectivity-extreme-networks.pdf`.
