# CLAUDE.md — ClaudeProjects 메타 프로젝트

이 파일은 `ClaudeProjects/` 루트에서 실행할 때만 단독 로드된다.
하위 디렉토리에서 실행하면 이 파일과 하위 CLAUDE.md가 **함께** 로드된다.

---

## 프로젝트 구조

### 루트 구조

```
ClaudeProjects/
├── CLAUDE.md                  ← 공통 규칙 (이 파일)
├── .claude/
│   ├── config.md                  ← 프로젝트 공통 설정
│   ├── agents/                    ← 루트 공통 에이전트
│   ├── naming-convention-map.md   ← 명명 규칙 매퍼 (표준 어휘)
│   ├── skills/                    ← 루트 공통 skills
│   └── commands/                  ← 슬래시 커맨드 (project/, agent/, file/, session/ 분류)
├── docs/                      ← 루트 전용 참조 문서
│   └── public/                ← 서브 프로젝트 공유 문서
├── make/                      ← 설계 문서 + 기능 계획 + 변경 이력
├── handoffs/                  ← 완료된 HANDOFF.md 아카이브
├── input/                     ← 외부에서 받은 입력 데이터
├── project_transactions/      ← 프로젝트 간 데이터 교환
├── pending/                   ← 삭제 대기·변경 제안 (운영용)
├── output/                    ← 루트 레벨 출력물
├── scripts/                   ← 훅·유틸리티 스크립트
├── sessions/                  ← 루트 대화 세션 기록
└── ClaudeProject_*/           ← 서브 프로젝트들
```

### 서브 프로젝트 공통 구조

> 상세는 참조 문서 섹션의 `project-creation-guide.md`를 참조한다.

```
{ProjectName}/
├── CLAUDE.md            ← 통일 템플릿
├── PROFILE.md           ← 프로젝트별 세부사항
├── .claude/
│   ├── config.md        ← 프로젝트 설정
│   ├── agents/          ← 에이전트
│   ├── skills/          ← skill 모듈
│   └── commands/        ← 슬래시 커맨드
├── input/               ← 다른 프로젝트로부터 받은 입력 데이터
├── make/                ← 설계 문서 + 기능 계획 + 변경 이력
├── handoffs/            ← 완료된 HANDOFF.md 아카이브
├── output/              ← 최종 보고서
├── pending/             ← 삭제 대기·변경 제안 (운영용)
├── scripts/             ← 훅·유틸리티 스크립트
├── sessions/            ← 대화 세션 기록
├── todo/                ← 미해결 작업 항목
└── transactions/        ← 에이전트 간 데이터 교환
```

> 프로젝트 목록은 참조 문서 섹션의 `project-registry.md`를 참조한다.

---

## 슬래시 커맨드

파일 삭제는 반드시 `/file:delete`를 통해서만 수행한다 (파일 삭제 규칙 참조).
개별 커맨드 상세는 `docs/command-guide.md`를 참조한다.

| 폴더 | 용도 |
|------|------|
| `project/` | 서브 프로젝트 CRUD + 동기화 + 실행 |
| `agent/` | 에이전트 sub-agent 실행 |
| `docs/` | 공용 참조 문서 관리 |
| `file/` | 파일 삭제 관리 (삭제 대기 등록·실행) |
| `session/` | 세션 기록 관리 (저장·조회·삭제·병합·통합) |

---

## 공유 참조 문서

`docs/public/`은 루트와 서브 프로젝트가 공통으로 참조하는 문서다.

| 문서 | 용도 |
|------|------|
| `docs/public/config-template.md` | config.md 작성 템플릿 |
| `docs/public/skill-guide.md` | Skill 구조, YAML, 다국어 규칙 |
| `docs/public/file-naming-convention.md` | 파일/디렉토리 명명 규칙 |
| `docs/public/dev-environment-guide.md` | Docker, Sandbox, 실행환경 설정 |

---

## 공통 운영 규칙

### 세션 시작 시 로드

작업 시작 전 아래 항목을 순서대로 확인한다:

