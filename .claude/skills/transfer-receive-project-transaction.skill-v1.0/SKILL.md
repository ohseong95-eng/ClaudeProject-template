---
name: transfer-receive-project-transaction
description: Receive and process data from another project via project_transactions/. Use when picking up deliveries from other projects.
---

# Cross-Project Transaction Receive

Protocol that agents follow when retrieving and processing data delivered from another project.

## Receive Procedure

### 1. Identify the Recipient Project

Determine which project is currently active.

### 2. Query Pending Transactions

Search `project_transactions/` for files where **this project is the recipient** and the status is `pending`.

- Filename pattern: `*→{current project}-*`
- Optional filter by sender: `{sender project}→{current project}-*`

### 3. Review Transaction Contents

Read the full contents of the target file and identify the payload and expected action.

### 4. Acknowledge Receipt

1. Change `| Status | pending |` to `| Status | received |` in the file
2. Append the received timestamp to the file

### 5. Mark as Completed

Once processing is finished, change `| Status | received |` to `| Status | completed |`.

## Status Values

| Status | Meaning |
|--------|---------|
| `pending` | Sent but not yet processed by recipient |
| `received` | Recipient has acknowledged the transaction |
| `completed` | Recipient has finished processing |

## Rules

- The recipient project must not modify the **Payload** section of the original file
- Only status changes are permitted
