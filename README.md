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

Add an open-by-default, collapsible box with a quote block. The bold label at the start sets the box title: use `Takeaway.` / `要点。` for the default title, or `Box: Your Title.` / `盒子：你的标题。` for any custom title. The box body may span multiple paragraphs and can contain `tabular` tables, `\includegraphics` images, and math:

```tex
\begin{quote}
\textbf{Box: Evidence Table.} First paragraph.

\begin{tabular}{ll}
Method & Score \\
K-Flow & 12.3 \\
\end{tabular}

Closing paragraph with \(x^2\) math.
\end{quote}
```

Embed a short video clip (mp4) with the custom `videoclip` environment; the first argument is the site-relative source path, the second a plain-text caption (may be empty):

```tex
\begin{videoclip}{assets/videos/demo.mp4}{A short demo clip.}
\end{videoclip}
```

Animated GIFs need no special syntax — `\includegraphics{assets/images/foo.gif}` renders as a normal image on the web.

Caveat for `make posts-pdf`: XeLaTeX cannot embed GIF or mp4 files, and does not know the `videoclip` environment. Posts that use them should be excluded from `--pdf` runs, or given PDF-safe fallbacks.

Every post page automatically gets a floating table of contents built from its `\section`/`\subsection` headings (visible on wide viewports only); no TeX markup is required.

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
