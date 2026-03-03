# 슬래시 커맨드 가이드

> 루트(`ClaudeProjects/`)의 `.claude/commands/` 아래에 폴더별로 분류되어 있다.
> 이 커맨드들은 **루트에서만 실행**한다 — 서브 프로젝트 디렉토리에서는 사용 불가.

---

## 커맨드 목록

| 폴더 | 용도 | 커맨드 |
|------|------|--------|
| `project/` | 서브 프로젝트 CRUD + 동기화 + 실행 | `create`, `delete`, `modify`, `list`, `sync`, `run` |
| `agent/` | 에이전트 sub-agent 실행 | `run` |
| `docs/` | 공용 참조 문서 조회 | `public` |
| `file/` | 파일 삭제 관리 (삭제 대기 등록·실행) | `delete`, `pending` |
| `session/` | 세션 기록 관리 | `save`, `list`, `delete`, `merge`, `consolidate` |

---

## 호출 형식

```
/폴더:커맨드
```

예: `/project:create`, `/agent:run`, `/docs:public`, `/file:delete`, `/session:save`

---

## 커맨드 상세

### project/

| 커맨드 | 설명 |
|--------|------|
| `create` | 서브 프로젝트 생성 + 레지스트리 등록 |
| `delete` | 서브 프로젝트 삭제 |
| `modify` | 레지스트리 정보(역할, 상태 등) 변경 |
| `list` | 프로젝트 레지스트리 목록 조회 |
| `sync` | 에이전트/스킬 변경 후 naming-convention-map, audit-status 일괄 동기화 |
| `run` | 프로젝트 선택 → 에이전트 선택 → 현재 대화에서 직접 실행 |

### agent/

| 커맨드 | 설명 |
|--------|------|
| `run` | 에이전트 선택 → input 파일 생성 → Task 도구(sub-agent)로 실행 |

### docs/

| 커맨드 | 설명 |
|--------|------|
| `public` | `docs/public/` 공용 문서 관리 (조회·추가·삭제·이름변경 + CLAUDE.md 연쇄 갱신) |

### file/

| 커맨드 | 설명 |
|--------|------|
| `delete` | 삭제 대기 목록에서 선택하여 삭제 실행 |
| `pending` | 삭제 대기 목록 조회 |

### session/

| 커맨드 | 설명 |
|--------|------|
| `save` | 현재 세션을 `sessions/`에 저장 |
| `list` | 세션 기록 목록 조회 |
| `delete` | 세션 기록 삭제 |
| `merge` | 세션 병합 및 재정리 |
| `consolidate` | 세션 분석 → 프로젝트 비교 → 불필요 제거 → stable 파일로 통합 |

---

## 규칙

- 파일 삭제는 반드시 `/file:delete`를 통해서만 수행한다
- 서브 프로젝트 자체 커맨드가 있으면 해당 커맨드를 우선 사용한다
