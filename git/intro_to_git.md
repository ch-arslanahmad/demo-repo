// - What is Git, why version control matters, snapshots vs diffs, repos, working directory.
# Intro to Git

Git is a version control system useful for tracking changes.

### Example

It means, it tracks every change so via `git` you can go to the first change you made to a folder or a file, you can time travel of sorts. See how file was at a specific time and who made the change all via `git`.

## Why Git Matters?

Version control is essential for several reasons:
1. **Collaboration**: Git allows multiple people to work on the same project simultaneously without overwriting each other's changes.
2. **History Tracking**: Git keeps a detailed history of changes, making it easy to revert to previous versions if needed.
3. **Branching and Merging**: Git enables you to create branches for new features or experiments, which can later be merged back into the main project.

As you have learnt that Git is a version control system that helps you track changes in your files and collaborate with others. Here are some fundamental concepts and commands to get you started with Git.

## Key Concepts

The following are really basic concepts in Git that you should be familiar with:

* **Repository (Repo)**: A directory (folder) that contains your project files and the history of changes made to them.
* **Commit**: A snapshot of your files at a specific point in time.
  * Each commit has a unique ID called a SHA, like 8db0f224589c808727d4a8e0a4202e79998623f7, you can even use a shortened version of it, example., 8db0f22.
* **Branch**: It can be defined as:
  * separate line of development
  * separate version of workspace of your project
  * a seperate version of your repo.

The default branch is usually called `main` or `master`.

* **Remote**: version of your repo hosted on the internet or another network.
* **Local**: version of your repo on your own computer.

* **Staging Area**: A place where you can group (add) changes, before committing them.

* **Untracked Files**: Files in your working directory that are not being tracked by Git.

* `.gitignore` - tells which files, folders (or patterns) to ignore in a repo.

* **Working Directory**: The (actual) files and folders you see in your project folder on your computer. It differs from the (local/remote) repository, which contains the history of changes.

Now learn some basic commands to get started with Git here: [Basic Git Commands](git_basics.md)