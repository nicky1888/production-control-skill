# Production Control Method

Use this method when a user wants to periodically update a Markdown control board for ongoing workstreams, research lines, products, automations, or project assets.

## Workflow

1. Locate the control board.
   - Prefer `board_path` from `.production-control.yml`.
   - If absent, search for headings such as `Status Heatmap`, `Five-Layer Control Table`, `Now / Next / Later`, or equivalent local-language headings.
   - If no board exists, create one from `templates/production-control-board.md`.
2. Gather recent activity.
   - Use `scripts/scan_activity.py --config .production-control.yml` when available.
   - Also inspect recent git commits, recently modified files, reports, generated artifacts, and agent memory files if available.
3. Decide whether each candidate belongs on the board.
4. Classify each accepted item using the five-layer model.
5. Update the board sections:
   - Quick read
   - Overview map
   - Status heatmap
   - Five-layer control table
   - Now / Next / Later
6. Re-read the board and verify Markdown table structure.

## Inclusion Criteria

Add or update a line only if at least one condition is true:

- It has a durable artifact: report, dashboard, script, dataset, service, automation, skill, command, or published page.
- It will recur: daily, weekly, ad hoc but repeated, or used as a reusable decision workflow.
- It affects other workstreams.
- It has a real path, URL, command, service name, or output directory.

Do not add:

- One-off chat.
- Unverified market opinions or brainstorming with no artifact.
- Minor implementation details that are already covered by a broader line.
- Items with no next action and no verification path.

## Five-Layer Model

Each line must have:

| Layer | Question |
|---|---|
| Source | What does it consume? Is the source authorized and stable? |
| Engine | What script, service, command, skill, workflow, or team process handles it? |
| Output | What does the user actually see or use? |
| Verification | What exact action proves it is current and usable? |
| Next action | What is the one most important next step? |

Verification must be concrete:

- Open a URL and check the displayed date.
- Run a command and confirm a zero exit or expected row count.
- Compare the latest two snapshot files.
- Check service status, latest log timestamp, and generated output.
- Confirm the report links to the expected data period.

Avoid vague wording such as "check it", "improve it", or "continue research".

## Status Rules

Overall status:

- `🟢 Stable`: usable today and has a concrete verification action.
- `🟡 Needs attention`: useful but has a gap in source, engine, output, or verification.
- `🔴 Do not rely`: cannot support decisions until a source or verification problem is fixed.
- `⚪ Parked`: preserved but not actively advanced.

Layer status:

- `🟢`: this layer is usable today.
- `🟡`: this layer has a known limitation.
- `🔴`: this layer blocks use.
- `⚪`: paused or not applicable.

Priority rules:

1. If verification is red, the overall status is usually red.
2. If source rights or source stability are unclear, the overall status is at most yellow.
3. If the output exists but no one knows how to verify it, the overall status is at most yellow.
4. If the line is intentionally inactive, mark it parked instead of yellow.

## Board Hygiene

- Keep the board short.
- One row per workstream.
- One next action per row.
- `Now` should have no more than three items.
- Long analysis belongs in linked artifacts, not in the control board.
- Prefer conservative status when evidence is incomplete.

