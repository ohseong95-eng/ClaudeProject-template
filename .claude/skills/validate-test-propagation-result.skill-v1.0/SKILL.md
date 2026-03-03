---
name: validate-test-propagation-result
description: Validate results after propagation operations such as file renames or reference updates. Use after propagation to verify correctness before cleanup.
---

# Validate Propagation Result

After a propagation agent completes its work, this skill verifies the changes from multiple angles.
On test failure, it returns failure details to the agent for retry decision-making.

## Validation Checks

### 1. File Existence Verification

Confirm that all "after" filenames in the change plan actually exist.

```
[ ] Does the changed file exist under its new name?
[ ] Has the old-name file been deleted (moved)?
[ ] Are there any missing files?
```

### 2. Naming Convention Compliance

Confirm that changed filenames follow the naming convention.

```
[ ] Skill: Is the directory name at least 3 words ({category}-{action}-{target})?
[ ] Skill: Does the directory contain SKILL.md?
[ ] Agent: Does the file follow {role}-{target}-{action}.agent-v{M}.{m}.md?
```

### 3. Reference Integrity Verification

Confirm that changed filenames are correctly referenced in related documents.

```
[ ] Is the new path reflected in the CLAUDE.md directory section?
[ ] Do agent files reference the new skill path in their "Used Skills" section?
[ ] Are there no documents still referencing the old filename? (grep check)
```

### 4. File Content Integrity Verification

Confirm that file contents have not been corrupted.

```
[ ] Is the changed file's size non-zero?
[ ] Does SKILL.md contain valid YAML frontmatter (name, description)?
[ ] Do self-references within the file match the new name?
```

## Validation Procedure

### Step 1: Receive Change Plan

Receive the change plan (before → after mapping) from the agent.

### Step 2: Execute Validation

Run the 4 validation checks above in order.

### Step 3: Determine Result

- **All checks pass** → return `PASS`
- **Any check fails** → return `FAIL` + failure details

## Return Value

```markdown
## Validation Result

- Status: PASS | FAIL
- Validated at: YYYY-MM-DD HH:MM:SS
- Total checks: N
- Passed: N
- Failed: N

### Failed Items (if FAIL)

| # | Check Item | Expected | Actual | Severity |
|---|------------|----------|--------|----------|
| 1 | ... | ... | ... | Critical / Warning |

### Recommended Actions

(Remediation steps for each failed item)
```

## Severity Classification

| Severity | Description | Retriable |
|----------|-------------|-----------|
| Critical | Missing file, broken reference | Yes (rework required) |
| Warning | Best practice not followed (minor) | Yes (optional) |

## Constraints

- Validation is read-only -- it does not modify any files
- A validation failure does not necessarily mean a rollback (the agent decides whether to retry)
- When performing grep checks, limit the search scope to within the target project
