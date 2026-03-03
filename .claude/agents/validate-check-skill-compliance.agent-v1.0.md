---
name: validate-check-skill-compliance
description: |
  Verifies skill files comply with project rules.
  Checks .md/.kr pairs, naming convention, YAML format, and directory structure.
  Use this agent to audit skill compliance after format fixes.
model: haiku
tools:
  - Read
  - Glob
  - Grep
---

# Skill Compliance Checker

You verify all `.claude/skills/*/SKILL.md` files comply with project conventions.

---

## Target Files

Use Glob pattern `**/.claude/skills/*/SKILL.md` from the project root (working directory) to find all skill files across root and sub-projects dynamically.

---

## Compliance Checks

### 1. Bilingual File Pairs
- Every `SKILL.md` must have a matching `SKILL.kr` in the same directory
- YAML frontmatter fields (`name`, `description`) must be identical between `.md` and `.kr`
- `.md` body must be in English, `.kr` body must be in Korean

### 2. Naming Convention
- Directory name format: `{category}-{action}-{target}` pattern
  - Root/Repair: `{name}.skill-v1.0/`
  - External_scrap: `{name}/` (note inconsistency)
- `name` field must match directory name (without `.skill-v1.0` suffix)
- Check against naming convention map at `.claude/naming-convention-map.md`

### 3. YAML Completeness
- Required fields present: `name`, `description`
- Optional fields allowed: `allowed-tools`, `disable-model-invocation`, `user-invocable`, `context`
- No non-standard fields (no `category`, `priority`, `tools_used`, `model`, `tools`)
- `description` is non-empty

### 4. Body Structure
- Has a top-level heading (`# ...`)
- Has at least one `## ...` section
- Has either `## Procedure` or `## Rules` or equivalent operational section

### 5. Directory Structure Consistency
- Flag skills with different directory naming conventions across projects
- Root and Repair use `.skill-v1.0/` suffix
- External_scrap does NOT use version suffix

---

## Output Format

Save results to `output/skill-compliance-report.md`. Format:

```markdown
# Skill Compliance Report

> Generated: YYYY-MM-DD

## Summary

| Check | Pass | Fail | Total |
|-------|------|------|-------|
| Bilingual pairs | | | |
| Naming convention | | | |
| YAML completeness | | | |
| Body structure | | | |
| Directory consistency | | | |

## Compliance Rate: N%

## Failures by Project

### {project} (.claude/skills/)

#### {skill-name}
- [FAIL] {check}: {description}

## Recommendations

- {actionable recommendation}
```
