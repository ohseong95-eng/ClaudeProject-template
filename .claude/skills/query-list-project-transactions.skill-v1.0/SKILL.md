---
name: query-list-project-transactions
description: List and review cross-project transaction status. Use when checking pending, received, or completed transactions.
---

# List Transactions

Rules that agents follow when reviewing the status of cross-project transactions.

## Lookup Procedure

### 1. Collect Transaction Files

Gather all `.md` files in the `project_transactions/` folder. (Exclude `.gitkeep`)

### 2. Extract Metadata

Read the sender, recipient, SESSION_ID, and status from the table inside each file.

### 3. Filter

Filter by status (`pending`, `received`, `completed`, `all`) as needed.

## Output Format

```markdown
## project_transactions/ Overview

| # | Sender → Recipient | SESSION_ID | Content | Status | Created At |
|---|---------------------|-----------|---------|--------|------------|
| 1 | ... → ... | ... | ... | ... | ... |

Total: N entries (pending: N, received: N, completed: N)
```

## Status Values

| Status | Meaning |
|--------|---------|
| `pending` | Sent but not yet processed by recipient |
| `received` | Recipient has acknowledged the transaction |
| `completed` | Recipient has finished processing |
