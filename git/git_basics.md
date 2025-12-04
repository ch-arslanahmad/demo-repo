# Git Basics

## Basic Git Commands

### Make a Repository

To make a repo,

```bash
git init
```

### Commit Changes

A commit is made in two steps: staging and committing.

- First you must add a file for commit (save for simplicity) 
  
  ```bash
  git add <file-name>      # Stage changes for commit
  git commit -m "Commit message"  # Commit staged changes with a message
  ```

> [!NOTE]
> For simplicity, you can think of `git add` as "adding something to save" and `git commit` as "actual save".

> [!TIP]
> You can stage all changed files at once using:
> 
> ```bash
> git add .
> ```

#### Commit Message:

As i have told you that each commit has a SHA, but it must have a message too (except exceptions), that describes what changes were made in that commit.

A good commit message is _concise_ yet **descriptive**.

Example, when you added fixed fingerprint authentication bug, a good commit message would be:

```bash
git commit -m "fixed fingerprint auth bug"
```

Rather than

```bash
git commit -m "fixed bug"
```

### Check Status

To check status if files are staged, modified, or untracked, use:

```bash
git status # also tells current-branch
```

### View Commit History

To view commit history, use:

```bash
git log
```

### View Changes

To view changes made to files, use:

```bash
git diff
```

### Undo Changes

To undo changes in a file before staging, use:

```bash
git restore <file-name>
# or
git restore . # to restore all files
```

> [!TIP]
> When getting a long output from commands like `git log` or `git diff`, you can navigate using:
> 
> - `j` or Down Arrow: Move down one line
> - `k` or Up Arrow: Move up one line
> - `Space`: Move down one page
> - `b`: Move up one page
> - `q`: Quit the viewer





### Answering Questions

1. what does git restore . do, does it remove local/remote commits?

It resets the **files in your working directory** back to the state of the **latest commit (HEAD)**.

So it only affects:

* **Unstaged changes** → removed
* **Uncommitted changes** → removed

Not for,

- commits (local/remote)
- remote repo
- branches & history
