# Configure Git

Here we will configure `git` with my customizations.

If you have configured basic, `globa user.name` and `global user.email`, then you will see the following in the `.gitconfig` file:

```ini
[user]
	email = ch.arslanad@gmail.com
	name = ch-arslanahmad
```

> [!NOTE]
> The format of `.gitconfig` file is INI format.

# Customizations

## Setting default branch name

You can add,
```ini
[init]
    defaultBranch = main
```

## Line Endings

Cross-platform? Normalize line endings. For a Linux workflow, run:

```ini
[core]
    autocrlf = input
```

## Aliases (speed boosters)

You can create shortcuts for common git commands using aliases(same as linux). Here are some useful ones:

```ini

[alias]
    st = status
    co = checkout
    br = branch
    cm = commit -m
    df = diff
    lg = log --oneline --graph --decorate --all

```

Now you can use them with `git` like:
- `git st` for `git status`
- `git co` for `git checkout`
- `git df` for `git diff`
- and so on.

## Others

Aside from this basic configuration,

Others include,
- setting up default text editor
- configuring merge tool
- setting up colors for better visibility
- configuring credential helpers for easier authentication
- adding a global .gitignore file to ignore common files across all repositories

You can do this by following:

```ini
# tobeadded
```