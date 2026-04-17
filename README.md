# Strawberry Studios

**A Distributed AI Operating System — Your Virtual AI Lab**

Strawberry Studios makes heterogeneous compute (Local, AWS, Colab, etc.) feel like
one unified workspace. It is the "VS Code of AI infrastructure" — a desktop application
where you visually build, run, and reproduce AI experiments across any hardware.

---

## What It Is

A **Tauri desktop app** (Rust + React) that lets AI researchers:

1. **See all their compute** in one place — local machine, cloud VMs, Colab notebooks
2. **Build pipelines visually** — drag-and-drop nodes in a canvas (like a DAG editor)
3. **Write code** in a Jupyter-like notebook that stays in sync with the node graph
4. **Run on any machine** — one-command install of the Claw Worker daemon on any hardware
5. **Package experiments** as `.berry` files — reproducible, shareable, portable

---

## Architecture

```
DESKTOP APP (Tauri — Rust + React)
├── Node Editor     → ReactFlow canvas — visual pipeline builder
├── Notebook        → CodeMirror cells — Jupyter-like code/markdown
├── Asset Browser   → .berry file manager — datasets, weights, scripts
└── RPC Server      → WebSocket/gRPC bridge to Claw Workers

CLAW WORKER (Python daemon — runs on any hardware)
├── WebSocket server (port 7331) — receives commands from desktop app
├── Script executor — runs Python/Rust/Mojo, streams stdout back
├── Telemetry — CPU/RAM/GPU every 5s
└── Systemd service — auto-reconnects on disconnect
```

---

## Key Design Decisions

| Decision | Choice | Reason |
|----------|--------|--------|
| Desktop framework | **Tauri** (not Electron) | 15MB binary, Rust safety, native speed |
| Node editor | **ReactFlow** | Best graph UI library |
| Notebook | **CodeMirror 6** | Lightweight, fast, extensible |
| Claw Worker | **Pure Python** | Works on any machine with Python |
| Package format | **.berry** (ZIP+JSON) | One file = one reproducible experiment |
| Communication | **WebSocket → gRPC → HTTP** | Adaptive to any network environment |

---

## Monorepo Structure

```
strawberry-studios/
├── packages/
│   ├── app/          # Tauri desktop application (React + TypeScript)
│   ├── agent/        # Claw Worker Python daemon
│   └── shared/       # Shared TypeScript types and utilities
├── package.json      # pnpm workspace root
├── pnpm-workspace.yaml
└── turbo.json        # Build pipeline
```

---

## The .berry Package Format

Projects are saved as `.berry` files (ZIP archives):
```
project.berry (ZIP)
├── project.json    # Node graph + notebook cells (Unified State Model)
├── /scripts        # Python/Rust/Mojo source files
├── /data           # Content-addressed datasets & weights (hash dedup)
└── /env            # Dependencies (conda env.yaml, pip requirements.txt)
```

---

## Built By

This project is being autonomously developed by an agentic pipeline:
- **OpenClaw (Gemini AI)** — Research brain, plans and decides what to build
- **OpenHands (Claude/GPT-4o)** — Coding executor, writes the actual code
