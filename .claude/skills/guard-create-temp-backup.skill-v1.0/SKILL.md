---
name: guard-create-temp-backup
description: Create temporary backups of target files before destructive operations. Use before rename, edit, or delete operations to enable rollback on failure.
---

# Create Temporary Backup

Before an agent modifies files, this skill copies the originals to a temporary directory so they can be restored using the `guard-rollback-temp-backup` skill if the operation fails.

## Backup Procedure

### 1. Create Backup Directory

```
{project root}/.claude/_temp_backup/{TIMESTAMP}/
```

- TIMESTAMP format: `YYYYMMDD-HHMMSS`
- If the directory already exists, create a new one instead of reusing it (second-level precision prevents collisions)

### 2. Copy Target Files

Copy all files scheduled for modification to the backup directory.

```
Original: {project}/.claude/skills/old-name/SKILL.md
Backup:   {project}/.claude/_temp_backup/{TIMESTAMP}/skills/old-name/SKILL.md
```

- Preserve the directory structure during copy (maintain relative paths)
- Also back up any reference files that will change (CLAUDE.md, etc.)

### 3. Generate Manifest File

Create `_manifest.md` in the backup directory:

```markdown
# Backup Manifest

- Created at: YYYY-MM-DD HH:MM:SS
- Agent: {calling agent name}
- Project: {target project name}
- Operation type: {rename/edit/delete etc.}

## Backed Up Files

| # | Original Path | Backup Path | Size |
|---|---------------|-------------|------|
| 1 | ... | ... | ... |

## Recovery Instructions

To restore this backup, use the `guard-rollback-temp-backup` skill.
Backup path: {full backup directory path}
```

### 4. Verify Backup

- Confirm the number of copied files matches the manifest
- Confirm file sizes match the originals
- If verification fails, return a warning to the agent (recommend aborting the operation)

## Backup Cleanup Rules

- Delete the backup directory after the operation succeeds and tests pass
- Delete the backup directory after a rollback as well
- Warn if any backups under `_temp_backup/` are older than config.md's `backup_ttl_hours`

## Return Value

Return the following information to the agent:

```
backup_path: {full backup directory path}
manifest_path: {manifest file path}
file_count: {number of backed up files}
status: success | failed
error: {error message on failure}
```

## Constraints

- `_temp_backup/` must only be created under `.claude/`
- Use the `cp` command for binary files
- Do not proceed with the main operation if the backup fails
