#!/usr/bin/env python3
"""Serve the generated study guides from this repository."""

from __future__ import annotations

import argparse
import html
import io
import mimetypes
import posixpath
import re
import sys
import urllib.parse
from dataclasses import dataclass
from http import HTTPStatus
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Iterable, List, Optional, Sequence, Tuple


ROOT = Path(__file__).resolve().parent
TITLE_RE = re.compile(r"<title>\s*(.*?)\s*</title>", re.IGNORECASE | re.DOTALL)
DATE_RE = re.compile(r"(\d{4}-\d{2}-\d{2})")


@dataclass(frozen=True)
class GuideCollection:
    name: str
    current_path: str
    archive_dir: Optional[str] = None
    archive_prefix: Optional[str] = None
    aliases: Tuple[str, ...] = ()


COLLECTIONS: Tuple[GuideCollection, ...] = (
    GuideCollection("LeetCode Study Guide", "guide.html", "guides", "guide", ("guide", "leetcode")),
    GuideCollection("Python Guide", "python-guide.html", "python-guides", "python-guide", ("python",)),
    GuideCollection(
        "JavaScript Guide",
        "javascript-guide.html",
        "javascript-guides",
        "javascript-guide",
        ("javascript", "js"),
    ),
    GuideCollection(
        "TypeScript Guide",
        "typescript-guide.html",
        "typescript-guides",
        "typescript-guide",
        ("typescript", "ts"),
    ),
    GuideCollection("Go Guide", "golang-guide.html", "golang-guides", "golang-guide", ("golang", "go")),
    GuideCollection("Multi-Language Guide", "lang-guide.html", "lang-guides", "lang-guide", ("lang",)),
    GuideCollection("Performance Report", "report.html", "reports", "report", ("report", "reports")),
    GuideCollection("Cheatsheet", "cheatsheet.html", aliases=("cheatsheet",)),
)

TOP_LEVEL_FILES = {collection.current_path for collection in COLLECTIONS}
GUIDE_DIRS = {collection.archive_dir for collection in COLLECTIONS if collection.archive_dir}


def is_relative_to(path: Path, base: Path) -> bool:
    try:
        path.relative_to(base)
    except ValueError:
        return False
    return True


def read_title(path: Path) -> str:
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return path.name

    match = TITLE_RE.search(text)
    if not match:
        return path.name

    title = " ".join(match.group(1).split())
    return html.unescape(title)


def archive_files(collection: GuideCollection) -> List[Path]:
    if not collection.archive_dir:
        return []

    archive_dir = ROOT / collection.archive_dir
    if not archive_dir.is_dir():
        return []

    prefix = collection.archive_prefix or ""
    pattern = f"{prefix}-*.html" if prefix else "*.html"
    return sorted(archive_dir.glob(pattern), key=lambda path: path.name, reverse=True)


def relative_url(path: Path) -> str:
    rel = path.relative_to(ROOT).as_posix()
    return "/" + urllib.parse.quote(rel)


def file_date(path: Path) -> str:
    match = DATE_RE.search(path.name)
    return match.group(1) if match else ""


def route_aliases() -> dict:
    aliases = {}
    for collection in COLLECTIONS:
        target = "/" + collection.current_path
        for alias in collection.aliases:
            aliases["/" + alias] = target
            aliases["/latest/" + alias] = target
    aliases["/latest"] = "/guide.html"
    return aliases


ALIASES = route_aliases()


def split_url_path(url_path: str) -> List[str]:
    raw_parts = posixpath.normpath(urllib.parse.unquote(url_path)).split("/")
    return [part for part in raw_parts if part and part not in (".", "..")]


def quote_parts(parts: Iterable[str]) -> str:
    return "/" + "/".join(urllib.parse.quote(part) for part in parts)


def nested_guide_redirect(url_path: str) -> Optional[str]:
    parts = split_url_path(url_path)
    if len(parts) < 2 or parts[0] not in GUIDE_DIRS:
        return None

    if parts[1] in TOP_LEVEL_FILES or parts[1] in GUIDE_DIRS:
        return quote_parts(parts[1:])

    return None


def render_index() -> bytes:
    current_items = []
    for collection in COLLECTIONS:
        current = ROOT / collection.current_path
        if not current.is_file():
            continue

        title = read_title(current)
        archives = archive_files(collection)
        latest_archive = archives[0] if archives else None
        meta_parts = [html.escape(title)]
        if latest_archive:
            latest_label = html.escape(file_date(latest_archive) or latest_archive.name)
            meta_parts.append(f"latest archive: {latest_label}")

        current_items.append(
            f"""
            <li class="guide-row">
              <a class="guide-title" href="/{html.escape(collection.current_path)}">{html.escape(collection.name)}</a>
              <span class="guide-meta">{' | '.join(meta_parts)}</span>
            </li>
            """
        )

    archive_sections = []
    for collection in COLLECTIONS:
        archives = archive_files(collection)
        if not archives:
            continue

        links = []
        for archive in archives:
            label = file_date(archive) or archive.name
            title = read_title(archive)
            links.append(
                f"""
                <li>
                  <a href="{html.escape(relative_url(archive))}">{html.escape(label)}</a>
                  <span>{html.escape(title)}</span>
                </li>
                """
            )

        archive_sections.append(
            f"""
            <details class="archive" open>
              <summary>
                <span>{html.escape(collection.name)}</span>
                <span class="count">{len(archives)} files</span>
              </summary>
              <ul>{''.join(links)}</ul>
            </details>
            """
        )

    body = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Study Guides</title>
