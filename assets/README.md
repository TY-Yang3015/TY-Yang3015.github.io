# Assets

Source assets are grouped by responsibility:

- `css/foundation/`: theme tokens, reset, typography, and global behavior.
- `css/layout/`: site shell, header, footer, and shared section geometry.
- `css/components/`: reusable controls, polygon panels, cards, filters, and disclosures.
- `css/pages/`: page-level composition only.
- `css/style.scss`: ordered Sass manifest.
- `js/theme.js`: persistent day/night mode controller.
- `js/collection-filter.js`: shared filtering for blog and publication archives.
- `js/external-links.js`: ensures external web links and PDF documents open safely in a new tab.
- `documents/`: public profile documents such as the CV.
- `icons/`: favicons and source artwork.
- `images/`: blog and publication media.
- `papers/`: locally hosted papers and dissertations.

Keep content data in `_data/` and `_publications/`; reusable Liquid markup belongs in `_includes/components/`.
