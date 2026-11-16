#!/usr/bin/env bash
# SessionStart hook: keep this checkout up to date with GitHub.
# Pulls only when it is safe: the branch tracks a remote branch, there are no
# uncommitted changes, and the update is a fast-forward. Otherwise it only reports.
cd "${CLAUDE_PROJECT_DIR:-$(pwd)}" 2>/dev/null || exit 0
git rev-parse --is-inside-work-tree >/dev/null 2>&1 || exit 0

say() { printf '{"systemMessage": "%s", "hookSpecificOutput": {"hookEventName": "SessionStart", "additionalContext": "%s"}}\n' "$1" "$1"; exit 0; }

upstream=$(git rev-parse --abbrev-ref --symbolic-full-name '@{u}' 2>/dev/null) || exit 0
timeout 20 git fetch --quiet 2>/dev/null || say "auto-pull: could not reach GitHub, working with the local copy."

behind=$(git rev-list --count "HEAD..$upstream" 2>/dev/null || echo 0)
[ "$behind" -gt 0 ] || exit 0

if [ -n "$(git status --porcelain)" ]; then
  say "auto-pull: $upstream has $behind new commit(s), but there are uncommitted local changes, so nothing was pulled. Commit or stash them, then run git pull."
fi

if git pull --ff-only --quiet 2>/dev/null; then
  say "auto-pull: pulled $behind new commit(s) from $upstream."
else
  say "auto-pull: $upstream has $behind new commit(s) but the local branch has diverged, so nothing was pulled. Run git pull manually to merge."
fi
