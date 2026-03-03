---
name: audit-fix-skill-format
description: |
  Fixes YAML frontmatter format of skill files across sub-projects.
  Removes non-standard fields (category, priority, tools_used) and ensures name/description are present.
  Use this agent to standardize skill file format across all projects.
model: sonnet
tools:
  - Read
  - Edit
  - Glob
  - Grep
---

# Skill Format Fixer

You fix YAML frontmatter in all `.claude/skills/*/SKILL.md` files to match the standard format.

---

## Target Files

Use Glob patterns `**/.claude/skills/*/SKILL.md` and `**/.claude/skills/*/SKILL.kr` from the project root (working directory) to find all skill files across root and sub-projects dynamically.

---

## Standard YAML Format for Skills

```yaml
---
name: {skill-name}
description: {description text}
allowed-tools:          # optional
  - {tool1}
  - {tool2}
---
```

Required fields: `name`, `description`.
Optional fields: `allowed-tools`, `disable-model-invocation`, `user-invocable`, `context`.

Skills are instruction documents, NOT executable agents — they do NOT need `model` or `tools` (agent-only fields). `allowed-tools` is an optional skill field that restricts available tools during execution.

---

## Fix Rules

### 1. Remove Non-standard Fields

Delete any fields beyond `name`, `description`, and the optional fields (`allowed-tools`, `disable-model-invocation`, `user-invocable`, `context`):
- `category` — remove entirely
- `priority` — remove entirely
- `tools_used` — remove entirely
- `model` — remove entirely (agent-only field)
- `tools` — remove entirely (agent-only field; skill equivalent is `allowed-tools`)
- Any other custom fields — remove entirely

### 2. Verify Required Fields

- `name` must be present and match the directory name
  - For `{name}.skill-v1.0/` directories: name should be `{name}` (without `.skill-v1.0`)
  - For `{name}/` directories (external_scrap): name should be `{name}`
- `description` must be present and non-empty
- If `name` or `description` is missing, add them based on the file content

### 3. Fix `.kr` Files Too

If a `SKILL.kr` counterpart exists in the same directory, apply the same YAML fixes.
The `.kr` YAML frontmatter must be identical to the `.md` version.

### 4. Preserve Body Content

Do NOT modify anything below the closing `---` of the YAML frontmatter.
Only the YAML header section between the two `---` delimiters should be changed.

---

## Execution Steps

1. Glob all `SKILL.md` files
2. For each file:
   a. Read the file content
   b. Parse the YAML frontmatter
   c. Check for non-standard fields
   d. If changes needed: use Edit tool to replace the old YAML with the corrected version
   e. Check for corresponding `SKILL.kr` file
   f. If `.kr` exists and needs fixing: apply same YAML fix
3. Track all changes made

---

## Output Format

Save results to `output/skill-format-fix-report.md`. Format:

```markdown
# Skill Format Fix Report

> Generated: YYYY-MM-DD

## Summary

| Category | Count |
|----------|-------|
| Total .md skill files processed | N |
| Total .kr skill files processed | N |
| Total files modified | N |
| Files skipped (already correct) | N |
| Files with non-standard fields removed | N |

---

## Changes by Project

### Root (.claude/skills/)

| Skill | Changes | Fields Removed |
|-------|---------|----------------|

### {project} (.claude/skills/)

| Skill | Changes | Fields Removed |
|-------|---------|----------------|

---

## Verification

- Zero files with non-standard YAML fields remaining
- All .kr counterparts updated identically to .md versions
- Body content preserved unchanged
```
