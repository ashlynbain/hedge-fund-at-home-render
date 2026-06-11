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
