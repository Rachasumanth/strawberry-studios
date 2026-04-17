# AGENTS.md — Instructions for OpenHands Coding Agent

You are building **Strawberry Studios** — a Distributed AI Operating System / Virtual AI Lab.
An orchestrator (OpenClaw/Gemini) decides WHAT to build. You execute it.

---

## ⚠️ THE TRUE VISION (Read This First)

Strawberry Studios is NOT a generic desktop app. It is a **Virtual AI Lab** where:
- Researchers control multiple compute machines (local, AWS, Colab) from ONE visual interface
- A **Node Editor canvas** (ReactFlow) is the primary UI — visual pipeline builder
- A **Notebook** (CodeMirror) is secondary — stays in BIDIRECTIONAL SYNC with the node graph
- **Claw Workers** (Python daemons) run on remote machines and accept commands via WebSocket
- Projects are packaged as **.berry files** (ZIP archives with project.json, scripts, data, env)
- The desktop app is **Tauri** (Rust + React) — NOT Electron, NOT a web app

**Architecture:**
```
Tauri Desktop App → WebSocket/gRPC → Claw Worker Daemon (port 7331)
     (Control Center)                   (on any machine)
```

---

## ⚠️ MANDATORY: Completion Marker

When your task is fully done, you MUST write:

```bash
TASK_ID="your-task-id-here"
mkdir -p /home/ubuntu/workspace/.task-complete
python3 -c "
import json
data = {
    'task_id': '$TASK_ID',
    'status': 'done',
    'files_created': [],
    'summary': 'One sentence of what you built'
}
open('/home/ubuntu/workspace/.task-complete/$TASK_ID.json','w').write(json.dumps(data,indent=2))
print('Completion marker written')
"
```

**Without this, the orchestrator thinks you failed and retries.**

---

## Git Discipline

```bash
cd /home/ubuntu/workspace
git add -A
git commit -m "feat(TASK_ID): what you built"
```

---

## Workspace Rules

- **Root:** `/home/ubuntu/workspace`
- **Check existing code FIRST** — `ls`, `cat` before writing anything
- **Never overwrite working code** without reading it first
- **Tech stack is fixed** — Tauri + React + TypeScript + pnpm + Turbo + Python Claw Worker

---

## Current Build State

| Package | Purpose | Status |
|---------|---------|--------|
| `packages/app/` | Tauri desktop app (React frontend) | Scaffold only — needs Tauri init |
| `packages/agent/` | Claw Worker Python daemon | WebSocket server in progress |
| `packages/shared/` | Shared TypeScript types | Empty — fill as needed |

---

## Technology Reference

- **Tauri:** `cargo tauri init` inside `packages/app/`
- **Claw Worker:** `asyncio` + `websockets` library (pure Python, no heavy deps)
- **ReactFlow:** `npm install reactflow` for the node editor canvas
- **CodeMirror 6:** `npm install @codemirror/view @codemirror/state @codemirror/lang-python`
- **Zustand:** state management for USM (Unified State Model)
- **Framer Motion:** animations
- **WebSocket protocol:** messages are JSON. Claw Worker listens on `ws://0.0.0.0:7331`
