# Production Control Skill

A portable workflow for keeping an AI-assisted work portfolio under control.

It helps an agent periodically scan recent work, decide which new artifacts deserve to enter a control board, and update a compact status heatmap with clear next actions.

The method is agent-neutral. This repository ships adapters for:

- Codex skills
- Claude Code custom slash commands

## What It Does

Production Control turns scattered work into a maintainable control board:

1. Find recent work across notes, repositories, reports, generated files, and agent memory.
2. Decide which items are durable assets rather than one-off conversations.
3. Classify each line through five layers:
   - Source
   - Engine
   - Output
   - Verification
   - Next action
4. Update a Markdown control board:
   - Overview map
   - Status heatmap
   - Five-layer table
   - Now / Next / Later queue

## Repository Layout

```text
production-control-skill/
├── codex/production-control/        # Codex skill adapter
├── claude-code/commands/            # Claude Code slash command adapter
├── core/                            # Agent-neutral method
├── templates/                       # Markdown board templates
├── scripts/                         # Portable helper scripts
└── examples/                        # Example config and output
```

## Install For Codex

Copy the Codex adapter into your local Codex skills folder:

```bash
mkdir -p ~/.codex/skills
cp -R codex/production-control ~/.codex/skills/production-control
```

Then invoke:

```text
Use $production-control to update my production control board.
```

## Install For Claude Code

Claude Code supports custom slash commands as Markdown files under `.claude/commands/` for a project or `~/.claude/commands/` for personal commands.

Project-level install:

```bash
mkdir -p .claude/commands
cp claude-code/commands/production-control.md .claude/commands/production-control.md
```

Then invoke in Claude Code:

```text
/production-control update my control board
```

## Configure

Create a `.production-control.yml` file in your workspace. Example:

```yaml
board_path: "notes/Production Control Board.md"
scan_roots:
  - "."
  - "notes"
  - "reports"
lookback_days: 7
include_keywords:
  - report
  - dashboard
  - skill
  - automation
  - strategy
exclude_dirs:
  - .git
  - node_modules
  - .venv
```

If no config file exists, the agent should ask for the board path or create one from `templates/production-control-board.md`.

## Status System

Use only four statuses:

| Status | Meaning |
|---|---|
| 🟢 Stable | Usable today and has a concrete verification action |
| 🟡 Needs attention | Runnable or useful, but has a gap in data, automation, output, or verification |
| 🔴 Do not rely on it | Cannot be used for decisions until a source or verification problem is fixed |
| ⚪ Parked | Preserved for reference, not actively advanced |

## Design Principles

- One line per durable workstream.
- One next action per line.
- Verification must be executable, not vague.
- Keep long analysis outside the control board and link to the real artifact.
- Prefer conservative status. If evidence is incomplete, mark yellow.

## License

MIT

