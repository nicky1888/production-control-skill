#!/usr/bin/env python3
"""Scan recent candidate artifacts for a production control board.

This script is intentionally lightweight and dependency-free. It does not decide
status; it only collects candidate evidence for an agent to inspect.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import time


DEFAULT_CONFIG = {
    "board_path": "",
    "scan_roots": ["."],
    "lookback_days": 7,
    "include_keywords": [
        "report",
        "dashboard",
        "skill",
        "automation",
        "service",
        "release",
        "strategy",
    ],
    "exclude_dirs": [".git", "node_modules", ".venv", "__pycache__"],
}


def parse_simple_yaml(path: Path) -> dict[str, object]:
    if not path.exists():
        return dict(DEFAULT_CONFIG)

    cfg: dict[str, object] = dict(DEFAULT_CONFIG)
    current_list_key: str | None = None
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.split("#", 1)[0].rstrip()
        if not line.strip():
            continue
        if line.startswith("  - ") and current_list_key:
            value = line[4:].strip().strip('"').strip("'")
            cfg.setdefault(current_list_key, [])
            assert isinstance(cfg[current_list_key], list)
            cfg[current_list_key].append(value)
            continue
        if ":" in line and not line.startswith(" "):
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()
            if value == "":
                cfg[key] = []
                current_list_key = key
            else:
                current_list_key = None
                if value.isdigit():
                    cfg[key] = int(value)
                else:
                    cfg[key] = value.strip('"').strip("'")
    return cfg


def is_skipped(path: Path, exclude_dirs: list[str]) -> bool:
    return any(part in exclude_dirs for part in path.parts)


def recent_files(root: Path, cfg: dict[str, object], limit: int) -> list[dict[str, object]]:
    days = int(cfg.get("lookback_days", 7))
    cutoff = time.time() - days * 86400
    include_keywords = [str(x).lower() for x in cfg.get("include_keywords", [])]
    exclude_dirs = [str(x) for x in cfg.get("exclude_dirs", [])]
    scan_roots = [Path(str(x)) for x in cfg.get("scan_roots", ["."])]

    out: list[dict[str, object]] = []
    for scan_root in scan_roots:
        base = scan_root if scan_root.is_absolute() else root / scan_root
        if not base.exists():
            continue
        for path in base.rglob("*"):
            if is_skipped(path, exclude_dirs) or not path.is_file() or path.name.startswith("."):
                continue
            try:
                stat = path.stat()
            except OSError:
                continue
            if stat.st_mtime < cutoff:
                continue
            path_text = str(path)
            if include_keywords and not any(k in path_text.lower() for k in include_keywords):
                continue
            out.append(
                {
                    "path": path_text,
                    "mtime": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(stat.st_mtime)),
                    "size": stat.st_size,
                }
            )
    out.sort(key=lambda item: str(item["mtime"]), reverse=True)
    return out[:limit]


def find_boards(root: Path) -> list[str]:
    headings = ("Status Heatmap", "Five-Layer Control Table", "Now / Next / Later")
    found: list[str] = []
    for path in root.rglob("*.md"):
        if is_skipped(path, [".git", "node_modules", ".venv", "__pycache__"]):
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        if any(h in text for h in headings):
            found.append(str(path))
    return sorted(found)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default=".production-control.yml")
    parser.add_argument("--root", default=".")
    parser.add_argument("--limit", type=int, default=80)
    args = parser.parse_args()

    root = Path(args.root).resolve()
    cfg = parse_simple_yaml(root / args.config)
    payload = {
        "root": str(root),
        "config": cfg,
        "configured_board": str(root / str(cfg.get("board_path", ""))) if cfg.get("board_path") else "",
        "discovered_boards": find_boards(root),
        "recent_files": recent_files(root, cfg, args.limit),
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

