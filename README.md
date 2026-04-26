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

## 中文说明

Production Control Skill 是一个通用的“生产总控”工作流，用来管理长期并行推进的研究线、产品线、自动化、报告、脚本、服务和 agent 技能。

它解决的问题是：当你不断用 AI agent 做研究、写报告、生成脚本、搭建 dashboard、配置自动化之后，资产会越来越多，但你很快会忘记哪些已经稳定可用，哪些只是一次性实验，哪些需要继续维护。Production Control 把这些分散产物收敛到一张 Markdown 总控表里。

### 它适合谁

- 同时维护多条研究线、产品线或工程线的人。
- 经常让 Codex、Claude Code 或其他 agent 生成报告、脚本、服务和自动化的人。
- 希望每周或不定期复盘“最近做了什么、哪些可以沉淀、哪些还不可靠”的团队。
- 想用 Markdown/Obsidian/Git repo 管理工作资产，而不是只靠聊天记录回忆的人。

### 核心逻辑

每条工作线都按五层来管理：

| 层级 | 要回答的问题 |
|---|---|
| Source | 它吃什么输入？数据、文档、事件、反馈是否稳定？ |
| Engine | 哪个脚本、服务、agent skill、命令或人工流程在处理？ |
| Output | 用户实际看到或使用的是什么？报告、网页、dashboard、提醒、数据文件？ |
| Verification | 怎么证明它今天真的可用？必须是可执行的检查动作。 |
| Next action | 当前最重要的一件下一步是什么？ |

这样可以避免把“想法、工具、报告、服务、自动化、产品入口”混在一起。

### 状态系统

只使用四种状态：

| 状态 | 含义 |
|---|---|
| 🟢 Stable | 今天可用，并且知道怎么验证 |
| 🟡 Needs attention | 能跑或有价值，但数据、自动化、输出或验证还有缺口 |
| 🔴 Do not rely on it | 暂时不能拿它做判断，必须先修数据源或验证问题 |
| ⚪ Parked | 暂停推进，只保留为资料 |

总控表不是为了记录所有事情，而是为了让你第一眼看到：哪些线稳定，哪些线要盯，哪些线不能信，哪些线可以先放下。

### Codex 使用方式

把 Codex adapter 复制到本地 skills 目录：

```bash
mkdir -p ~/.codex/skills
cp -R codex/production-control ~/.codex/skills/production-control
```

然后在 Codex 里调用：

```text
Use $production-control to update my production control board.
```

### Claude Code 使用方式

Claude Code 通过 custom slash command 使用：

```bash
mkdir -p .claude/commands
cp claude-code/commands/production-control.md .claude/commands/production-control.md
```

然后在 Claude Code 里调用：

```text
/production-control update my control board
```

### 配置方式

在你的工作区创建 `.production-control.yml`：

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

如果没有配置文件，agent 应该先询问总控表路径，或者用 `templates/production-control-board.md` 创建一张新的 Markdown 总控表。

### 使用原则

- 一条工作线只占一行。
- 一条工作线只能有一个下一步。
- 验证动作必须具体，比如打开 URL 看日期、运行命令看输出、比较两个快照、检查服务日志。
- 长分析不要塞进总控表，只链接到真实报告或文档。
- 证据不足时宁愿标黄，不要假装稳定。

## License

MIT
