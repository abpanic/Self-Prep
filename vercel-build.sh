#!/usr/bin/env bash
# Vercel build step: install Quarto, then render the site.
#
# Nothing is executed at render time (see `execute.enabled: false` in _quarto.yml)
# because every notebook ships with its outputs already stored. That means this
# build needs no scikit-learn, no dataset downloads and no JDK — Quarto renders
# the whole site on its own.
#
# The one addition is tools/postprocess_site.py, which needs a bare Python 3 (no
# third-party packages) to write robots.txt and match canonical/sitemap URLs to
# the clean URLs Vercel serves. If no interpreter is found the build still
# succeeds and simply ships Quarto's own robots.txt and sitemap.
#
# If you would rather not install Quarto on every build, the alternative is to
# render locally and commit the `_site/` directory: drop `_site/` from
# .gitignore, set `buildCommand` to "" in vercel.json, and Vercel will simply
# serve the static files.
set -euo pipefail

# Pinned deliberately. Match this to your local Quarto so the site you previewed
# is the site that ships; `quarto --version` locally tells you what to put here.
QUARTO_VERSION="1.10.18"
TARBALL="quarto-${QUARTO_VERSION}-linux-amd64.tar.gz"
URL="https://github.com/quarto-dev/quarto-cli/releases/download/v${QUARTO_VERSION}/${TARBALL}"

echo "==> Installing Quarto ${QUARTO_VERSION}"
mkdir -p "${HOME}/opt"
curl -fsSL "${URL}" -o "/tmp/${TARBALL}"
tar -xzf "/tmp/${TARBALL}" -C "${HOME}/opt"
export PATH="${HOME}/opt/quarto-${QUARTO_VERSION}/bin:${PATH}"

quarto --version

echo "==> Rendering site"
quarto render

# robots.txt, plus canonical/sitemap URLs matched to the clean URLs Vercel serves.
echo "==> Post-processing for crawlers"
PY_BIN=""
for candidate in python3 python; do
  if command -v "${candidate}" >/dev/null 2>&1; then PY_BIN="${candidate}"; break; fi
done
if [ -n "${PY_BIN}" ]; then
  "${PY_BIN}" tools/postprocess_site.py _site
else
  echo "WARNING: no python3 on PATH; shipping Quarto's robots.txt and sitemap unmodified" >&2
fi

echo "==> Done. Output in _site/"
ls -la _site | head -20
