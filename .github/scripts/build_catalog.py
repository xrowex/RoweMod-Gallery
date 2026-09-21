#!/usr/bin/env python3
import json
from pathlib import Path

root = Path(__file__).resolve().parents[2]
mods_dir = root / "mods"
mods = []
for folder in sorted(mods_dir.iterdir() if mods_dir.exists() else []):
    info = folder / "mod.json"
    if not info.is_file():
        continue
    data = json.loads(info.read_text(encoding="utf-8"))
    rel = "mods/" + folder.name
    mods.append(
        {
            "id": data.get("id", folder.name),
            "title": data.get("title", folder.name),
            "author": data.get("author", ""),
            "slot": data.get("slot", ""),
            "row": data.get("row", data.get("id", folder.name)),
            "version": data.get("version", "1"),
            "path": rel,
            "preview": rel + "/preview.png" if (folder / "preview.png").is_file() else None,
        }
    )
out = {"repo": "xrowex/RoweMod-Gallery", "mods": mods}
(root / "catalog.json").write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
print("wrote catalog.json", len(mods))
