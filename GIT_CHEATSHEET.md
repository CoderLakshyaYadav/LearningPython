# Git Cheat Sheet (Beginner, `main` + `origin`)





## 1) Daily workflow (safe)

```zsh
git status -sb
git pull --rebase origin main
git add .
git commit -m "your message"
git push

```

## 2) First-time setup (once per machine)

```zsh
git config --global user.name "CoderLakshyaYadav"
git config --global user.email "yadavl@s.dcsdk12.org"
git init
git remote add origin <repository_url>
git branch -M main
git add .
git commit -m 'Your commit message here!'
git status
git push -u origin main
```

Check values:

```zsh
git config --global user.name
git config --global user.email
```

## 3) New repo setup (once per repo)

```zsh
git init
git branch -M main
git remote add origin https://github.com/<username>/<repo>.git
git add .
git commit -m "Initial commit"
git push -u origin main
```

## 4) Common issue: push rejected (fetch first)

Error meaning: GitHub has commits you do not have locally.

```zsh
git fetch origin
git pull --rebase origin main
git push -u origin main
```

If rebase has conflicts:

```zsh
git status
# fix files with conflict markers
# <<<<<<<
# =======
# >>>>>>>
git add <fixed-file>
git rebase --continue
git push -u origin main
```

Cancel rebase if needed:

```zsh
git rebase --abort
```

## 5) Ignore IDE files (`.idea/`)

```zsh
printf ".idea/\n" >> .gitignore
git add .gitignore
git commit -m "Ignore PyCharm project files"
git push
```

## 6) Useful checks

```zsh
git status -sb
git branch -vv
git remote -v
git log --oneline --decorate --graph -n 12
```

## 7) Undo commands (safe first)

Unstage a file:

```zsh
git restore --staged <file>
```

Discard local unstaged edits to a file:

```zsh
git restore <file>
```

Change last commit message:

```zsh
git commit --amend -m "new message"
```

Undo last commit but keep changes:

```zsh
git reset --soft HEAD~1
```

## 8) Safety rules

- Run `git status` before and after pull/push.
- Prefer `git pull --rebase origin main` before pushing.
- Do not use `git push --force` unless you fully understand why.
- If stuck in `git log`, press `q` to quit pager.
- Keep commits small and messages clear.
- Commit often; push at the end of a working session.

## 9) Quick recovery checklist

1. `git status -sb`
2. `git branch -vv`
3. `git fetch origin`
4. `git pull --rebase origin main`
5. Resolve conflicts if shown
6. `git push`

