# RoweMod Gallery

Shared clothing mods for [RoweMod × Rollout](https://github.com/xrowex/RoweMod-Rollout).

Players subscribe in RoweMod → **Gallery**. Authors submit a pull request from the same button. Nothing is playable until a maintainer merges.

## Rules

- Original work only. No ripped game meshes, textures, or `dumps/`.
- Cooked files must belong to a `-mod` item. Never `main-rig` or `MI-Upper`.
- `row` must be unique across `mods/*/mod.json`.

## Layout

```
mods/<id>/
  mod.json
  item.json
  preview.png
  files.json
  cooked/...
catalog.json
```

`catalog.json` is rebuilt on every push to `main`.
