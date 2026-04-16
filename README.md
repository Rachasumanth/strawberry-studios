# Strawberry Studios

Strawberry Studios is an AI-powered desktop application built with modern web technologies and Rust. This monorepo contains all the components needed to build and deploy the application.

## Project Overview

Strawberry Studios is a desktop application that leverages artificial intelligence to enhance user productivity and creativity. The project is structured as a monorepo using pnpm workspaces, enabling seamless code sharing and dependency management across multiple packages.

## Architecture

### Packages

- **@strawberry/app** - Tauri desktop application frontend built with React and TypeScript
  - Provides the user interface and desktop integration
  - Built on Tauri for cross-platform compatibility (Windows, macOS, Linux)

- **@strawberry/agent** - Claw Worker Python daemon
  - Handles background processing and AI operations
  - Communicates with the desktop app via IPC
  - Manages long-running tasks and worker processes

- **@strawberry/shared** - Shared TypeScript types and utilities
  - Common type definitions used across packages
  - Utility functions and constants
  - Ensures type safety across the monorepo

## Technology Stack

- **Frontend**: React, TypeScript, Tauri
- **Backend**: Python (Claw Worker daemon)
- **Build Tools**: Turbo, pnpm
- **Monorepo Manager**: pnpm workspaces

## Getting Started

### Prerequisites

- Node.js 16+ and pnpm
- Python 3.8+
- Rust (for Tauri development)

### Installation

```bash
# Install dependencies
pnpm install

# Run development servers
pnpm dev

# Build all packages
pnpm build
```

## Development Workflow

This monorepo uses Turbo for build orchestration, enabling:

- Parallel builds across packages
- Incremental builds for changed packages
- Caching for faster development cycles
- Task pipelines with dependency management

## Project Structure

```
.
├── packages/
│   ├── app/          # Tauri desktop application
│   ├── agent/        # Python daemon worker
│   └── shared/       # Shared types and utilities
├── package.json      # Root package.json with workspaces
├── pnpm-workspace.yaml  # pnpm workspace configuration
├── turbo.json        # Turbo build pipeline configuration
└── README.md         # This file
```

## License

Strawberry Studios - All rights reserved
