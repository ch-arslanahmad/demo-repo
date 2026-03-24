# Git Intermediate

Intermediate Commands & Use Cases are as follows:

## Rename Last Commit Message

```bash

git commit -amend # opens default editor to change the last commit message
git commit -amend "New commit message" 

```

## Rename or Update any Commit Message

```bash

git rebase -i HEAD~3
# opens editor with last 3 commits,
# change 'pick' to 'reword' for the commit you want to change the message of, save and exit,
# editor will open again for you to change the commit message, save and exit
```

> [!caution]
> Safe if commit is local (not pushed to remote), if pushed,
> ```bash
> git push --force # do not do if working in a team, dangerous
> ```
> In teams, only rename commits that haven’t been pushed yet, unless everyone is aware and agrees to the change.


## Temporarily Stash Changes

**Stash:** Stash is simply `git` creating a new commit with the changes you want to stash, but it’s not on any branch, so it’s not part of your commit history. It’s like a temporary storage for your changes.

To stash changes, you can use:
```bash

git stash # stash uncommited changes.
git stash save "message" # stash with a message to identify it later.

```

List stashes, and switch to a stash:
```bash

git stash list # list all stashes

git stash apply # it applies the most recent (or only) stash

git stash apply stash@{0} # specify a stash by its index


git stash pop # it deleted latest stash after applying it

git stash pop # to apply + remove

```

## Viewing Commit History

Rather than simply using `git log`, you can get more concise output. 

```bash

git log --online # shows each commit in oneline.

git log --online --graph --all --decorate # long but shows branches, tags, and a graph of the commit history.

```
For convienience, you can create an alias for this command.


## Remote Info

```bash
git remote -v
```

It return info regarding remote info, good for [upstream and downstreaming](~/Desktop/github/demo-repo/git/syncing_local_and_remote.md).
```



