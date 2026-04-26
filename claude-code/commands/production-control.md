---
description: Update a Markdown production control board and status heatmap
argument-hint: [update request]
allowed-tools: Bash(find:*), Bash(rg:*), Bash(git status:*), Bash(git log:*), Bash(python3:*), Read, Edit, Write
---

# Production Control

Your task: $ARGUMENTS

Maintain a Markdown control board for recurring workstreams. The board should show what exists, what is usable, what needs attention, and the one next action for each line.

## Method

1. Locate the board.
   - Prefer `board_path` in `.production-control.yml`.
   - Otherwise search for `Status Heatmap`, `Five-Layer Control Table`, `Now / Next / Later`, or equivalent headings.
   - If no board exists, create one from `templates/production-control-board.md` if present.
2. Gather recent activity.
   - If present, run:
     ```bash
     python3 scripts/scan_activity.py --config .production-control.yml
     ```
   - Also inspect recent git commits and recently modified reports, dashboards, scripts, services, skills, commands, automations, or generated files.
3. Add or update only durable workstreams:
   - Has a real artifact, path, command, URL, service, or output.
   - Will be reused or reviewed repeatedly.
   - Affects other workstreams.
4. Classify each accepted line through five layers:
   - Source
   - Engine
   - Output
   - Verification
   - One next action
5. Update:
   - Quick Read
   - Status Heatmap
   - Five-Layer Control Table
   - Now / Next / Later

## Status Rules

Use only:

- `🟢 Stable`: usable today and has a concrete verification action.
- `🟡 Needs attention`: useful but has a gap.
- `🔴 Do not rely`: cannot support decisions until source or verification is fixed.
- `⚪ Parked`: preserved but not active.

Layer cells use only `🟢`, `🟡`, `🔴`, or `⚪`.

## Verification Standard

Verification must be executable. Examples:

- Open a URL and check a displayed date.
- Run a command and confirm expected output.
- Compare the latest two snapshot files.
- Check service status and latest log timestamp.
- Confirm a report covers the expected period.

Do not write vague next actions such as "check it", "improve", or "continue research".

## Final Response

Report only:

- The board path.
- Added or changed workstreams.
- Red/yellow items and why.
- Any evidence gaps.

Do not paste the whole board unless explicitly requested.

