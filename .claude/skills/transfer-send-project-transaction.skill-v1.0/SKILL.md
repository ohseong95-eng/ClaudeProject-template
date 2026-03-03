---
name: transfer-send-project-transaction
description: Send data to another project via project_transactions/. Use when delivering results or reports between projects.
---

# Cross-Project Transaction Send

Protocol that agents follow when delivering data to another project.

## Send Procedure

### 1. Identify the Sender Project

Determine which project is currently active.
- When running from root, the sender is `root`

### 2. Determine SESSION_ID

Count today's date (YYYYMMDD) files in `project_transactions/` and add 1 for the sequence number.

```
SESSION_ID = YYYYMMDD-{4-digit sequence}
```

### 3. Verify Recipient Project Status

Use the `project-registry` skill to check the recipient project's status.
- Do **not** send to **Disabled** projects

### 4. Create File

**Filename:**
```
project_transactions/{sender project}→{recipient project}-{SESSION_ID}-<content summary>.md
```

**File contents:**
```markdown
# Project Transaction

| Field | Value |
|-------|-------|
| Sender | {sender project} |
| Recipient | {recipient project} |
| SESSION_ID | {SESSION_ID} |
| Created At | YYYY-MM-DD HH:MM:SS |
| Status | pending |

## Payload

(Data to deliver)

## Expected Action

(Processing expected from the recipient project)
```

## Rules

- Report the file path after the send is complete
- The recipient project must not modify the original file (read-only)
