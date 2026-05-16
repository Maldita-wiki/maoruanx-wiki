#!/usr/bin/env python3
"""Crawl guide.maoruanx.com — used by GitHub Actions CI"""

import os
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urlparse, unquote
from concurrent.futures import ThreadPoolExecutor, as_completed
from bs4 import BeautifulSoup

import requests


BASE = "https://guide.maoruanx.com"
OUT_DIR = Path("/home/runner/work/maoruanx-wiki/maoruanx-wiki/docs")
SITEMAP_URL = f"{BASE}/sitemap.xml"
MAX_WORKERS = 6
TIMEOUT = 15


def get_urls():
    resp = requests.get(SITEMAP_URL, timeout=30)
    root = ET.fromstring(resp.text)
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    return [u.find("sm:loc", ns).text for u in root.findall("sm:url", ns)]


DOC_PREFIXES = ("/game/", "/gta5/", "/rdr2/", "/misc/", "/home/", "/injecterror/")
EXCLUDE_PATTERNS = ("/blog", "/search", "/markdown-page", "/docs/intro")


def is_doc_url(url):
    parsed = urlparse(url)
    path = unquote(parsed.path)
    if not any(path.startswith(p) for p in DOC_PREFIXES):
        return False
    for bad in EXCLUDE_PATTERNS:
        if bad in path:
            return False
    return True


def url_to_filepath(url):
    parsed = urlparse(url)
    path = unquote(parsed.path).rstrip("/")
    if path.startswith("/"):
        path = path[1:]
    if path in ("game", "gta5", "rdr2", "misc", "home", "injecterror"):
        return None
    return OUT_DIR / (path + ".md")


def scrape_one(url):
    out_path = url_to_filepath(url)
    if out_path is None:
        return url, "skip-root", None

    if out_path.exists():
        return url, "exists", out_path

    try:
        resp = requests.get(url, timeout=TIMEOUT)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")

        article = (
            soup.find("article") or
            soup.find("main") or
            soup.find(class_=re.compile(r"markdown|content|docs", re.I)) or
            soup.find(class_=re.compile(r"container", re.I)) or
            soup.find("body")
        )
        if not article:
            return url, "no-content", None

        title_el = soup.find("h1") or soup.find("title")
        title = title_el.get_text(strip=True) if title_el else url.split("/")[-1]
        slug = urlparse(url).path.rstrip("/")

        # Remove nav/sidebar/breadcrumb elements
        for tag in article.find_all(
            ["nav", "header", "footer", "aside", "div", "a"],
            class_=re.compile(r"navbar|sidebar|nav|menu|toc|breadcrumb", re.I)
        ):
            tag.decompose()

        frontmatter = f"---\nsidebar_position: 1\ntitle: {title}\nslug: {slug}\n---\n\n"
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(frontmatter + str(article), encoding="utf-8")
        return url, "ok", out_path

    except Exception as e:
        return url, f"error: {e}", None


def main():
    print("Fetching sitemap...")
    all_urls = get_urls()
    doc_urls = sorted(set(u for u in all_urls if is_doc_url(u)))
    print(f"Found {len(doc_urls)} doc URLs out of {len(all_urls)} total")

    ok = exists = skipped = errors = 0

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        futures = {ex.submit(scrape_one, url): url for url in doc_urls}
        for i, future in enumerate(as_completed(futures), 1):
            url, status, path = future.result()
            if status == "ok":
                ok += 1
                print(f"[{i}/{len(doc_urls)}] ✓ {path.name}")
            elif status == "exists":
                exists += 1
            elif status == "skip-root":
                skipped += 1
            else:
                errors += 1
                print(f"[{i}/{len(doc_urls)}] ✗ {url}: {status}")

    print(f"\nDone! ok={ok} exists={exists} skipped={skipped} errors={errors}")
    print(f"Files saved in: {OUT_DIR}")


if __name__ == "__main__":
    main()