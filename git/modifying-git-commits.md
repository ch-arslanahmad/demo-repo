# Modifying Local Git Commits

A guide to rewriting local (+remote) commit history safely.

---

## Why Modify Commits?

- Fix a typo in a commit message
- Add forgotten files to a commit
- Combine or reorganize commits
- Remove sensitive data from a commit

> [!WARN]
> Only modify commits that haven't been pushed to shared branches!

---

## Scenario 1: Modify the Last Commit

Use `git commit --amend` to change the most recent commit.

### Change the commit message:

```bash
git commit --amend -m "New commit message"
```

### Add new changes to the last commit:

```bash
git add forgotten_file.txt
git commit --amend --no-edit
```

`--no-edit` keeps the same message. Remove it to also change the message.

---

## Scenario 2: Modify an Older Commit (Not the Last)

Use interactive rebase to modify commits deeper in history.

### Example: Modify the 2nd commit from HEAD

```bash
git rebase -i HEAD~3
```

This shows the last 3 commits:

```
pick abc123 Commit message 1
pick def456 Commit message 2
pick ghi789 Commit message 3
```

### Steps:

1. Change `pick` to `edit` on the line you want to modify:

```
pick abc123 Commit message 1
edit def456 Commit message 2
pick ghi789 Commit message 3
```

2. Save and exit the editor

3. Make your changes:

```bash
git add your_files
git commit --amend
```

4. Continue the rebase:

```bash
git rebase --continue
```

---

## Scenario 3: Commit Already Pushed

### If it's the most recent commit on the branch:

```bash
git commit --amend
git push --force
```

> [CAUTION]
> This will rewrite history. If others have pulled, they'll have issues. Coordinate with your team!

### If it's an older pushed commit:

```bash
git rebase -i HEAD~n
# make your changes
git push --force
```

### Safer alternative (create new commit to revert):

```bash
git revert <commit-hash>
git push
```

This creates a new commit that undoes the changes, preserving history.

---

## Common Scenarios Quick Reference

| Scenario                           | Command                                           |
| ---------------------------------- | ------------------------------------------------- |
| Fix last commit message            | `git commit --amend -m "New message"`             |
| Add files to last commit           | `git add <files> && git commit --amend --no-edit` |
| Modify middle commit               | `git rebase -i HEAD~n` → change `pick` to `edit`  |
| Undo last commit (keep changes)    | `git reset --soft HEAD~1`                         |
| Undo last commit (discard changes) | `git reset --hard HEAD~1`                         |
| Revert a pushed commit             | `git revert <commit-hash>`                        |
| Force push amended commit          | `git push --force`                                |

---

## Visual: Interactive Rebase Flow

```
Before rebase -i HEAD~3:

HEAD
  ↓
ghi789 (3rd commit - newest)
  ↓
def456 (2nd commit - target)
  ↓
abc123 (1st commit - oldest)

After marking "edit" on def456 and amending:

HEAD
  ↓
ghi789 (unchanged)
  ↓
def456' (modified - new hash)
  ↓
abc123 (unchanged)
```

---

## Best Practices

1. **Backup first:** Create a branch backup before rewriting history
   
   ```bash
   git branch backup-branch
   ```

2. **Use `--force-with-lease`** instead of `--force` for safer pushes
   
   ```bash
   git push --force-with-lease
   ```


> [!NOTE]
> `--force-with-lease` flag means, only overwrite if no one else updated the branch after I last fetched (pulled).

3. **Never rewrite public/shared history** unless absolutely necessary

4. **Use `git reflog`** if things go wrong - it tracks all HEAD movements
   
   ```bash
   git reflog
   git reset --hard HEAD@{n} # to go back to a previous state
   ```

5. **Interrupted rebase?** Use `git rebase --abort` to cancel completely and start fresh.

---

## When to Use Rebase vs When It's Overkill

| Use Rebase                               | Don't Rebase - Just Commit                  |
| ---------------------------------------- | ------------------------------------------- |
| Fix local commit messages before sharing | Add missed files → just amend or new commit |
| Combine/squash messy WIP commits         | Small fixes → new commit is cleaner         |
| Reorder commits for clarity              | Already pushed commits → prefer revert      |
| Before merging/PR                        | Time crunch → skip rebase complexity        |



>  [!tip]
> If you're spending more than 5 minutes on rebase for simple changes, just make a new "fix" commit. Clean history is nice, but not worth hours of debugging.
