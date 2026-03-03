---
name: query-check-project-status
description: Check project status from the registry before starting work. Use when verifying if a project is active or disabled.
---

# Project Registry Lookup

Rules that agents follow when checking the current status of projects.

## Lookup Procedure

1. Read the **Project Registry** table in `docs/project-registry.md`
2. Check the **Status** column
   - **Active**: Available as a work target
   - **Disabled**: Excluded from agent execution, task assignments, and data send/receive
3. Verify that each project directory actually exists
4. Check the most recent file in each project's `output/` and `sessions/`

## Output Format

```markdown
## Project Status

| # | Project | Role | Latest Report | Latest Session | Status |
|---|---------|------|---------------|----------------|--------|
| 1 | ... | ... | output/... | sessions/... | Active / Disabled |
```

## Status Determination Criteria

| Status | Condition |
|--------|-----------|
| Active | Registry status = Active, CLAUDE.md exists, directory is intact |
| Disabled | Registry status = Disabled |
| Incomplete Setup | CLAUDE.md or required directories are missing |
| Not Found | Listed in registry but directory does not exist |

## Rules

- If an agent attempts to work on a Disabled project, **stop immediately** and report the reason
- All agents must verify the target project's status using this skill before starting work
