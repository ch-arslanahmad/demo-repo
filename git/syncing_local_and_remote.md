# Syncing Local & Remote Repo


When working in a project, it is essentail that both the local and remote repo are in sync,
- this is increadibly important in collaborative environment

## Rules for local-remote sync

Hence it is necessary to follow these rules,

- always pull before commiting
- push commits regularly
- resolve conflicts as soon as possible

However sometimes, there may be a conflict between local and remote by any reason, because of which you cannot push.

Following is a example scenario.

## Scenario

```bash
You have 3 local commits.
Remote has 1 commit after your last sync.
Current work has unstaged changes.
```

First check status and log:
```bash
git status
git log --oneline --graph --all
```

Save unfinished work (stash)
git statsh push -m "stash message"


You can either do 2 things
- rebase - simpler and easier to read only, Rebasing keeps history linear.
- merge - better if collaborating, easiest to do

Rebasing

Rebasing local commits on top of remote.

git fetch origin
git rebase origin/main # or branch name (main) if different


Now push it to remote,

git push --force-with-lease


> [!important]
> As we are rebasing, which is rewriting history, simple `git push` would have fast-forward and been rejected.
> - Hence we used `--force-with-lease`, which force pushes your commits only if remote repo is the last thing you pushed.
> Only using `force` may cause deleltion of commits in remote blindly without any checks because local has been forced.


Merge

Same scanario:

Simply use the following commands,

```bash

git fetch origin
git merge origin/main # a merge conflict may occur, resolve, commit, then
git push
# git push --abort - to abort, if not good


```


