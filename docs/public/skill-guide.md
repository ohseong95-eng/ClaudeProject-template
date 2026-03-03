# Skills 구조 가이드

> CLAUDE.md에서 분리된 참조 문서. Skill 생성·수정 시 참조한다.

---

## Skills란

Skills는 Claude Code가 **자동 인식**하는 재사용 가능한 기능 모듈이다.
`/skill-name`으로 슬래시 커맨드처럼 호출하거나, Claude가 description을 보고 자동 호출한다.

### 핵심 구분

```
command  (.claude/commands/*.md)  — 단일 파일, 사용자가 /명령 으로 호출
skill    (.claude/skills/name/)   — 디렉토리 + SKILL.md, 자동 인식·자동/수동 호출
agent    (.claude/agents/*.md)    — Task tool로 서브프로세스 실행, 자율적 멀티스텝 작업
```

---

## 디렉토리 구조

각 skill은 **디렉토리**이며, 진입점은 반드시 `SKILL.md`이다.

```
.claude/skills/
├── query-check-project-status.skill-v1.0/
│   └── SKILL.md                # 필수 — YAML frontmatter + 지시사항
├── transfer-send-project-transaction.skill-v1.0/
│   └── SKILL.md
├── guard-create-temp-backup.skill-v1.0/
│   ├── SKILL.md                # 필수
│   └── reference.md            # 선택 — 보조 문서
└── {category}-{action}-{target}.skill-v{M}.{m}/
    ├── SKILL.md                # 필수
    ├── *.md                    # 선택 — 상세 문서, 예시
    ├── scripts/                # 선택 — 보조 스크립트
    └── templates/              # 선택 — 템플릿
```

---

## SKILL.md 필수 형식

모든 SKILL.md는 **YAML frontmatter**를 포함해야 한다:

```markdown
---
name: skill-name
description: When and why to use this skill (Claude가 자동 호출 판단에 사용)
---

Skill instructions here...
```

### 주요 frontmatter 필드

| 필드 | 필수 | 설명 |
|------|:---:|------|
| `name` | O | 소문자, 하이픈 구분 |
| `description` | O | 언제·왜 사용하는지 (자동 호출 판단 기준) |
| `disable-model-invocation` | - | `true`면 사용자만 `/name`으로 호출 가능 |
| `user-invocable` | - | `false`면 Claude만 호출 가능 (사용자 호출 불가) |
| `allowed-tools` | - | 이 skill 실행 시 사용 가능한 도구 제한 |
| `context` | - | `fork`면 격리된 서브에이전트에서 실행 |

---

## 인식·호출 방식

- **자동 인식**: `.claude/skills/` 하위 디렉토리의 SKILL.md를 Claude Code가 시작 시 탐색
- **수동 호출**: 사용자가 `/skill-name` 입력
- **자동 호출**: Claude가 description을 보고 요청에 맞는 skill을 자동 로드
- **CATALOG.md 불필요**: Claude Code가 자동 탐색하므로 별도 카탈로그 파일이 필요 없음

---

## Skill 작성 규칙

- SKILL.md는 **하나의 기능**에 집중한다 (단일 책임)
- YAML frontmatter의 `description`을 명확히 작성한다 (자동 호출 정확도에 영향)
- 입력·출력·처리 규칙을 명확히 기술한다
- 보조 파일이 있으면 SKILL.md에서 상대 경로로 참조한다

---

## Skill 에스컬레이션 규칙

**동일한 skill이 2개 이상의 프로젝트에서 필요해지면** 루트 `.claude/skills/`로 이동한다.

| 범위 | 위치 | 예시 |
|------|------|------|
| 프로젝트 내부 전용 | `{Project}/.claude/skills/` | 해당 프로젝트에서만 인식 |
| 크로스-프로젝트 공통 | 루트 `.claude/skills/` | 루트에서 실행 시 인식 |

---

## 다국어 프롬프트 규칙

프롬프트 파일(agent, skill)은 **영어를 기본 언어**로 작성하고, 한국어 사본을 함께 보관한다.

### 파일 구성

```
.claude/skills/guard-create-temp-backup/
├── SKILL.md                    ← 영어 원본 (Claude Code가 읽는 파일)
├── SKILL.kr                    ← 한국어 사본 (사용자 열람용)
└── reference.md                ← 보조 문서 (선택)
```

- 한국어 사본은 `.md` 확장자를 config.md의 `prompt_locale_copy` 값(`.kr`)으로 교체한다
- `.kr` 파일은 `.md`가 아니므로 Claude Code가 인식하지 않는다
- 같은 디렉토리에 원본과 나란히 위치하여 사용자가 쉽게 찾을 수 있다

### 운영 규칙

- skill **신규 생성 시** 디렉토리 + `SKILL.md`(영어) + `SKILL.kr`(한국어) 함께 생성한다
- 영어 원본 **수정 시** 한국어 `SKILL.kr`도 반드시 함께 갱신한다
- 에이전트·Claude Code가 skill을 읽을 때는 **항상 `SKILL.md`**를 읽는다
