---
name: production-control
description: Maintain a Markdown production control board for recurring workstreams. Use when the user wants to scan recent activity, decide which durable artifacts belong on the board, update a status heatmap, fill a five-layer control table, and keep Now / Next / Later current across research, product, engineering, operations, automation, or agent workflows.
---

# Production Control

## Purpose

Keep an AI-assisted work portfolio visible, verifiable, and bounded.

Use this skill to update a Markdown control board that tracks durable workstreams through:

- Source
- Engine
- Output
- Verification
- One next action

## First Step

Read `references/production-control.md` for the full method when you need more detail. The compact workflow below is enough for routine updates.

Locate the board:

1. Prefer `board_path` from `.production-control.yml`.
2. Search for `Status Heatmap`, `Five-Layer Control Table`, `Now / Next / Later`, or local-language equivalents.
3. If no board exists, create one from the template in `templates/production-control-board.md` or make an equivalent Markdown board.

## Default Workflow

1. Read the current board.
2. Gather recent activity:
   - Run `scripts/scan_activity.py --config .production-control.yml` if available.
   - Inspect recent git commits, recently modified files, reports, generated artifacts, and agent memory files where available.
3. Decide which candidates are durable enough to add or update.
4. Classify accepted candidates using the five-layer model.
5. Update the quick read, status heatmap, five-layer table, and Now / Next / Later.
6. Re-read the file and verify Markdown table structure.

## Inclusion Rules

Add or update a row only when the item has at least one durable signal:

- Report, dashboard, script, dataset, service, automation, skill, command, published page, or recurring workflow.
- Real path, URL, command, service name, output directory, or owner.
- Repeated use: daily, weekly, release-based, review-based, or ad hoc but recurring.
- Cross-workstream impact.

Do not add one-off chat, unverified opinions, or tiny implementation details already covered by a broader line.

## Status Rules

Use only:

- `🟢 Stable`: usable today and has a concrete verification action.
- `🟡 Needs attention`: useful but has a gap in source, engine, output, or verification.
- `🔴 Do not rely`: cannot support decisions until a source or verification problem is fixed.
- `⚪ Parked`: preserved but not actively advanced.

Layer cells use only `🟢`, `🟡`, `🔴`, or `⚪`.

If source rights or verification are unclear, stay conservative and mark yellow. If verification is red, the overall status is usually red.

## Verification Standard

Verification must be executable:

- Open a URL and check a date.
- Run a command and confirm expected output.
- Compare the latest two snapshots.
- Check service status and latest log timestamp.
- Confirm a report covers the expected period.

Avoid vague actions such as "check", "improve", or "continue research".

## Output

After updating, summarize:

- Board path.
- Added or changed workstreams.
- Red or yellow items and why.
- Any evidence gaps.

Do not paste the entire board unless asked.

## Bundled Resources

- `references/production-control.md`: full agent-neutral method.
- `templates/production-control-board.md`: default Markdown board.
- `scripts/scan_activity.py`: dependency-free scanner for recent candidate artifacts.
