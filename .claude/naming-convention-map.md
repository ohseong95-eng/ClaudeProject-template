# Naming Convention Map

> Standardized vocabulary for skill/agent naming across all projects.
> Same function must always use the same category, action, and target terms.
> New skill/agent creation must reference this map for consistency.

---

## File Name Format

### Skill
```
{category}-{action}-{target}.skill-v{Major}.{Minor}/SKILL.md
```

### Agent
```
{category}-{action}-{target}.agent-v{Major}.{Minor}.md
```

- YAML frontmatter `name` field: `{category}-{action}-{target}` (no version, no dots)
- Skill: directory name includes `.skill-v{M}.{m}` suffix
- Agent: file name includes `.agent-v{M}.{m}` suffix

---

## Category (분류)

| Code | Description | Use Case |
|------|-------------|----------|
| `guard` | Protection / safety | Backup, rollback, safety checks |
| `query` | Lookup / search | Status checks, listing, searching |
| `transfer` | Send / receive | Cross-project data exchange |
| `catalog` | Catalog management | Sync, consolidate, inventory |
| `validate` | Verification | Result checks, integrity tests |
| `fetch` | Retrieval | Web page / URL data fetching |
| `extract` | Extraction | Text, image, structured data parsing |
| `transform` | Conversion | Format conversion, cleansing, summarization |
| `store` | Storage | File / data persistence |
| `control` | Control / limiting | Rate limiting, scope limiting, history tracking |
| `manage` | Management / administration | Naming conventions, configuration, governance |
| `orchestrate` | Coordination / dispatch | Cross-project pipelines, task dispatch |
| `classify` | Classification / analysis | Bug classification, pattern analysis |
| `repair` | Code repair / fix | Bug fixes, code patches |
| `generate` | Creation / generation | Agent/file creation from templates |
| `propagate` | Propagation / spreading | Structure/convention propagation to sub-projects |
| `scan` | Scanning / discovery | Source code scanning, endpoint discovery |
| `report` | Reporting / output | Report generation, result summary |
| `execute` | Execution / running | Test execution, API calls |
| `analyze` | Deep analysis | Scope analysis, impact analysis |
| `collect` | Collection / gathering | Web crawling, source research, page scraping |
| `audit` | Documentation review | Consistency checks, doc quality, cross-reference validation |

---

## Action (동작)

| Action | Description | Example |
|--------|-------------|---------|
| `check` | Verify status or condition | `query-check-project-status` |
| `list` | Enumerate items | `query-list-project-transactions` |
| `send` | Transmit data | `transfer-send-project-transaction` |
| `receive` | Accept data | `transfer-receive-project-transaction` |
| `sync` | Synchronize | — |
| `create` | Generate new item | `guard-create-temp-backup` |
| `rollback` | Restore previous state | `guard-rollback-temp-backup` |
| `test` | Run validation tests | `validate-test-propagation-result` |
| `retrieve` | Fetch single item | `fetch-retrieve-single-page` |
| `search` | Find via query | `fetch-search-web-results` |
| `parse` | Analyze structure | `extract-parse-text-body` |
| `collect` | Gather multiple items | `extract-collect-image` |
| `download` | Fetch binary file | `extract-download-document` |
| `convert` | Change format | `transform-convert-html-markdown` |
| `cleanse` | Clean / normalize | `transform-cleanse-data` |
| `generate` | Produce output | `transform-generate-summary` |
| `save` | Write to storage | `store-save-markdown-report` |
| `export` | Output in format | `store-export-json-csv` |
| `limit` | Restrict scope/rate | `control-limit-request-rate` |
| `track` | Record history | `control-track-crawl-history` |
| `handle` | Process events | `control-handle-error-retry` |
| `update` | Modify existing entry | `manage-update-naming-convention` |
| `read` | Load and return content | `extract-read-classification-bugs` |
| `generate` | Create new item from rules | `control-generate-session-id` |
| `match` | Find best-fit item | `query-match-capability-agent` |
| `coordinate` | Orchestrate across projects | `orchestrate-coordinate-cross-project` |
| `dispatch` | Assign and route tasks | `orchestrate-dispatch-repair-task` |
| `analyze` | Deep examination | `classify-analyze-bug-dimension` |
| `deploy` | Apply to target location | `propagate-deploy-directory-structure` |
| `enforce` | Apply rules strictly | `propagate-enforce-naming-convention` |
| `control` | Manage and govern | `manage-control-naming-convention` |
| `add` | Insert new element | `repair-add-null-guard` |
| `implement` | Build missing feature | `repair-implement-missing-function` |
| `fix` | Correct existing error | `repair-fix-unpack-count` |
| `set` | Configure value | `repair-set-config-value` |
| `relax` | Loosen restriction | `repair-relax-validation` |
| `detect` | Identify errors/issues | `validate-detect-agent-error` |
| `discover` | Find unknown items | `scan-discover-endpoints` |
| `scrape` | Extract from web pages | `collect-scrape-page-content` |
| `crawl` | Navigate through pages | `collect-crawl-site-pages` |
| `research` | Search and compile sources | `collect-research-topic-sources` |
| `process` | Transform collected data | `transform-process-collected-content` |
| `trace` | Follow execution path | `extract-trace-call-chain` |
| `build` | Construct output artifact | `generate-build-catalog` |
| `run` | Execute test or process | `execute-run-api-test` |
| `retest` | Re-run previous test | `execute-retest-fixed-bugs` |
| `identify` | Determine scope/impact | `analyze-identify-repair-scope` |
| `compose` | Assemble pipeline/plan | `orchestrate-compose-execution-pipeline` |
| `aggregate` | Merge distributed findings into one | `audit-aggregate-doc-report` |
| `apply` | Apply approved changes | `audit-apply-doc-fixes` |

