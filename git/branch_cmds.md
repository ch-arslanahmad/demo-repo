# Git Branch Commands

> [!NOTE]
> Have a basic understading of Git branches before moving to branch commands. You can learn that here: [Git Branches Basics](branches_basics.md)

The following are some common Git branch commands:

## See all Branches
To see all branches in your repository, use the following command:

```bash 
git branch

# See all branches (including remote)
git branch -a
```

## See Current Branch

```bash
git branch --show-current 

git status # also shows current branch
```

## Creating a Branch
To create a new branch, you can use the following command:
```bash
git branch <branch-name> # only creates the branch

git checkout -b <branch-name> # this creates and switches to it
```

## Switching Between Branches
To switch to an existing branch, use:

```bash
git checkout <branch-name> # switches to the branch
```

## Renaming a Branch
To rename the current branch, use:

```bash
git branch -m <new-branch-name> # renames current branch

# To rename a specific branch (not current)
git branch -m <old-branch-name> <new-branch-name>


```

After renaming the local branch, you need to update the remote repository. This involves deleting the old remote branch and pushing the newly named local branch.

```bash
# Delete old branch from remote (using `origin` keyword for remote)
git push origin --delete <old-branch-name>
# Push the renamed branch to remote and set upstream
git push -u origin <new-branch-name>
```


## Deleting a Branch

To delete a branch that is no longer needed:

```bash
# Safe delete: only if fully merged
git branch -d <branch-name>
```

“Fully merged” compared to:
- The branch’s upstream (if set), e.g., main or origin/main
- Otherwise, the current branch (HEAD)

Check before deleting:
```bash
-- see the last section below for more details...
```

Force delete even if not merged:

```bash
git branch -D <branch-name>
```

You can’t delete the branch you’re currently on. Switch first:
```bash
git switch main
git branch -d <branch-name>
```


> [!IMPORTANT]
> Learn the following commands what they mean and how to USE them,
> ```bash
> git branch --merged          # merged into HEAD
> git branch --merged main     # merged into 'main'
> git branch --no-merged main  # not merged into 'main'
> ```