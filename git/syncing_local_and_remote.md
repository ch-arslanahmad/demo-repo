# Syncing Local & Remote Repo


When working in a project, it is essential that both the local and remote repo are in sync,
- this is incredibly important in collaborative environment

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

```bash
git statsh push -m "stash message"
```

You can either do 2 things
- rebase - simpler and easier to read only, Rebasing keeps history linear.
- merge - better if collaborating, easiest to do

## Rebasing

Rebasing local commits on top of remote.

```bash
git fetch origin
git rebase origin/main # or branch name (main) if different
```

Now push it to remote,

```bash
git push --force-with-lease
```

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


## Upstream Branches (Tracking Branches)

### Upstream

Upstream is simply the connection of the `local` with `remote` branch.

When you create a branch locally, Git doesn't automatically know where to push or pull from.

If `local` branch does not have no upstream,

```bash
⚠ push/pull requires explicit target
```

#### List Branches with Upstreams

Lists all local branches with their upstream and how many commits ahead/behind they are.

```bash
git branch -vv
```

> [!note]
> The output is like,
> ```bash
> ❯ git branch -vv
> * main 90defcb [origin/main] docs(sync): scenario for syncing local and remote repo if conflict
> ```
> You'll see something like, `* main abc1234 [origin/main]` your message. The part in brackets is the upstream. If there's no bracket, *no upstream is set.*