---

## Target (대상) — Standardized Terms

| Target | Description | Used In |
|--------|-------------|---------|
| `project-status` | Project registry status | `query-check-project-status` |
| `project-transaction` | Cross-project data exchange | `transfer-send-project-transaction` |
| `project-transactions` | Transaction list (plural) | `query-list-project-transactions` |
| `project-specs` | Project specification documents | — |
| `temp-backup` | Temporary backup files | `guard-create-temp-backup` |
| `propagation-result` | Propagation operation results | `validate-test-propagation-result` |
| `single-page` | Single web page | `fetch-retrieve-single-page` |
| `multi-page` | Multiple web pages | `fetch-retrieve-multi-page` |
| `web-results` | Search engine results | `fetch-search-web-results` |
| `text-body` | Main text content | `extract-parse-text-body` |
| `image` | Image files | `extract-collect-image` |
| `document` | Document files (PDF etc.) | `extract-download-document` |
| `structured-data` | Tables, JSON, structured | `extract-parse-structured-data` |
| `metadata` | Meta tags, headers | `extract-parse-metadata` |
| `html-markdown` | HTML to Markdown conversion | `transform-convert-html-markdown` |
| `data` | Generic data | `transform-cleanse-data` |
| `summary` | Text summary | `transform-generate-summary` |
| `markdown-report` | Markdown report file | `store-save-markdown-report` |
| `json-csv` | JSON/CSV export | `store-export-json-csv` |
| `binary-file` | Binary files | `store-save-binary-file` |
| `request-rate` | HTTP request rate | `control-limit-request-rate` |
| `crawl-scope` | Crawl boundary | `control-limit-crawl-scope` |
| `error-retry` | Error handling / retry | `control-handle-error-retry` |
| `crawl-history` | Crawl visit history | `control-track-crawl-history` |
| `naming-convention` | Naming convention rules/map | `manage-update-naming-convention` |
| `classification-bugs` | Bug classification JSON entries | `extract-read-classification-bugs` |
| `target-file` | Source code file from fix_hints | `extract-read-target-file` |
| `repair-result` | Repair outcome report | `store-save-repair-result` |
| `session-id` | SESSION_ID token | `control-generate-session-id`, `validate-check-session-id` |
| `capability-agent` | Capability-based agent match | `query-match-capability-agent` |
| `session-record` | Session log file | `store-save-session-record` |
| `cross-project` | Cross-project coordination scope | `orchestrate-coordinate-cross-project` |
| `directory-structure` | Project directory layout | `propagate-deploy-directory-structure` |
| `project-inventory` | Project component inventory | — |
| `repair-task` | Bug repair task assignment | `orchestrate-dispatch-repair-task` |
| `bug-dimension` | Multi-dimensional bug classification | `classify-analyze-bug-dimension` |
| `repair-agent` | Repair agent file | `generate-create-repair-agent` |
| `null-guard` | None/null value check guard | `repair-add-null-guard` |
| `exception-handler` | Try/except exception handler | `repair-add-exception-handler` |
| `missing-function` | Unimplemented function | `repair-implement-missing-function` |
| `unpack-count` | Unpack variable count mismatch | `repair-fix-unpack-count` |
| `config-value` | Configuration setting value | `repair-set-config-value` |
| `oauth-refresh` | OAuth token refresh | `repair-implement-oauth-refresh` |
| `request-format` | HTTP request format support | `repair-add-request-format` |
| `validation` | Input validation rules | `repair-relax-validation` |
| `typo` | Code typo | `repair-fix-typo` |
| `agent-error` | Agent file format/content errors | `validate-detect-agent-error` |
| `agent-format` | Agent YAML frontmatter format | `audit-fix-agent-format` |
| `agent-compliance` | Agent standards compliance | `validate-check-agent-compliance` |
| `skill-error` | Skill file format/content errors | `validate-detect-skill-error` |
| `skill-format` | Skill YAML frontmatter format | `audit-fix-skill-format` |
| `skill-compliance` | Skill standards compliance | `validate-check-skill-compliance` |
| `endpoints` | API route/endpoint definitions | `scan-discover-endpoints` |
| `services` | Service/internal functions | `scan-discover-services` |
| `parameters` | Request parameters/schema | `extract-analyze-parameters` |
| `auth` | Authentication mechanisms | `extract-analyze-auth` |
| `call-chain` | Function call relationships | `extract-trace-call-chain` |
| `models` | Data models/DTOs/schemas | `extract-analyze-models` |
| `catalog` | API catalog artifact | `generate-build-catalog` |
| `testcases` | Test case scenarios | `generate-build-testcases` |
| `api-test` | API HTTP test execution | `execute-run-api-test` |
| `response` | HTTP response validation | `validate-check-response` |
| `bug-detection` | Bug detection report | `report-generate-bug-detection` |
| `repair-scope` | Repair impact scope | `analyze-identify-repair-scope` |
| `fixed-bugs` | Previously fixed bugs retest | `execute-retest-fixed-bugs` |
| `regression-test` | Regression test execution | `execute-run-regression-test` |
| `verification` | Verification report | `report-generate-verification` |
| `page-content` | Web page content | `collect-scrape-page-content` |
| `site-pages` | Multi-page site crawl | `collect-crawl-site-pages` |
| `topic-sources` | Topic research sources | `collect-research-topic-sources` |
| `page-assets` | Page images/files | `extract-download-page-assets` |
| `collected-content` | Previously collected content | `transform-process-collected-content` |
| `scraping-task` | Web scraping task dispatch | `orchestrate-dispatch-scraping-task` |
| `execution-pipeline` | Composed execution pipeline | `orchestrate-compose-execution-pipeline` |
| `doc-inconsistency` | Documentation inconsistency findings | `audit-detect-doc-inconsistency` |
| `doc-report` | Aggregated documentation audit report | `audit-aggregate-doc-report` |
| `fix-checklist` | Actionable fix checklist | `audit-generate-fix-checklist` |
| `doc-fixes` | Documentation fix operations | `audit-apply-doc-fixes` |
| `common-skill` | Common functionality extracted as shared skill | `audit-generate-common-skill` |
| `pipeline-summary` | Pipeline execution summary report | `report-generate-pipeline-summary` |

---

## Rules

1. **New skill/agent**: Look up this map first. If the same category+action+target exists, use the identical name.
2. **New vocabulary**: If a new term is needed, add it to the appropriate table in this file.
3. **Cross-project reuse**: If two projects use the same skill name, escalate to root `.claude/skills/`. If the same agent capability is needed, escalate to root `.claude/agents/`.
4. **Version suffix**: Skill: `.skill-v{M}.{m}` on directory name. Agent: `.agent-v{M}.{m}` on file name. The YAML `name` field uses the base name only (lowercase, hyphens, no dots).
5. **Read-only for sub-projects**: This file is a shared root resource. Sub-projects may read but must NOT modify it. If a sub-project needs a new term, it must request the addition via `project_transactions/` to the root. The root session reviews and updates this file.
6. **Agent naming**: Agents follow the same `{category}-{action}-{target}` pattern as skills. The category should describe the agent's primary role (e.g., `repair`, `orchestrate`, `classify`).
