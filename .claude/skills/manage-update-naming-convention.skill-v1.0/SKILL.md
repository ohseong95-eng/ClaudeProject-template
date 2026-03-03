---
name: manage-update-naming-convention
description: Add, update, or remove vocabulary entries in the naming convention map. Use when a sub-project requests a new category, action, or target term via project_transactions/.
---

# Update Naming Convention Map

This skill governs all modifications to `.claude/naming-convention-map.md`.
Only the `manage-control-naming-convention` agent may invoke this skill.
Sub-projects and other agents must NOT modify the map directly.

## Authorized Operations

| Operation | Description |
|-----------|-------------|
| `ADD_TERM` | Add a new category, action, or target to the map |
| `UPDATE_TERM` | Modify an existing term's description or usage |
| `REGISTER_SKILL` | Add a new skill entry to the Full Skill Registry |
| `DEREGISTER_SKILL` | Remove a skill entry from the registry |
| `UPDATE_VERSION` | Update a skill's version in the registry |

## Procedure

### 1. Receive Request

Accept a change request from one of these sources:
- `project_transactions/` — sub-project request file (pattern: `*→root-*-naming-request*`)
- Direct user instruction in a root session
- Agent self-detection during skill creation/rename

### 2. Validate Request

Before applying changes:

```
[ ] Is the requester authorized? (sub-project via transaction OR user OR naming-convention agent)
[ ] Does the new term conflict with an existing term?
[ ] Does the new term follow the format? (lowercase, hyphens only, descriptive)
[ ] Is the category/action/target placement correct?
```

- If a conflict is found, reject with reason and suggest the existing term instead
- If the term is ambiguous, ask the user for clarification

### 3. Apply Changes

Edit `.claude/naming-convention-map.md`:

- **ADD_TERM**: Insert into the appropriate table (Category / Action / Target), maintaining alphabetical order
- **REGISTER_SKILL**: Add row to the appropriate project section in Full Skill Registry
- **DEREGISTER_SKILL**: Remove the row from the registry
- **UPDATE_TERM / UPDATE_VERSION**: Modify the existing entry in place

### 4. Verify

After modification:

```
[ ] No duplicate entries in any table
[ ] Alphabetical order maintained (within each table)
[ ] Registry entry matches actual skill directory name
[ ] All table formatting is intact (markdown table alignment)
```

### 5. Respond

Return the result to the requester:

```markdown
## Naming Convention Update Result

- Operation: ADD_TERM / UPDATE_TERM / REGISTER_SKILL / DEREGISTER_SKILL / UPDATE_VERSION
- Status: approved | rejected | needs-clarification
- Updated at: YYYY-MM-DD HH:MM:SS

### Changes Applied

| # | Table | Term | Action |
|---|-------|------|--------|
| 1 | ... | ... | Added / Updated / Removed |

### Rejection Reason (if rejected)

(Why the request was rejected and what to use instead)
```

If the request came via `project_transactions/`, update the transaction status to `completed`.

## Constraints

- This skill may ONLY be invoked by the `manage-control-naming-convention` agent
- Never remove a term that is referenced by an existing skill directory
- Before deregistering a skill, verify it has been deleted or renamed
- Keep the map file under 300 lines — archive old entries if needed
