# Setup Git

As you know you can use,

```bash
git clone github.com/username/repo.git # via HTTPS

git clone git@github.com:username/repo.git # via SSH
```

Using these commands you can easily `clone` any public repo..

To get access to any `private` repo, you need

- have a GitHub/GitLab (etc) account
- read/write access to repo

For that you need to login to `git` via the account, you can login via:

- HTTPS
- SSH


## Setup via SSH


Got it! Let’s set up Git with SSH on Ubuntu (or any Linux) quickly and easily. I’ll give you a step-by-step streamlined version.

---

### 1. Check for existing SSH keys

```bash
ls -al ~/.ssh
```

Look for files like `id_rsa` or `id_ed25519`. If you have one, you can skip key generation.

![list-all-ssh-keys](img/step_1(ssh).png)

---

### 2. Generate a new SSH key (if none exists)

I recommend Ed25519 (modern, fast, secure):

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

* Press Enter to accept default file location.
* Optional: add a passphrase (more secure).

![Generating SSH key](img/step-2(ssh).png)

---

### 3. Start the SSH agent

```bash
eval "$(ssh-agent -s)"
```

---

### 4. Add your key to the agent

```bash
ssh-add ~/.ssh/id_ed25519
```

---

### 5. Copy your SSH key

```bash
cat ~/.ssh/id_ed25519.pub
```

Copy the entire output (starts with `ssh-ed25519`).

![Getting the Public SSH key](img/step-3-5(ssh).png)

---

### 6. Add the key to GitHub/GitLab/Bitbucket etc

* GitHub: [https://github.com/settings/keys](https://github.com/settings/keys) → “New SSH key” → Paste.
* GitLab: [https://gitlab.com/-/profile/keys](https://gitlab.com/-/profile/keys)
* Bitbucket: [https://bitbucket.org/account/settings/ssh-keys/](https://bitbucket.org/account/settings/ssh-keys/)


---

### 7. Test the connection

Finally, test the connection,

```bash
ssh -T git@github.com
```

You should see something like:

```
Hi username! You've successfully authenticated.
```

![authenticated SSH key](img/step_6(ssh).png)

---

### 8. Set Git to use your email & name


Before using any git operations, you may need to tell who you are..

Hence, you can set your username and email via the following commands:

```bash
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"
```

---


Now you can clone repos using SSH:

```bash
git clone git@github.com:username/repo.git
```

Simply put, you can do `git` operations over `SSH`.

> [!NOTE]
> `clone` was told as an example, this is not limited to only `clone` rather concerning reading, modifying, any private or restricted repository.



---

If you want, I can also give you a one-liner that sets up SSH key + adds to agent + copies it to clipboard so it’s literally a 2-minute setup.

Do you want me to do that?


