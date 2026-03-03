# config.md 프로젝트 설정 가이드

> CLAUDE.md에서 분리된 참조 문서. config.md 작성·수정 시 참조한다.

---

## config.md 규칙

- 에이전트는 재시도 횟수, 백업 경로 등 **설정값을 하드코딩하지 않는다**
- 작업 전 `.claude/config.md`를 읽고 해당 설정값을 사용한다
- 서브 프로젝트 config가 있으면 **해당 프로젝트 값 우선**, 없으면 루트 config를 사용한다

---

## config.md 표준 템플릿

```markdown
# Project Config — {프로젝트명}

> 에이전트가 참조하는 프로젝트 설정값.

## 설정값

| 키 | 값 | 설명 |
|----|----|------|
| `max_retry_count` | 10 | 작업 실패 시 최대 재시도 횟수 |
| `backup_dir` | `.claude/_temp_backup` | 임시 백업 저장 경로 |
| `backup_ttl_hours` | 24 | 백업 보존 시간 (시간 초과 시 경고) |
| `prompt_default_lang` | `en` | 프롬프트(agent, skill) 기본 작성 언어 |
| `prompt_locale_copy` | `.kr` | 한국어 사본 확장자 (.md → .kr로 교체) |
```

프로젝트 성격에 따라 설정값을 추가할 수 있다.
