# Component Audit Status — Root (ClaudeProjects)

> Last updated: -
> Audit scope: Agent YAML format, Skill YAML format, bilingual pairs, compliance

---

## Agents (.claude/agents/)

| # | Agent | Model | tools | YAML Format | .kr Pair | Status |
|---|-------|-------|-------------|-------------|----------|--------|
| 1 | `manage-control-naming-convention` | haiku | Read, Edit, Write, Glob, Grep | OK | OK | Done |
| 2 | `propagate-deploy-directory-structure` | haiku | Read, Edit, Write, Glob, Grep | OK | OK | Done |
| 3 | `propagate-enforce-naming-convention` | haiku | Read, Edit, Write, Glob, Grep | OK | OK | Done |
| 4 | `validate-detect-agent-error` | haiku | Read, Glob, Grep | OK | OK | Done |
| 5 | `audit-fix-agent-format` | sonnet | Read, Edit, Glob, Grep | OK | OK | Done |
| 6 | `validate-check-agent-compliance` | haiku | Read, Glob, Grep | OK | OK | Done |
| 7 | `validate-detect-skill-error` | haiku | Read, Glob, Grep | OK | OK | Done |
| 8 | `audit-fix-skill-format` | sonnet | Read, Edit, Glob, Grep | OK | OK | Done |
| 9 | `validate-check-skill-compliance` | haiku | Read, Glob, Grep | OK | OK | Done |
| 10 | `orchestrate-compose-execution-pipeline` | sonnet | Read, Glob, Grep | OK | OK | Done |
| 11 | `audit-detect-doc-inconsistency` | haiku | Read, Glob, Grep | OK | OK | Done |
| 12 | `audit-aggregate-doc-report` | haiku | Read, Glob, Grep | OK | OK | Done |
| 13 | `audit-generate-fix-checklist` | sonnet | Read, Glob, Grep | OK | OK | Done |
| 14 | `audit-apply-doc-fixes` | sonnet | Read, Edit, Write, Glob, Grep | OK | OK | Done |
| 15 | `audit-generate-common-skill` | sonnet | Read, Write, Glob, Grep | OK | OK | Done |

---

## Skills (.claude/skills/)

| # | Skill | YAML Format | .kr Pair | .kr YAML | Status |
|---|-------|-------------|----------|----------|--------|
| 1 | `guard-create-temp-backup` | OK | OK | OK | Done |
| 2 | `guard-rollback-temp-backup` | OK | OK | OK | Done |
| 3 | `validate-test-propagation-result` | OK | OK | OK | Done |
| 4 | `transfer-send-project-transaction` | OK | OK | OK | Done |
| 5 | `transfer-receive-project-transaction` | OK | OK | OK | Done |
| 6 | `query-list-project-transactions` | OK | OK | OK | Done |
| 7 | `query-check-project-status` | OK | OK | OK | Done |
| 8 | `manage-update-naming-convention` | OK | OK | OK | Done |

---

## Summary

| Category | Total | Audited | Fixed | Remaining |
|----------|-------|---------|-------|-----------|
| Agents | 15 | 15 | 15 | 0 |
| Skills | 8 | 8 | 8 | 0 |
