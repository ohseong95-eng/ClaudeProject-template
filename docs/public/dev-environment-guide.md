# Development Environment Guide

> Reference document for setting up isolated development environments.

---

## Docker Container Development

Use Docker for safe, isolated development environments.

### Base Dockerfile

```dockerfile
FROM ubuntu:22.04
RUN apt-get update && apt-get install -y curl git tmux vim nodejs npm python3 python3-pip
RUN curl -fsSL https://claude.ai/install.sh | sh
WORKDIR /workspace
CMD ["/bin/bash"]
```

### Build & Run

```bash
docker build -t claude-sandbox .
docker run -it --rm -v $(pwd):/workspace -e ANTHROPIC_API_KEY=$ANTHROPIC_API_KEY claude-sandbox
```

### Worker Orchestration

A local main Claude can use tmux to dispatch tasks to worker Claudes inside containers and collect results.

---

## Sandbox Mode

Use `/sandbox` to auto-approve only trusted commands.

**Safe commands:**

| Category | Commands |
|----------|----------|
| **npm** | `npm install`, `npm test`, `npm run build`, `npm run lint`, `npm ci`, `npm ls` |
| **git (read-only)** | `git status`, `git diff`, `git log`, `git branch`, `git show`, `git rev-parse` |
| **file (read-only)** | `ls`, `cat`, `head`, `tail`, `wc`, `find`, `file`, `stat` |
| **search** | `grep`, `rg`, `ack`, `fd` |
| **build/test** | `make`, `pytest`, `jest`, `vitest`, `cargo test` |
| **info** | `node --version`, `python3 --version`, `which`, `echo`, `date` |

---

## YOLO Mode (`--dangerously-skip-permissions`)

**Allowed:** experiments inside containers, long autonomous tasks, trusted repetitive tasks
**Prohibited:** direct host execution, critical data directories, production environments

After using YOLO mode, include risky actions taken in the **final report**.

---

## Exponential Backoff (Long-running Tasks)

Progress checks for long-running tasks use exponential backoff: **1 min -> 2 min -> 4 min -> 8 min ...**
