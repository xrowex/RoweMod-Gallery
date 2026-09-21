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
    data = json.loads(info.read_text(encoding="utf-8-sig"))
    rel = "mods/" + folder.name
    mods.append(
        {
            "id": data.get("id") or data.get("Id") or folder.name,
            "title": data.get("title") or data.get("Title") or folder.name,
            "author": data.get("author") or data.get("Author") or "",
            "slot": data.get("slot") or data.get("Slot") or "",
            "row": data.get("row") or data.get("Row") or data.get("id") or data.get("Id") or folder.name,
            "version": data.get("version") or data.get("Version") or "1",
            "path": rel,
            "preview": rel + "/preview.png" if (folder / "preview.png").is_file() else None,
        }
    )
out = {"repo": "xrowex/RoweMod-Gallery", "mods": mods}
(root / "catalog.json").write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
print("wrote catalog.json", len(mods))
