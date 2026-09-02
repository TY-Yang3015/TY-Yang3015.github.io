#!/usr/bin/env python3
"""Compile LaTeX article sources into Jekyll HTML posts and optional PDFs."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "_tex" / "posts.json"
BIBLIOGRAPHY = ROOT / "_tex" / "references.bib"
LINK_FILTER = ROOT / "scripts" / "pandoc_external_links.lua"
PDF_ROOT = ROOT / "_tex" / "build" / "pdf"
TEX_BUILD_ROOT = ROOT / ".tex-build"


def run(command: list[str], *, cwd: Path = ROOT) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, cwd=cwd, check=True, text=True, capture_output=True)


def yaml_value(value: Any) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    return json.dumps(value, ensure_ascii=False)


def front_matter(metadata: dict[str, Any], source: Path) -> str:
    lines = ["---"]
    for key, value in metadata.items():
        lines.append(f"{key}: {yaml_value(value)}")
    lines.extend((f'generated_from: "{source.as_posix()}"', "---", ""))
    return "\n".join(lines)


def render_html(entry: dict[str, Any]) -> str:
    source = ROOT / entry["source"]
    command = [
        "pandoc",
        str(source),
        "--from=latex",
        "--to=html5",
        "--wrap=none",
        "--mathjax",
        "--citeproc",
        "--metadata=link-citations:true",
        f"--bibliography={BIBLIOGRAPHY}",
        f"--lua-filter={LINK_FILTER}",
        "--shift-heading-level-by=1",
        f"--metadata=lang:{entry['language']}",
        f"--metadata=reference-section-title:{entry.get('reference_title', 'References')}",
    ]
    body = run(command).stdout
    body = body.replace('src="assets/', 'src="/assets/')
    body = body.replace('<h1 class="unnumbered" id="bibliography">', '<h2 class="unnumbered" id="bibliography">')
    body = body.replace('</h1>\n<div id="refs"', '</h2>\n<div id="refs"')

    def mark_key_equation(match: re.Match[str]) -> str:
        equation = match.group(1) + match.group(3)
        key = match.group(2)
        return f'<div class="equation-emphasis" id="equation-{key}">\n<span class="math display">{equation}</span>\n</div>'

    body = re.sub(
        r'<p><span class="math display">([^<]*?)\\label\{keyeq:([A-Za-z0-9_-]+)\}([^<]*?)</span></p>',
        mark_key_equation,
        body,
        flags=re.DOTALL,
    )

    takeaway_titles = {"Takeaway.": "Takeaway", "要点。": "要点"}

    def make_takeaway(match: re.Match[str]) -> str:
        title = takeaway_titles[match.group(1)]
        content = match.group(2)
        return (
            '<details class="takeaway-box" open>\n'
            f'<summary><span>{title}</span><span class="takeaway-toggle" aria-hidden="true"></span></summary>\n'
            f'<div class="takeaway-content"><p>{content}</p></div>\n'
            '</details>'
        )

    body = re.sub(
        r'<blockquote>\s*<p><strong>(Takeaway\.|要点。)</strong>\s*(.*?)</p>\s*</blockquote>',
        make_takeaway,
        body,
        flags=re.DOTALL,
    )

    def mark_image_pair(match: re.Match[str]) -> str:
        figure = match.group(0)
        if figure.count("<img ") > 1:
            return figure.replace("<figure>", '<figure class="image-pair">', 1)
        return figure

    body = re.sub(r"<figure>.*?</figure>", mark_image_pair, body, flags=re.DOTALL)
    notice = f"<!-- Generated from {entry['source']}; edit the TeX source, not this file. -->\n"
    return front_matter(entry["front_matter"], Path(entry["source"])) + notice + body


def write_or_check(entry: dict[str, Any], rendered: str, check: bool) -> bool:
    output = ROOT / entry["output"]
    if check:
        current = output.read_text(encoding="utf-8") if output.exists() else ""
        if current != rendered:
            print(f"out of date: {output.relative_to(ROOT)}", file=sys.stderr)
            return False
        return True
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(rendered, encoding="utf-8")
    print(f"generated {output.relative_to(ROOT)}")
    return True


def tex_escape(text: str) -> str:
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
    }
    return "".join(replacements.get(char, char) for char in text)


def compile_pdf(entry: dict[str, Any]) -> None:
    if not shutil.which("latexmk") or not shutil.which("xelatex"):
        raise RuntimeError("PDF compilation requires latexmk and XeLaTeX")

    build_dir = TEX_BUILD_ROOT / entry["id"]
    build_dir.mkdir(parents=True, exist_ok=True)
    source_from_build = Path("../..") / entry["source"]
    bibliography_from_build = Path("../..") / BIBLIOGRAPHY.relative_to(ROOT).with_suffix("")
    title = tex_escape(entry["front_matter"]["title"])
    language = entry["language"]
    document_class = "ctexart" if language.startswith("zh") else "article"
    date = tex_escape(entry["front_matter"].get("date", ""))
    if not date:
        date = ""

    wrapper = rf"""\documentclass[11pt]{{{document_class}}}
\usepackage[margin=1in]{{geometry}}
\usepackage{{amsmath,amssymb,mathtools,bm,graphicx}}
\usepackage[round,authoryear]{{natbib}}
\usepackage[hidelinks]{{hyperref}}
\graphicspath{{{{../../}}}}
\title{{{title}}}
\author{{Tianyue Yang}}
\date{{{date}}}
\begin{{document}}
\maketitle
\input{{{source_from_build.as_posix()}}}
\bibliographystyle{{plainnat}}
\bibliography{{{bibliography_from_build.as_posix()}}}
\end{{document}}
"""
    (build_dir / "main.tex").write_text(wrapper, encoding="utf-8")
    result = run(
        ["latexmk", "-xelatex", "-bibtex", "-interaction=nonstopmode", "-halt-on-error", "main.tex"],
        cwd=build_dir,
    )
    PDF_ROOT.mkdir(parents=True, exist_ok=True)
    destination = PDF_ROOT / f"{entry['id']}.pdf"
    shutil.copy2(build_dir / "main.pdf", destination)
    print(f"compiled {destination.relative_to(ROOT)}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if generated posts differ from their TeX sources")
    parser.add_argument("--pdf", action="store_true", help="also compile PDF copies with XeLaTeX and BibTeX")
    args = parser.parse_args()

    if not shutil.which("pandoc"):
        parser.error("pandoc is required")

    entries = json.loads(MANIFEST.read_text(encoding="utf-8"))
    ok = True
    for entry in entries:
        rendered = render_html(entry)
        ok = write_or_check(entry, rendered, args.check) and ok
        if args.pdf and not args.check:
            compile_pdf(entry)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
