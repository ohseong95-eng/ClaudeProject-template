# 파일 명명 규칙

> CLAUDE.md에서 분리된 참조 문서. 파일·디렉토리 생성 시 참조한다.

---

## 기본 형식

```
{분류}-{동작}-{대상}.{유형}-v{Major}.{Minor}.md
```

- **최소 3단어** 이상으로 파일의 역할을 명확히 기술한다
- **유형 접미사**를 포함하여 파일명만으로 종류를 식별한다
- **시맨틱 버전**을 사용한다 (v{Major}.{Minor})

---

## 버전 규칙

| 변경 | Major 올림 | Minor 올림 |
|------|-----------|-----------|
| 입출력 형식 변경 | O | |
| 절차 구조 변경 | O | |
| 내용 보강·수정 | | O |
| 오타·표현 수정 | | O |

- 신규 생성 시 `v1.0`으로 시작한다
- 버전 변경 시 파일명의 버전 번호를 직접 수정한다
- **단일 버전 정책**: 같은 skill/agent는 항상 하나의 버전만 유지한다. 버전 업그레이드 시 기존 디렉토리/파일을 새 버전으로 교체한다 (두 버전 공존 금지)

---

## 유형별 명명 규칙

### Skill 디렉토리 — `.claude/skills/{name}.skill-v{M}.{m}/SKILL.md`

```
디렉토리명: {분류}-{동작}-{대상}.skill-v{Major}.{Minor}
진입점:     SKILL.md (YAML frontmatter 필수)
```

| 디렉토리명 예시 | 설명 |
|----------------|------|
| `guard-add-null-check.skill-v1.0/SKILL.md` | None 체크 가드 추가 |
| `handler-add-exception-catch.skill-v1.0/SKILL.md` | 예외 처리 추가 |
| `extract-parse-test-output.skill-v1.0/SKILL.md` | 테스트 결과 파싱 |
| `classify-bug-five-dimension.skill-v1.0/SKILL.md` | 5차원 버그 분류 |

> 디렉토리명에 `.skill-v{M}.{m}` 버전 접미사를 포함한다.
> YAML frontmatter `name`에는 base name만 기재한다 (소문자, 하이픈만 허용, 점/버전 불가).
> 표준 어휘는 `.claude/naming-convention-map.md`를 참조한다.

### Agent 파일 — `.claude/agents/`

```
{분류}-{동작}-{대상}.agent-v{M}.{m}.md
```

Skill과 동일한 `{category}-{action}-{target}` 패턴을 따른다.

| 예시 | 분류 | 동작 | 대상 |
|------|------|------|------|
| `orchestrate-coordinate-cross-project.agent-v1.0.md` | orchestrate | coordinate | cross-project |
| `classify-analyze-bug-dimension.agent-v1.0.md` | classify | analyze | bug-dimension |
| `repair-add-null-guard.agent-v1.0.md` | repair | add | null-guard |
| `generate-create-repair-agent.agent-v1.0.md` | generate | create | repair-agent |
| `propagate-enforce-naming-convention.agent-v1.0.md` | propagate | enforce | naming-convention |

> Agent 파일명에도 `.agent-v{M}.{m}` 버전 접미사를 포함한다.
> YAML frontmatter `name`에는 base name만 기재한다 (소문자, 하이픈만 허용, 점/버전 불가).
> 표준 어휘는 `.claude/naming-convention-map.md`를 참조한다.

### Workitem 파일 — `workitems/`

```
YYYY-MM-DD-{동작}-{대상}-{상세}.workitem.md
```

| 예시 | 설명 |
|------|------|
| `2026-02-20-add-oauth-refresh-impl.workitem.md` | OAuth refresh 구현 계획 |
| `2026-02-20-fix-unpack-count-sanity.workitem.md` | unpack 불일치 수정 |
| `2026-02-20-refactor-skill-extraction.workitem.md` | skill 분리 리팩토링 |

> workitem은 날짜가 버전 역할을 하므로 별도 버전 번호를 붙이지 않는다.

### Output 파일 — `output/`

```
YYYY-MM-DD-{주제}.md
```

> 보고서는 버전이 아닌 날짜로 관리한다.

### Transaction 파일 — `transactions/`

```
{SESSION_ID}-{역할}-{상세}.{ext}
```

> SESSION_ID가 버전 역할을 한다.

### Session 파일 — `sessions/`

```
YYYY-MM-DD-HHMMSS.md
```

---

## Skill 디렉토리명 규칙

- Skill 디렉토리명은 `{분류}-{동작}-{대상}.skill-v{M}.{m}` 형식을 따른다 (최소 3단어 + 버전)
- 신규 생성 시 `.claude/naming-convention-map.md`에서 표준 어휘를 확인한다
- 같은 기능은 프로젝트가 달라도 동일한 분류/동작/대상을 사용한다
- 디렉토리명 변경 시 해당 skill을 참조하는 에이전트 프롬프트도 함께 갱신한다
- Claude Code가 자동 탐색하므로 별도 CATALOG.md 동기화는 불필요하다

---

## 커맨드 명명 규칙

> `docs/command-naming-convention.md` 참조
