#!/usr/bin/env bash
# Builds a temporary docs/ folder of symlinks to the real notes (no copy is kept) and serves or builds the site.
# Usage: bash scripts/serve_site.sh [build]
set -e
cd "$(dirname "$0")/.."
rm -rf docs && mkdir docs
for d in 0*-*; do ln -s "../$d" "docs/$d"; done
ln -s ../assets docs/assets; ln -s ../README.md docs/index.md; ln -s ../TRANSCRIPTION_NOTES.md docs/TRANSCRIPTION_NOTES.md
if [ "$1" = "build" ]; then mkdocs build -d site; else mkdocs serve; fi