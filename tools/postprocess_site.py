#!/usr/bin/env python3
"""Post-render fixes for the published site. Run after `quarto render`.

Two jobs, both about being crawlable and being found:

1. Write an explicit robots.txt. Quarto writes one containing only a `Sitemap:`
   line, which works (crawling is allowed by default) but says nothing out loud.

2. Reconcile URLs with how Vercel actually serves the site. vercel.json sets
   `cleanUrls: true`, so `/foo.html` 308-redirects to `/foo` and `/foo` is the
   URL a visitor lands on. Quarto, knowing nothing about that, writes `.html`
   into both sitemap.xml and every canonical link — so every canonical and every
   sitemap entry pointed at a URL that redirects somewhere else. Search engines
   resolve that eventually; it is better not to make them.

Idempotent: running it twice changes nothing the second time.
"""
from __future__ import annotations

import io
import pathlib
import re
import sys

SITE = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "_site").resolve()
SITE_URL = "https://self-prep-seven.vercel.app"

ROBOTS = """\
# Everything here is meant to be read, indexed and linked to.
User-agent: *
Allow: /

# Build artefacts and search plumbing - no value in an index, and search.json is
# a large file that is only useful to the site's own search box.
Disallow: /site_libs/
Disallow: /search.json

Sitemap: %s/sitemap.xml
""" % SITE_URL


def clean_url(url: str) -> str:
    """Match Vercel's cleanUrls: drop `.html`, and drop a trailing `index`."""
    if not url.endswith(".html"):
        return url
    url = url[: -len(".html")]
    if url.endswith("/index"):
        url = url[: -len("index")]          # .../index.html -> .../
    if url == SITE_URL:
        url += "/"
    return url


def main() -> int:
    if not SITE.is_dir():
        print("no such directory: %s" % SITE, file=sys.stderr)
        return 1

    robots = SITE / "robots.txt"
    robots.write_text(ROBOTS, encoding="utf-8")
    print("wrote %s" % robots.relative_to(SITE.parent))

    sitemap = SITE / "sitemap.xml"
    if sitemap.exists():
        text = io.open(sitemap, encoding="utf-8").read()
        rewritten = re.sub(r"<loc>([^<]+)</loc>",
                           lambda m: "<loc>%s</loc>" % clean_url(m.group(1)), text)

        # Two source paths can collapse to one served URL (index.html and the
        # directory itself), and a partial re-render can append a duplicate.
        # Either way a sitemap should list each URL once.
        seen: set[str] = set()
        removed = 0

        def dedupe(match: re.Match) -> str:
            nonlocal removed
            loc = re.search(r"<loc>([^<]+)</loc>", match.group(0))
            if loc and loc.group(1) in seen:
                removed += 1
                return ""
            if loc:
                seen.add(loc.group(1))
            return match.group(0)

        rewritten = re.sub(r"\s*<url>.*?</url>", dedupe, rewritten, flags=re.S)
        rewritten = rewritten.replace("</urlset>", "\n</urlset>")
        if rewritten != text:
            io.open(sitemap, "w", encoding="utf-8").write(rewritten)
        print("sitemap.xml: %d urls normalised to the served (clean) form%s"
              % (len(seen), ", %d duplicate(s) dropped" % removed if removed else ""))
    else:
        print("WARNING: no sitemap.xml - is site-url set in _quarto.yml?", file=sys.stderr)

    # Canonical links, same treatment.
    changed = 0
    pages = sorted(SITE.rglob("*.html"))
    missing = []
    for page in pages:
        if "site_libs" in page.parts:
            continue
        html = io.open(page, encoding="utf-8", errors="surrogateescape").read()
        if 'rel="canonical"' not in html:
            missing.append(page.relative_to(SITE).as_posix())
            continue
        new = re.sub(
            r'(<link[^>]*\brel="canonical"[^>]*\bhref=")([^"]+)(")',
            lambda m: m.group(1) + clean_url(m.group(2)) + m.group(3),
            html,
        )
        if new != html:
            io.open(page, "w", encoding="utf-8", errors="surrogateescape").write(new)
            changed += 1
    print("canonical links: %d rewritten across %d pages" % (changed, len(pages)))
    if missing:
        print("WARNING: %d page(s) have no canonical link: %s"
              % (len(missing), ", ".join(missing[:5])), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
