# Configuration in `git`

As you know `git` is a version-control system originally made to track changes in kernel (Linux by Linus).

You may know basic configuration but advanced configuration is also possible via `.gitconfig` file or `git config` command.


As you know:
- In Linux, you can configure and customize almost every native app and `git` is no exception.
- `git config` command, used to set:
    - user_name
    - email
    - gpg key
    - preferred diff algorithm
    - file formats and many more.

- configuration is at 3 levels:

|Configuration Level|Limit|Path|
|--|--|--|
|local|per repo|`<repo-path>/.gitconfig`|
|global|per user| - `~/.gitconfig` - Linux, macO  & `C:\Users\<username>\.gitconfig` - Windows|
|system|all|`/etc/gitconfig` or `$(prefix)/etc/gitconfig` - Linux, macOS (may not exist), & `C:\ProgramData\Git\config\` - Windows|

# Basic usage

You can set global configuration (applied to all repositories) using:
```bash
git config --global user.name "Your Name"
git config --global user.email "example@example.com"
```

## Viewing configuration

To view your current configuration, you can use:

```bash
git config --list
git config --global --list
git config --system --list
```

Alternatively, you can view see, `.gitconfig` file directly.

> [!IMPORTANT]
> Learn how to [configure git.](learn_config_git.md)