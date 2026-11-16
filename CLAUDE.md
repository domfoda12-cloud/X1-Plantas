# X1-Plantas

## Keeping the local copy in sync with GitHub

- A SessionStart hook (`.claude/hooks/auto-pull.sh`) pulls new commits automatically when a session starts, but only when it is safe (no uncommitted changes, fast-forward only). If it reports that it could not pull, tell the user why and offer to fix it.
- Before editing files in a long-running session, or when the user says something was changed on GitHub, run `git fetch` and check `git status`. If the branch is behind and the working tree is clean, run `git pull --ff-only`. If there are local changes, ask before stashing or merging.
- After making changes the user wants to keep, offer to commit and push them so GitHub stays the up-to-date copy.

## Agents

- `editor` (`.claude/agents/editor.md`): short-form video and content strategist based on the "going viral = supply and demand" framework.