1. `HANDOFF.md` — 이전 세션에서 넘긴 미완료 작업 (있을 때만)
2. `todo/` — 미해결 작업 항목
3. `sessions/*-stable.md` — 최신 stable 세션 (통합 기준선)
4. stable 이후 생성된 세션 파일 — 아직 통합되지 않은 최신 변경 사항

- 로드할 데이터의 총 크기가 과도하면 사용자에게 알리고 확인을 받는다

### 커맨드 우선 확인

- 사용자의 요청을 실행하기 전에 `.claude/commands/` 폴더를 확인하여 **동일하거나 유사한 기능의 커맨드가 있는지** 먼저 탐색한다
- 해당 커맨드가 있으면 직접 실행 대신 **커맨드를 통해 수행**한다
- 커맨드가 없을 때만 직접 실행한다

### SESSION_ID 형식

```
YYYYMMDD-{4자리 순번}
예: 20260219-0001
```

- 오케스트레이터가 서브 에이전트별로 **고유한 SESSION_ID**를 발급한다
  - 예: 에이전트 A → `20260222-0001`, 에이전트 B → `20260222-0002`
- 단독 실행 시에는 `transactions/` 폴더에서 오늘 날짜 파일 수 +1 로 결정한다
- SESSION_ID 없이 하위 에이전트를 호출하지 않는다

### input / output 규칙

- 모든 프로젝트는 `input/`에서 입력을 읽고 `output/`에 결과를 저장한다
- 다른 프로젝트의 폴더를 직접 참조하지 않는다
- 프로젝트 간 데이터 전달은 메인 프로젝트(오케스트레이터)가 조율한다
- **사용자가 읽는 보고서(`output/`)는 한국어로 작성한다** — 에이전트 간 교환용 JSON 등 기계 처리 파일은 영어 허용

### transactions 규칙

- `transactions/`는 서브 프로젝트 내 **sub-agent 간 데이터 공유** 전용 폴더다
- sub-agent는 작업 결과를 `transactions/{SESSION_ID}-{내용}.json` (또는 `.md`) 파일로 저장한다
- 후속 sub-agent는 이전 agent가 남긴 transactions 파일을 읽어 이어서 작업한다
- 파일명에 SESSION_ID를 포함하여 같은 파이프라인의 데이터를 식별한다
- `output/`은 사용자용 최종 보고서, `transactions/`는 에이전트 간 중간 결과물이다

### config.md 규칙

- 에이전트는 설정값(경로, 재시도 횟수 등)을 **하드코딩하지 않는다**
- 작업 전 `.claude/config.md`를 읽고 해당 설정값을 사용한다
- 서브 프로젝트 config가 있으면 **해당 프로젝트 값 우선**, 없으면 루트 config를 사용한다
- config.md 작성 형식은 `docs/public/config-template.md`를 참조한다

### 다국어 프롬프트 규칙

- 프롬프트 파일(agent, skill)은 **영어(.md)**를 기본 언어로 작성한다
- 한국어 사본은 `.md` 확장자를 `.kr`로 교체하여 같은 디렉토리에 보관한다 (사용자 열람용)
- `.kr` 파일은 Claude Code가 인식하지 않으므로 프롬프팅에 영향 없음
- 신규 생성 시 `.md`(영어) + `.kr`(한국어) 쌍을 함께 만든다
- 영어 원본 수정 시 `.kr` 사본도 반드시 함께 갱신한다
- 상세는 `docs/public/skill-guide.md`를 참조한다

### 저장 의무

- 모든 분석·수정 결과는 반드시 파일로 저장한다 (대화창 출력만은 금지)
- 저장 후 사용자에게 파일 경로를 알린다

### 서버 안전 규칙

- **리눅스 서버(OS) 자체를 재시작·종료하지 않는다** — 예외 없음

### 프로젝트 실행 시 todo 확인

- 서브 프로젝트를 실행(`/project:run`)할 때 해당 프로젝트의 `todo/` 폴더를 확인한다
- todo 항목이 있으면 작업 시작 전 사용자에게 목록을 보여주고 리마인드한다
- todo 파일이 해결되면 사용자 확인 후 삭제한다

### 프로젝트 변경 감지

프로젝트 세팅(에이전트, 스킬, 커맨드, 구조 등)이 변경될 때 아래를 확인한다:

