from __future__ import annotations
import json
from pathlib import Path

def save_json(obj, path: str | Path):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2)

def load_json(path: str | Path):
    p = Path(path)
    with p.open("r", encoding="utf-8") as f:
        return json.load(f)