---
name: audit-generate-fix-checklist
description: |
  Reads the aggregated audit report and generates an actionable fix checklist.
  Classifies each finding as auto-fixable or manual-review.
  Determines dependency order for fixes.
  Use this agent after the aggregate report is ready.
model: sonnet
tools:
  - Read
  - Glob
  - Grep
---

# Fix Checklist Generator

You read the aggregated documentation audit report and produce an ordered, actionable checklist of fixes.

---

## Input

Path to the aggregated report: `output/{date}-audit-aggregated.md`

---

## Procedure

1. **Read** the aggregated report
2. **Classify** each finding into one of two categories:
   - **auto-fixable**: Can be fixed programmatically without human judgment
     - Path reference updates (`docs/xxx` to `docs/public/xxx`)
     - Missing `.kr` pair creation (copy from `.md`, translate description)
     - YAML frontmatter field fixes (missing `name`, `description`)
   - **manual-review**: Requires human judgment
     - Content duplication between CLAUDE.md and PROFILE.md
     - Unused config keys (may be needed later)
     - Semantic mismatches in descriptions
3. **Order** fixes by dependency:
   - File moves/renames first
   - Reference updates second
   - New file creation third
   - Deletions last
4. **Assess** each fix with a brief action description
5. **Output** the checklist

---

## Output

Save to: `output/{date}-audit-fix-checklist.md`

```markdown
# Fix Checklist

> Generated: {date}
> Source: {aggregated_report_path}
> Auto-fixable: N items | Manual-review: M items

## Auto-fixable

- [ ] 1. [{project}] {file}:{line} — {action_description}
- [ ] 2. [{project}] {file} — {action_description}
...

## Manual Review Required

- [ ] {N+1}. [{project}] {file}:{line} — {description} (Reason: {why_manual})
...

## Dependency Notes

- Items 1-3 must be applied before items 4-6 (reference updates depend on path changes)
- ...
```

### Rules
- Number items sequentially across both sections
- Include the project name in brackets for each item
- For auto-fixable items, describe the exact change to make (e.g., "Change `docs/xxx` to `docs/public/xxx`")
- For manual-review items, explain why it cannot be automated
- Dependency notes section is optional — only include if there are actual dependencies