1. **변경 영향 스캔**: 변경된 항목(이름, 경로, 역할)을 참조하는 문서와 기능을 스캔한다
   - 커맨드 목록 (`commands/`)
   - 프로젝트 명세 (`PROFILE.md`, `docs/project-registry.md`)
   - 컴포넌트 현황 (`docs/component-audit-status.md`)
   - 명명 규칙 맵 (`.claude/naming-convention-map.md`)
   - 에이전트/스킬 간 cross-reference
2. **불일치 경고**: 갱신이 필요한 항목을 사용자에게 목록으로 알린다
3. **갱신 커맨드 안내**: 해당하는 커맨드가 있으면 안내한다 (예: `/agent:rename`, `/project:sync`)

---

## HANDOFF 규칙

작업이 중단될 때(토큰 초과, 세션 종료, 작업 전환 등) 다음 작업자가 이어받을 수 있도록 `HANDOFF.md`를 작성한다.

### 작성 시점

- 작업을 완료하지 못한 채 세션이 끝날 때
- 다른 에이전트 또는 다음 세션으로 작업을 넘길 때
- 작업 범위가 커서 분할이 필요할 때
- **context 잔여량이 10% 미만**이 되면 즉시 HANDOFF.md를 작성하고 사용자에게 `/clear` 안내한다

### 파일 위치

- 각 프로젝트 루트에 `HANDOFF.md`를 작성한다
- 완료된 HANDOFF는 `handoffs/{SESSION_ID}-handoff.md`로 이동한다

### 필수 내용

```markdown
# HANDOFF

## 현재 상태
(어디까지 완료했는지)

## 미완료 항목
(남은 작업 목록)

## 주의사항
(다음 작업자가 알아야 할 컨텍스트, 주의점)
```

### Context Handoff 규칙

- Sub-agent가 context의 **70%를 초과**하면 즉시 HANDOFF 방식으로 전환한다
- 현재까지의 작업 결과를 파일로 저장한 뒤 `HANDOFF.md`를 작성한다
- 메인 에이전트에 중간 결과를 반환하고, 메인 에이전트가 새 sub-agent를 생성하여 이어서 진행한다
- HANDOFF.md 형식은 위 "필수 내용"을 따른다

---

## 세션 저장 규칙

- 매 세션 종료 시 대화 내역을 `sessions/YYYY-MM-DD-HHMMSS.md`로 저장한다
- 사용자가 `/save-session`을 호출하거나 세션 종료를 알리면 즉시 저장한다
- 세션 파일에는 주요 논의 내용, 결정 사항, 완료 작업, 미해결 사항, 참고 파일을 포함한다

---

## 파일 삭제 규칙

- 삭제 권한은 **사용자에게만** 있다
- **사용자가 삭제를 지시하면** `rm`으로 즉시 삭제한다 — pending 등록·`/file:delete` 절차 불필요
- **에이전트가 자체 판단으로 삭제가 필요한 경우** 직접 삭제하지 않는다 — `pending/pending-delete.md`에 등록하고 사용자에게 `/file:delete`를 안내한다
- 등록 형식: `## SESSION {SESSION_ID}` 아래에 대상·사유 표를 작성한다
- 사용자가 `/file:delete <번호>` 또는 `/file:delete all`을 호출하면 커맨드 절차에 따라 삭제한다

---

## CLAUDE.md 수정 규칙

- **사용자가 명시적으로 수정을 요청한 경우에만** 이 파일을 수정한다
- 수정이 필요하다고 판단되면 `pending/pending-changes.md`에 변경 제안을 기록하고 사용자에게 알린다
- 형식: `## SESSION {SESSION_ID}` 아래에 대상 섹션·변경 내용·사유를 작성한다
- 사용자 승인 후에만 반영한다

---

## 주요 경로 참조

> 프로젝트별 세부사항은 각 프로젝트의 `PROFILE.md`를 참조한다.
> 파일 명명 규칙은 `docs/public/file-naming-convention.md`를 참조한다.
> 명명 규칙 표준 어휘(Category/Action/Target)는 `.claude/naming-convention-map.md`를 참조한다.
> Skill 구조는 `docs/public/skill-guide.md`를 참조한다.
