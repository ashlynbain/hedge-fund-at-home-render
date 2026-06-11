"""Resolve toolkit and site paths independent of process cwd."""
from __future__ import annotations

import os
import sys
from pathlib import Path

_SERVICE_ROOT = Path(__file__).resolve().parents[1]


def toolkit_root() -> Path:
    env = os.environ.get("HFAH_TOOLKIT_ROOT", "").strip()
    if env:
        p = Path(env)
        if not p.is_absolute():
            p = (_SERVICE_ROOT / p).resolve()
        else:
            p = p.resolve()
        return p
    sibling = _SERVICE_ROOT.parent / "hedge-fund-at-home"
    if (sibling / "hedgekit").is_dir():
        return sibling.resolve()
    return _SERVICE_ROOT


def ensure_toolkit_on_path() -> Path:
    root = toolkit_root()
    entry = str(root)
    if entry not in sys.path:
        sys.path.insert(0, entry)
    return root
