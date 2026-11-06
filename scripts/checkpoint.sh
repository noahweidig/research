#!/usr/bin/env bash
set -e
git config user.name "zotero-sync[bot]"
git config user.email "zotero-sync@users.noreply.github.com"
git add -A papers .state
git diff --cached --quiet && exit 0
git commit -qm "Zotero sync progress $(date -u +%FT%TZ)"
for i in 1 2 3; do git pull -q --rebase && git push -q && exit 0; sleep $((i*3)); done
exit 1
