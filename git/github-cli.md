# Github CLI

Github CLI is the way in which  you can interact with github from the terminal.

It is a powerful tool that allows you to manage your repositories, issues, pull requests, and more without leaving the command line.

- [x] How is it going



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



