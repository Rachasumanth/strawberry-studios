# AGENTS.md — Instructions for OpenHands Coding Agent

You are building **Strawberry Studios**, a Tauri desktop application.
An orchestrator (OpenClaw/Gemini AI) decides WHAT to build. You execute it.

## ⚠️ MANDATORY: Completion Marker

When your task is fully done, you MUST write a completion marker:

```bash
TASK_ID="your-task-id-here"  # use the task_id from your instructions
mkdir -p /home/ubuntu/workspace/.task-complete
python3 -c "
import json
data = {
    'task_id': '$TASK_ID',
    'status': 'done',
    'files_created': [],  # list actual files you created
    'summary': 'One sentence describing what you built'
}
open('/home/ubuntu/workspace/.task-complete/$TASK_ID.json', 'w').write(json.dumps(data, indent=2))
"
```

**Without this marker, the orchestrator will think you failed and retry.**

## Git Discipline

After every meaningful change, commit:
```bash
cd /home/ubuntu/workspace
git add -A
git commit -m "feat(TASK_ID): description of change"
```

## Workspace Rules

- **Workspace root:** `/home/ubuntu/workspace`
- **Tech stack (fixed):** Tauri (Rust) + React + TypeScript + pnpm + turbo
- **Check what exists FIRST** before creating files (`ls`, `cat` existing files)
- **Do NOT overwrite working code** — read before writing
- **Do NOT install packages** outside the project's tech stack

## If Something Fails

1. Try a different approach — don't give up immediately
2. Document the failure in your completion marker with `"status": "failed"` and `"error": "what went wrong"`
3. Commit any partial work with a clear message

## Current Project State

The monorepo scaffold is already created. You will find:
- `/home/ubuntu/workspace/packages/app/` — Tauri frontend (empty, needs code)
- `/home/ubuntu/workspace/packages/agent/` — Python Claw Worker (empty, needs code)  
- `/home/ubuntu/workspace/packages/shared/` — Shared TypeScript types (empty, needs code)
- `/home/ubuntu/workspace/package.json` — root pnpm workspace config
- `/home/ubuntu/workspace/turbo.json` — build pipeline config

## Technology Reference

- **Tauri:** `cargo tauri init` for scaffold, `src-tauri/` for Rust, `src/` for React
- **ReactFlow:** `npm install reactflow` for node editor
- **CodeMirror:** `npm install @codemirror/view @codemirror/state` for notebook cells
- **Zustand:** state management
- **Framer Motion:** animations
- **Claw Worker:** pure Python daemon with `asyncio` + `websockets` library

## What "Done" Means Per Task

Each task's instructions will specify the completion criteria. Make sure you meet ALL of them before writing the marker.
