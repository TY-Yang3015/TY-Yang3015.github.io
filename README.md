# Tianyue Yang — research portfolio

A Jekyll site for projects, publications, and TeX-authored research notes across AI, physics, and chemistry.

## Local preview

Install the Ruby dependencies once, then use the Make targets so TeX posts are regenerated before Jekyll starts:

```sh
bundle install
make serve
```

## Writing blog posts in TeX

TeX is the source of truth for every English and Chinese article.

- Article sources: `_tex/posts/*.tex`
- Shared BibTeX database: `_tex/references.bib`
- Post metadata and output paths: `_tex/posts.json`
- Generated Jekyll inputs: `_posts/*.html` and `_zh/*.html`

Use standard natbib citation commands in a source article:

```tex
As shown by \citet{jacot2018ntk}, ...
A related result follows \citep{du2025flow}.
```

Mark a key display equation with a unique `keyeq` label to render it as a static color callout:

```tex
\[
E = mc^2
\label{keyeq:mass-energy}
\]
```

Add an open-by-default, collapsible takeaway with a quote block. Use `Takeaway.` for English or `要点。` for Chinese:

```tex
\begin{quote}
\textbf{Takeaway.} The concise point readers should retain.
\end{quote}
```

Then run:

```sh
make posts        # TeX → cited HTML for Jekyll
make posts-check  # verify committed HTML matches the TeX sources
make posts-pdf    # also compile PDFs with XeLaTeX + BibTeX
make build        # regenerate posts and build the complete site
```

`make posts` requires Pandoc. PDF output additionally requires `latexmk`, XeLaTeX, and BibTeX. Generated PDFs are written to `_tex/build/pdf/`. Do not edit generated article HTML directly.

## Content architecture

- `index.md`, `about.md`, `projects.md`, `blog.md`, `pub.md`: page composition.
- `_tex/`: TeX articles, their manifest, and shared citations.
- `_publications/`: one publication record per Markdown file.
- `_data/projects.yml`: project records.
- `_includes/components/`: reusable Liquid cards and page headers.
- `_layouts/`: shared document and post shells.
- `scripts/build_tex_posts.py`: reproducible TeX-to-HTML/PDF compiler.

## Frontend architecture

Sass is layered in dependency order:

1. `assets/css/foundation/` — day/night tokens and global defaults.
2. `assets/css/layout/` — site shell and structural layouts.
3. `assets/css/components/` — reusable UI and content components.
4. `assets/css/pages/` — page-specific composition.

`assets/js/theme.js` controls persistent color mode. `assets/js/collection-filter.js` powers both archive filters. `assets/js/external-links.js` safely opens external web links and PDF documents in a new tab.

## Notes

- Do not edit `_site/`; Jekyll generates it.
- Add design values to the token layer instead of hard-coding page colors.
- Keep reusable markup in `_includes/components/`.
- Keep public assets organized according to `assets/README.md`.
