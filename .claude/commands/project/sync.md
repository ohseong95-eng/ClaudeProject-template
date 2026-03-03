에이전트/스킬 변경 후 관련 문서를 일괄 동기화한다.

## 동기화 대상

1. **`.claude/naming-convention-map.md`** — 명명 규칙 어휘 (Category/Action/Target)
2. **각 프로젝트 `docs/component-audit-status.md`** — 컴포넌트 감사 현황 표

## 실행 절차

### Step 1 — 현재 상태 스캔

1. `docs/project-registry.md`에서 활성 프로젝트 목록을 읽는다
2. 각 활성 프로젝트의 `.claude/agents/*.agent-v1.0.md` 파일을 Glob으로 수집한다
3. 각 활성 프로젝트의 `.claude/skills/*/SKILL.md` 파일을 Glob으로 수집한다
4. 각 에이전트/스킬 파일의 YAML frontmatter(name, description, model, tools)를 읽는다

### Step 2 — naming-convention-map.md 갱신

1. `.claude/naming-convention-map.md`를 읽는다
2. 스캔된 모든 에이전트/스킬 이름에서 Category, Action, Target을 추출한다
3. map에 등록되지 않은 신규 어휘를 식별한다
4. 신규 어휘가 있으면 해당 표에 추가한다
5. 없으면 "이미 최신 상태"로 보고한다

### Step 3 — component-audit-status.md 갱신

1. 각 활성 프로젝트의 `docs/component-audit-status.md`를 읽는다
2. 스캔 결과와 비교하여 누락된 에이전트/스킬 행을 추가한다
3. 삭제된 에이전트/스킬 행을 제거한다

### Step 4 — 결과 보고

```
## 동기화 결과

| 문서 | 상태 | 변경 내용 |
|------|------|----------|
| naming-convention-map.md | 갱신됨/최신 | 신규 어휘 N개 |
| {프로젝트}/docs/component-audit-status.md | 갱신됨/최신 | +N 행 |
```
