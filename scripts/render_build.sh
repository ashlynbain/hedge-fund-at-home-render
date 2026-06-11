#!/usr/bin/env bash
# Render build: install public toolkit + this API package.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

if [[ -d .toolkit ]]; then
  rm -rf .toolkit
fi

git clone --depth 1 https://github.com/ashlynbain/hedge-fund-at-home.git .toolkit
cp .toolkit/config/config.yaml.example .toolkit/config/config.yaml
pip install -e ".toolkit[dev]"
pip install -e ".[dev]"

# Code lab subprocesses need strategies/ on sys.path (sibling of hedgekit/, not inside the wheel).
TOOLKIT_ROOT="$(pwd)/.toolkit"
SITE_PACKAGES="$(python -c "import site; print(site.getsitepackages()[0])")"
echo "$TOOLKIT_ROOT" > "$SITE_PACKAGES/hfah_toolkit_root.pth"
