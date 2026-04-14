MAIN = main.tex

.PHONY: pdf clean

pdf:
	latexmk -lualatex -interaction=nonstopmode -file-line-error -outdir=build $(MAIN)

clean:
	latexmk -C -outdir=build $(MAIN)
	rm -rf build
