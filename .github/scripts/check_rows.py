#!/usr/bin/env python3
import json
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[2]
seen = {}
ok = True
mods = root / "mods"
if mods.is_dir():
    for folder in mods.iterdir():
        info = folder / "mod.json"
        if not info.is_file():
            continue
        data = json.loads(info.read_text(encoding="utf-8"))
        row = data.get("row") or data.get("id")
        if not row:
            print("::error::missing row in", folder.name)
            ok = False
            continue
        if not str(row).endswith("-mod"):
            print("::error::row must end with -mod:", row)
            ok = False
        if row in seen:
            print(f"::error::duplicate row {row} in {folder.name} and {seen[row]}")
            ok = False
        seen[row] = folder.name
if not ok:
    sys.exit(1)
print("ok", len(seen), "rows")
