# Agent Rename

Renames an agent: file names, YAML `name` field, and all references across the project.

## Arguments

$ARGUMENTS — `<old_name> <new_name>` (both without version suffix)

Example: `/agent:rename repair-fix-agent-format audit-fix-agent-format`

## Output Rules

- Show change list before executing; proceed only after user confirmation
- No intermediate explanations — progress and results only

## Procedure

### Step 1 — Parse Arguments

1. Split `$ARGUMENTS` into `old_name` and `new_name`
2. If either is missing, ask the user
3. Validate format: lowercase, hyphens, no dots or version suffix

### Step 2 — Locate Agent Files

Glob for `**/{old_name}.agent-v*.md` and `**/{old_name}.agent-v*.kr` from project root.

If no files found, report error and stop.

### Step 3 — Scan References

Grep `old_name` across the entire project. Classify each match:

| Update | Location |
|--------|----------|
| YES | Agent files (.md + .kr) — filename and YAML `name` field |
| YES | Other agent/skill body text (cross-references) |
| YES | `docs/component-audit-status.md` |
| YES | `.claude/naming-convention-map.md` — Used In column |
| YES | `output/project-overview.md` |
| YES | `todo/` files |
| YES | `.claude/commands/` files |
| YES | `docs/public/file-naming-convention.md` |
| NO (history) | `make/` — design docs and changelogs |
| NO (history) | `sessions/` — session records |
| NO (history) | `input/` — task inputs |
| NO (history) | `output/` — reports (except `project-overview.md`) |
| NO (history) | `handoffs/` — archived handoffs |

### Step 4 — Present Change Plan

Show the user a table:

```
## Rename: {old_name} → {new_name}

### File Renames
| # | Current Path | New Path |
|---|-------------|----------|

### Content Updates
| # | File | Line | Change |
|---|------|------|--------|

### Skipped (history preservation)
| # | File | Reason |
|---|------|--------|
```

Ask user to confirm.

### Step 5 — Execute Changes

In this order:

1. **Rename files** — `mv` old path to new path (both `.md` and `.kr`)
2. **Fix YAML `name` field** — Edit the `name:` line in each renamed file
3. **Update references** — Replace `old_name` with `new_name` in all YES-classified files

### Step 6 — Verify

1. Grep `old_name` across the project
2. Filter out history files (make/, sessions/, input/, output/ except project-overview.md, handoffs/)
3. If remaining matches > 0, report them as warnings
4. Verify YAML `name` matches filename base in all renamed files

### Step 7 — Report

```
## Rename Complete

| Item | Value |
|------|-------|
| Old Name | {old_name} |
| New Name | {new_name} |
| Files Renamed | N |
| References Updated | N |
| History Files Skipped | N |
| Stale References | 0 (or list) |
```
