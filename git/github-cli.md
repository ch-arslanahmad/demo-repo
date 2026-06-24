# Github CLI

Github CLI is the way in which you can interact with github from the terminal.

It is a powerful tool that allows you to manage your repositories, issues, pull requests, and more without leaving the command line.

- [x] How is it going

## Features

- [x] Create and manage repositories (local to remote, and vice versa)
- [x] Create and manage issues and pull requests
- [x] View and manage notifications
- [x] Clone repositories and manage local branches

## Install

[Install Guide is HERE.](https://github.com/cli/cli/blob/trunk/docs/install_linux.md)

After installation,

```bash
gh auth login # for authentication
```

## Basics

```bash
gh auth login # for login

gh repo list # to list your own repos

gh repo list username --limit 1000 --json name,url # list repos in JSON

gh repo list username  # lists another user’s repos
gh repo list org-name  # lists all repos in an org

```

## Upload a local repo to remote (GitHub)

To make a local repo into a remote one.

Go inside the local repo and run the following command:

```bash
cd repo-folder
gh repo create knowledge-mcp --source=. --public --push --clone=false
# gh repo create <repo-name> --source=. --public --push --clone=false
```

Flags:

- `--source=.` — use current dir as source
- `--public` — public repo (use --private for private)
- `--push` — push immediately after create
- `--clone=false` — don't clone locally after

## Change visibility of a repo

Change remote repo visibility.

For example to make the repo private, run the following command:

```bash

gh repo edit --visibility private # if you are in the repo folder (locally)
gh repo edit ch-arslanahmad/knowledge-mcp --visibility private  # by username/repo-name

```
