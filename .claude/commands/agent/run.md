# 에이전트 실행

지정한 에이전트를 Task 도구(sub-agent)로 직접 실행한다.
입력 파일을 생성하고 에이전트에게 입력 파일 경로와 SESSION_ID를 전달한다.

## 인자

$ARGUMENTS — 에이전트 이름 또는 경로 (선택). 생략하면 목록에서 선택.

## 출력 규칙

- 중간 설명 없이 진행 상황과 결과만 출력한다

## 실행 절차

### Step 1 — 에이전트 선택

1. `$ARGUMENTS`가 있으면:
   - 전체 경로면 해당 파일을 직접 사용한다
   - 이름만 있으면 루트 `.claude/agents/`와 활성 프로젝트의 `.claude/agents/`에서 검색한다
   - 부분 일치도 허용한다 (예: `compose` → `orchestrate-compose-execution-pipeline`)
2. 없으면:
   - 루트 `.claude/agents/*.agent-v1.0.md`를 수집한다
   - `docs/project-registry.md`에서 활성 프로젝트를 읽고 각 프로젝트의 `.claude/agents/*.agent-v1.0.md`를 수집한다
   - 프로젝트별로 그룹화하여 보여준다:
     ```
     # 에이전트 목록

     ## 루트 (ClaudeProjects)
     | # | 에이전트 | 설명 |
     |---|---------|------|
     | 1 | orchestrate-compose-execution-pipeline | 파이프라인 구성 |
     | 2 | orchestrate-coordinate-cross-project | 크로스 프로젝트 조율 |

     ## ClaudeProject_example
     | # | 에이전트 | 설명 |
     |---|---------|------|
     | 3 | example-agent | 예시 에이전트 |
     ...
     ```
   - 사용자에게 번호로 선택하게 한다
3. 에이전트 파일의 YAML frontmatter를 읽어 `name`, `description`, `model`, `tools`를 파악한다

### Step 2 — 에이전트 소속 프로젝트 판별

에이전트 파일 경로에서 소속 프로젝트를 판별한다:
- `.claude/agents/` (루트) → 프로젝트 = `ClaudeProjects` (루트)
- `ClaudeProject_*/.claude/agents/` → 프로젝트 = 해당 서브 프로젝트

이 프로젝트 경로가 이후 input/output 경로의 기준이 된다.

### Step 3 — 작업 내용 입력

사용자에게 질문한다:
- **작업 목표**: 이 에이전트에게 무엇을 시킬 것인지
- **추가 컨텍스트**: 필요한 배경 정보나 이전 단계 출력 파일 경로 (선택)

### Step 4 — SESSION_ID 발급

1. 소속 프로젝트에 `transactions/` 폴더가 있으면 거기서, 없으면 루트 `sessions/`에서 오늘 날짜 파일 수를 센다
2. `SESSION_ID = YYYYMMDD-{4자리 순번}` (예: `20260223-0001`)

### Step 5 — 입력 파일 생성

`{프로젝트}/input/{SESSION_ID}-task.md` 파일을 생성한다:

```markdown
# Task Input

## SESSION_ID
{SESSION_ID}

## Agent
{에이전트 이름}

## Project
{프로젝트 이름}

## Goal
{사용자가 입력한 작업 목표}

## Context
{사용자가 입력한 추가 컨텍스트, 없으면 "없음"}

## Created
- Command: `/agent:run`
- Date: {YYYY-MM-DD HH:MM}
```

### Step 6 — Sub-Agent 실행

Task 도구를 사용하여 에이전트를 sub-agent로 실행한다.

**프롬프트 구성:**
```
에이전트 프롬프트 파일: {에이전트 파일 전체 경로}
SESSION_ID: {SESSION_ID}
입력 파일: {프로젝트}/input/{SESSION_ID}-task.md

위 입력 파일을 읽고, 에이전트 프롬프트의 절차에 따라 작업을 수행하라.
작업 전 에이전트 프롬프트 파일을 먼저 읽어라.
소속 프로젝트의 .claude/config.md가 있으면 참조하라.
결과는 {프로젝트}/transactions/ 또는 {프로젝트}/output/ 에 저장하라.
```

**Task 도구 설정:**
- `subagent_type`: 해당 에이전트가 등록된 subagent_type이 있으면 사용, 없으면 `general-purpose`
- `description`: `{에이전트 이름} 실행`
- `model`: 에이전트 YAML의 `model` 값 사용

### Step 7 — 결과 보고

실행 완료 후 결과를 요약한다:

```
## 실행 결과

| 항목 | 값 |
|------|-----|
| 에이전트 | {에이전트 이름} |
| 소속 프로젝트 | {프로젝트} |
| SESSION_ID | {SESSION_ID} |
| 입력 파일 | {입력 파일 경로} |
| 출력 파일 | {에이전트가 생성한 파일 경로} |
| 상태 | 성공 / 실패 |
```
