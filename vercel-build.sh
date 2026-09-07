#!/usr/bin/env bash
# Vercel build step: install Quarto, then render the site.
#
# Nothing is executed at render time (see `execute.enabled: false` in _quarto.yml)
# because every notebook ships with its outputs already stored. That means this
# build needs no Python, no scikit-learn, no dataset downloads and — once the DSA
# series exists — no JDK. Quarto alone is enough.
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

echo "==> Done. Output in _site/"
ls -la _site | head -20
