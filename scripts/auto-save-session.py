#!/usr/bin/env python3
"""
Claude Code Stop 훅에서 호출되는 세션 자동 저장 스크립트.
- Stop 훅은 응답 1회 완료 후마다 실행됨 (세션 종료 시가 아님)
- session_id 기반 고정 파일명으로 매 턴마다 덮어쓰기
- 파일명: sessions/YYYY-MM-DD-<session_id[:8]>.md
"""

import json
import sys
from datetime import datetime
from pathlib import Path


# Resolve paths dynamically from the script's location
_SCRIPT_DIR = Path(__file__).resolve().parent
_PROJECT_ROOT = _SCRIPT_DIR.parent
_PROJECT_KEY = str(_PROJECT_ROOT).replace("/", "-").lstrip("-")

PROJECT_JSONL_DIR = Path.home() / ".claude" / "projects" / _PROJECT_KEY
SESSIONS_DIR = _PROJECT_ROOT / "sessions"


def extract_text(content) -> str:
    """message.content에서 텍스트만 추출."""
    if isinstance(content, str):
        return content.strip()
    if isinstance(content, list):
        parts = []
        for block in content:
            if isinstance(block, dict) and block.get("type") == "text":
                text = block.get("text", "").strip()
                if text:
                    parts.append(text)
        return "\n".join(parts)
    return ""


def parse_jsonl(session_id: str) -> tuple[list[dict], str]:
    """
    JSONL 파일을 파싱해 (대화 목록, 세션 시작 시각) 반환.
    세션 시작 시각은 첫 번째 메시지의 timestamp 기준.
    """
    jsonl_path = PROJECT_JSONL_DIR / f"{session_id}.jsonl"
    if not jsonl_path.exists():
        return [], datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    messages = []
    seen_assistant_ids = set()
    session_start = None

    with open(jsonl_path, encoding="utf-8") as f:
        for raw in f:
            raw = raw.strip()
            if not raw:
                continue
            try:
                obj = json.loads(raw)
            except json.JSONDecodeError:
                continue

            # 세션 시작 시각: 첫 snapshot의 timestamp
            if session_start is None:
                snapshot = obj.get("snapshot", {})
                ts = snapshot.get("timestamp")
                if ts:
                    try:
                        dt = datetime.fromisoformat(ts.replace("Z", "+00:00"))
                        session_start = dt.strftime("%Y-%m-%d %H:%M:%S")
                    except ValueError:
                        pass

            msg = obj.get("message", {})
            role = msg.get("role", "")

            if role == "user":
                content = extract_text(msg.get("content", ""))
                # system-reminder, 내부 tool result 등 제외
                if not content:
                    continue
                skip_prefixes = ("<system-reminder", "<command-message", "<function_calls>")
                if any(content.startswith(p) for p in skip_prefixes):
                    continue
                messages.append({"role": "user", "content": content})

            elif role == "assistant":
                # 스트리밍으로 중복 저장되므로 id로 deduplicate
                msg_id = msg.get("id", "")
                if msg_id and msg_id in seen_assistant_ids:
                    continue
                if msg_id:
                    seen_assistant_ids.add(msg_id)

                content = extract_text(msg.get("content", []))
                if content:
                    messages.append({"role": "assistant", "content": content})

    if session_start is None:
        session_start = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return messages, session_start


def session_filename(session_id: str, session_start: str) -> Path:
    """세션 파일 경로 반환 — session_id 기반으로 고정 (덮어쓰기용)."""
    date_part = session_start[:10]  # YYYY-MM-DD
    short_id = session_id[:8]
    return SESSIONS_DIR / f"{date_part}-{short_id}.md"


def save_session(session_id: str, messages: list[dict], session_start: str) -> Path:
    """대화 목록을 마크다운 파일로 저장 (같은 세션은 항상 같은 파일에 덮어쓰기)."""
    SESSIONS_DIR.mkdir(parents=True, exist_ok=True)

    output_path = session_filename(session_id, session_start)
    updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"# 세션 기록: {session_start}\n\n")
        f.write(f"**Session ID**: `{session_id}`  \n")
        f.write(f"**Last Updated**: {updated_at}  \n")
        f.write(f"**Turns**: {sum(1 for m in messages if m['role'] == 'user')}\n\n")
        f.write("---\n\n")

        if not messages:
            f.write("*(대화 내용 없음)*\n")
        else:
            for msg in messages:
                if msg["role"] == "user":
                    f.write(f"## 사용자\n\n{msg['content']}\n\n")
                else:
                    f.write(f"## Claude\n\n{msg['content']}\n\n")
                f.write("---\n\n")

    return output_path


def resolve_session_id() -> str:
    """stdin payload에서 session_id 추출, 없으면 최신 JSONL 사용."""
    payload_raw = sys.stdin.read().strip()
    if payload_raw:
        try:
            payload = json.loads(payload_raw)
            sid = payload.get("session_id")
            if sid:
                return sid
        except json.JSONDecodeError:
            pass

    jsonl_files = sorted(
        PROJECT_JSONL_DIR.glob("*.jsonl"),
        key=lambda p: p.stat().st_mtime,
        reverse=True,
    )
    if jsonl_files:
        return jsonl_files[0].stem

    print("[auto-save-session] JSONL 파일을 찾을 수 없습니다.", file=sys.stderr)
    sys.exit(1)


def main():
    session_id = resolve_session_id()
    messages, session_start = parse_jsonl(session_id)
    output_path = save_session(session_id, messages, session_start)
    print(f"[auto-save-session] 저장: {output_path} ({sum(1 for m in messages if m['role'] == 'user')} turns)")


if __name__ == "__main__":
    main()