<style>
:root {{
  color-scheme: dark light;
  --bg: #0f1216;
  --panel: #171c22;
  --panel-2: #20262e;
  --text: #e7edf4;
  --muted: #9aa6b2;
  --border: #303944;
  --blue: #62a8ff;
  --green: #56d364;
  --gold: #d8a657;
}}
@media (prefers-color-scheme: light) {{
  :root {{
    --bg: #f7f8fa;
    --panel: #ffffff;
    --panel-2: #eef2f6;
    --text: #20252b;
    --muted: #65717d;
    --border: #d6dde5;
    --blue: #0969da;
    --green: #1a7f37;
    --gold: #9a6700;
  }}
}}
* {{ box-sizing: border-box; }}
body {{
  margin: 0;
  background: var(--bg);
  color: var(--text);
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
  line-height: 1.5;
}}
header, main {{ width: min(1120px, calc(100% - 32px)); margin: 0 auto; }}
header {{ padding: 32px 0 18px; border-bottom: 1px solid var(--border); }}
h1 {{ margin: 0 0 8px; font-size: 30px; letter-spacing: 0; }}
.subhead {{ color: var(--muted); margin: 0; }}
main {{ padding: 24px 0 48px; }}
h2 {{ margin: 0 0 12px; font-size: 18px; }}
.section {{ margin-bottom: 28px; }}
.guide-list, .archive ul {{ list-style: none; margin: 0; padding: 0; }}
.guide-row {{
  display: grid;
  grid-template-columns: minmax(190px, 260px) 1fr;
  gap: 16px;
  align-items: start;
  padding: 12px 0;
  border-bottom: 1px solid var(--border);
}}
.guide-title, .archive a {{ color: var(--blue); font-weight: 650; text-decoration: none; }}
.guide-title:hover, .archive a:hover {{ text-decoration: underline; }}
.guide-meta, .archive li span {{ color: var(--muted); font-size: 14px; }}
.archives {{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(310px, 1fr));
  gap: 14px;
}}
.archive {{
  background: var(--panel);
  border: 1px solid var(--border);
  border-radius: 8px;
  overflow: hidden;
}}
.archive summary {{
  cursor: pointer;
  display: flex;
  justify-content: space-between;
  gap: 16px;
  padding: 12px 14px;
  background: var(--panel-2);
  font-weight: 700;
}}
.count {{ color: var(--gold); font-size: 13px; white-space: nowrap; }}
.archive li {{
  display: grid;
  grid-template-columns: 96px 1fr;
  gap: 12px;
  padding: 9px 14px;
  border-top: 1px solid var(--border);
}}
.shortcuts {{
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
}}
.shortcut {{
  display: inline-flex;
  align-items: center;
  min-height: 32px;
  padding: 4px 10px;
  border: 1px solid var(--border);
  border-radius: 6px;
  color: var(--green);
  text-decoration: none;
  background: var(--panel);
  font-size: 14px;
  font-weight: 650;
}}
@media (max-width: 640px) {{
  .guide-row, .archive li {{ grid-template-columns: 1fr; gap: 4px; }}
  header {{ padding-top: 24px; }}
}}
</style>
</head>
<body>
<header>
  <h1>Study Guides</h1>
  <p class="subhead">Serving guide HTML from {html.escape(str(ROOT))}</p>
</header>
<main>
  <section class="section">
    <h2>Current</h2>
    <ul class="guide-list">{''.join(current_items)}</ul>
  </section>
  <section class="section">
    <h2>Shortcuts</h2>
    <div class="shortcuts">
      <a class="shortcut" href="/guide">LeetCode</a>
      <a class="shortcut" href="/python">Python</a>
      <a class="shortcut" href="/javascript">JavaScript</a>
      <a class="shortcut" href="/typescript">TypeScript</a>
      <a class="shortcut" href="/go">Go</a>
      <a class="shortcut" href="/lang">Multi-Language</a>
      <a class="shortcut" href="/report">Report</a>
      <a class="shortcut" href="/cheatsheet">Cheatsheet</a>
    </div>
  </section>
  <section class="section">
    <h2>Archives</h2>
    <div class="archives">{''.join(archive_sections)}</div>
  </section>
