#!/usr/bin/env python3
"""Install Production Control adapters for Codex and/or Claude Code."""

from __future__ import annotations

import argparse
from pathlib import Path
import shutil


REPO = Path(__file__).resolve().parents[1]


def copytree(src: Path, dst: Path) -> None:
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)


def install_codex(home: Path) -> Path:
    target = home / ".codex" / "skills" / "production-control"
    target.parent.mkdir(parents=True, exist_ok=True)
    copytree(REPO / "codex" / "production-control", target)
    return target


def install_claude_code(home: Path, project: Path | None, with_assets: bool) -> Path:
    if project:
        target = project / ".claude" / "commands" / "production-control.md"
    else:
        target = home / ".claude" / "commands" / "production-control.md"
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(REPO / "claude-code" / "commands" / "production-control.md", target)
    if with_assets and project:
        (project / "scripts").mkdir(exist_ok=True)
        (project / "templates").mkdir(exist_ok=True)
        shutil.copy2(REPO / "scripts" / "scan_activity.py", project / "scripts" / "scan_activity.py")
        shutil.copy2(REPO / "templates" / "production-control-board.md", project / "templates" / "production-control-board.md")
    return target


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--codex", action="store_true", help="Install Codex skill adapter")
    parser.add_argument("--claude-code", action="store_true", help="Install Claude Code slash command")
    parser.add_argument("--project", help="Install Claude Code command into a project .claude/commands directory")
    parser.add_argument("--with-assets", action="store_true", help="When installing into a project, also copy scripts and templates")
    parser.add_argument("--home", default=str(Path.home()))
    args = parser.parse_args()

    if not args.codex and not args.claude_code:
        args.codex = True
        args.claude_code = True

    home = Path(args.home).expanduser()
    installed: list[str] = []
    if args.codex:
        installed.append(str(install_codex(home)))
    if args.claude_code:
        installed.append(str(install_claude_code(home, Path(args.project).resolve() if args.project else None, args.with_assets)))

    for path in installed:
        print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
