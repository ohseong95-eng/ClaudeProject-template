---
name: guard-rollback-temp-backup
description: Restore original files from backup when an operation fails. Use when maximum retries are exceeded and rollback is needed.
---

# Rollback from Temporary Backup

When a propagation agent exceeds the maximum retry count and ultimately fails,
this skill reads the backup manifest and restores all files to their pre-operation state.

## Rollback Procedure

### 1. Read the Manifest

```
{project}/.claude/_temp_backup/{TIMESTAMP}/_manifest.md
```

Identify the original path <-> backup path mapping from the manifest.

### 2. Clean Up Current State

Delete files created during the operation (renamed files).

- Delete new files created during the operation that are not in the manifest
- Delete renamed files (the new names)

### 3. Restore Backed Up Files

Copy files from the backup directory back to their original paths.

```
Backup:   {project}/.claude/_temp_backup/{TIMESTAMP}/skills/old-name/SKILL.md
Restored: {project}/.claude/skills/old-name/SKILL.md
```

- Preserve directory structure during restoration
- Also restore reference files such as CLAUDE.md, etc.

### 4. Verify Restoration

- Confirm the number of restored files matches the manifest
- Confirm file sizes match the backup copies
- Confirm no residual files from the operation remain

### 5. Clean Up Backup Directory

Delete the backup directory after the rollback is complete.

## Return Value

```markdown
## Rollback Result

- Status: success | partial | failed
- Rolled back at: YYYY-MM-DD HH:MM:SS
- Restored files: N
- Deleted operation files: N

### Restoration Details

| # | Original Path | Restore Status |
|---|---------------|----------------|
| 1 | ... | Success / Failed |

### Errors (if any)

| # | File | Error Details |
|---|------|---------------|
```

## Rollback Status Definitions

| Status | Description |
|--------|-------------|
| `success` | All files restored successfully |
| `partial` | Only some files restored -- manual review required |
| `failed` | Rollback itself failed -- manual recovery required, backup directory preserved |

## Constraints

- Rollback can only be executed when a manifest exists
- On `partial` or `failed` status, do not delete the backup directory (preserved for manual recovery)
- Request user confirmation before executing the rollback
- Rollback is irreversible -- execute with caution