</main>
</body>
</html>
"""
    return body.encode("utf-8")


def render_directory_index(directory: Path) -> bytes:
    rel = directory.relative_to(ROOT)
    display = rel.as_posix() if rel.parts else "."
    rows = []

    if rel.parts:
        parent = "/" + urllib.parse.quote(rel.parent.as_posix()) if rel.parent.parts else "/"
        rows.append(f'<li><a href="{html.escape(parent)}">..</a><span>parent directory</span></li>')

    children = sorted(directory.iterdir(), key=lambda path: (not path.is_dir(), path.name.lower()))
    for child in children:
        if child.name.startswith("."):
            continue
        link = relative_url(child)
        label = child.name + ("/" if child.is_dir() else "")
        detail = "directory" if child.is_dir() else read_title(child) if child.suffix == ".html" else "file"
        rows.append(
            f'<li><a href="{html.escape(link)}">{html.escape(label)}</a><span>{html.escape(detail)}</span></li>'
        )

    body = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Index of {html.escape(display)}</title>
<style>
body {{ margin: 32px auto; max-width: 900px; padding: 0 16px; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; line-height: 1.5; }}
a {{ color: #0969da; font-weight: 650; text-decoration: none; }}
a:hover {{ text-decoration: underline; }}
ul {{ list-style: none; padding: 0; }}
li {{ display: grid; grid-template-columns: 260px 1fr; gap: 16px; padding: 8px 0; border-bottom: 1px solid #d0d7de; }}
span {{ color: #656d76; }}
@media (max-width: 640px) {{ li {{ grid-template-columns: 1fr; gap: 3px; }} }}
</style>
</head>
<body>
<h1>Index of {html.escape(display)}</h1>
<p><a href="/">Study Guides</a></p>
<ul>{''.join(rows)}</ul>
</body>
</html>
"""
    return body.encode("utf-8")


class GuideRequestHandler(SimpleHTTPRequestHandler):
    server_version = "GuideServer/1.0"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def do_GET(self) -> None:
        self.handle_request(send_body=True)

    def do_HEAD(self) -> None:
        self.handle_request(send_body=False)

    def handle_request(self, send_body: bool) -> None:
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path.rstrip("/") if parsed.path != "/" else "/"

        if path in ("/", "/index.html"):
            self.send_bytes(render_index(), "text/html; charset=utf-8", send_body)
            return

        if path == "/healthz":
            self.send_bytes(b"ok\n", "text/plain; charset=utf-8", send_body)
            return

        if path in ALIASES:
            self.send_response(HTTPStatus.FOUND)
            self.send_header("Location", ALIASES[path])
            self.end_headers()
            return

        redirect = nested_guide_redirect(parsed.path)
        if redirect:
            self.send_response(HTTPStatus.FOUND)
            self.send_header("Location", redirect)
            self.end_headers()
            return

        if not self.is_allowed_url_path(parsed.path):
            self.send_error(HTTPStatus.NOT_FOUND, "Guide file not found")
            return

        if send_body:
            super().do_GET()
        else:
            super().do_HEAD()

    def send_bytes(self, content: bytes, content_type: str, send_body: bool) -> None:
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        if send_body:
            self.wfile.write(content)

    def translate_path(self, path: str) -> str:
        parts = split_url_path(urllib.parse.urlparse(path).path)

        if not parts:
            return str(ROOT)

        return str(ROOT.joinpath(*parts))

    def is_allowed_url_path(self, url_path: str) -> bool:
        candidate = Path(self.translate_path(url_path)).resolve()
        if not is_relative_to(candidate, ROOT):
            return False

        try:
            rel = candidate.relative_to(ROOT)
        except ValueError:
            return False

        if not rel.parts:
            return True

        first = rel.parts[0]
        if len(rel.parts) == 1 and first in TOP_LEVEL_FILES:
            return True

        if first in GUIDE_DIRS:
            return True

        return False

    def list_directory(self, path: str):
        directory = Path(path).resolve()
        if not is_relative_to(directory, ROOT):
            self.send_error(HTTPStatus.NOT_FOUND, "Guide directory not found")
            return None

        content = render_directory_index(directory)
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        return io.BytesIO(content)


class GuideHTTPServer(ThreadingHTTPServer):
    allow_reuse_address = True


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Serve the generated guide HTML files.")
    parser.add_argument("--host", default="127.0.0.1", help="Host/interface to bind. Default: 127.0.0.1")
    parser.add_argument("--port", default=8000, type=int, help="Port to bind. Use 0 for an ephemeral port.")
    return parser.parse_args(argv)


def display_host(host: str) -> str:
    return "127.0.0.1" if host in ("", "0.0.0.0", "::") else host


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = parse_args(argv)
    mimetypes.add_type("text/html; charset=utf-8", ".html")

    try:
        server = GuideHTTPServer((args.host, args.port), GuideRequestHandler)
    except OSError as exc:
        print(f"Could not start guide server on {args.host}:{args.port}: {exc}", file=sys.stderr)
        return 1

    host, port = server.server_address[:2]
    print(f"Serving guides from {ROOT}")
    print(f"Open http://{display_host(str(host))}:{port}/")
    print("Press Ctrl-C to stop.")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping guide server.")
    finally:
        server.server_close()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
