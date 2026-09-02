
# git reset • --soft • --mixed • --hard • HEAD • git revert

---

## Learning Goals

- Understand what `git reset` does and how it moves the HEAD pointer.
- Know the difference between `--soft`, `--mixed`, and `--hard` options.
- Understand the meaning of `HEAD`, `HEAD~1`, and `HEAD~2`.
- Use `git reset` carefully (especially `--hard`).
- Understand what `git revert` does and when to use it instead of reset.
- Know the practical difference between reset and revert.

---

## 1. Visual Representation of Commits

Imagine your commit history like this:

```text
C0 (Initial commit - README)
   ↓
C1 ("1st commit" - Hi Team)
   ↓
C2 ("2nd commit" - Hi Students)   ← HEAD is here
```

- **HEAD** → points to the latest commit (currently C2)
- **HEAD~1** → one commit before HEAD (C1)
- **HEAD~2** → two commits before HEAD (C0)

---

## 2. Practical Setup (What we did in class)

1. Created a repository on GitHub: `git-reset-revert-commands-practice`
2. Initial commit (C0) with README file.
3. Created `index.html` with:
   ```html
   <h1>Hi Team</h1>
   ```
   Then:
   ```bash
   git add .
   git commit -m "1st commit"     # This is C1
   ```
4. Updated `index.html` to:
   ```html
   <h1>Hi Team</h1>
   <h1>Hi Students</h1>
   ```
   Then:
   ```bash
   git add .
   git commit -m "2nd commit"     # This is C2
   ```

---

## 3. git reset Commands

`git reset` moves the **HEAD** pointer to a previous commit and can change the Staging Area and Working Directory depending on the option used.

### 1. `git reset <commit_id>` or `git reset --mixed HEAD~1`

- Moves HEAD to the previous commit.
- Keeps your file changes in the **Working Directory**.
- Unstages the changes (Staging Area is cleaned).

```bash
git reset HEAD~1
# or
git reset --mixed HEAD~1
# or
git reset <commit_hash>
```

**Result:**  
Commit C2 is removed from history (locally).  
Changes from C2 are still present in your files (unstaged).

---

### 2. `git reset --soft HEAD~1`

- Moves HEAD to the previous commit.
- **Keeps the changes in the Staging Area** (still staged).
- Working Directory remains the same.

```bash
git reset --soft HEAD~1
```

**Result:**  
Commit C2 is removed.  
All changes from C2 are still staged and ready to commit again.

**Use case:** When you want to edit the commit message or combine commits.

---

### 3. `git reset --mixed HEAD~1` (Default)

- Same as `git reset HEAD~1`
- Moves HEAD back.
- Changes become **unstaged**.

```bash
git reset --mixed HEAD~1
# or simply
git reset HEAD~1
```

---

### 4. `git reset --hard HEAD~1`

- Moves HEAD to the previous commit.
- **Discards** the changes from the Staging Area **and** Working Directory.
- The changes are **permanently lost** (unless already pushed and recoverable by other means).

```bash
git reset --hard HEAD~1
```

**Warning:**  
This command is powerful and dangerous.  
Use it only when you are 100% sure you want to throw away the changes.

---

### Comparison Table – git reset options

| Option | Moves HEAD? | Staging Area | Working Directory | Changes Kept? |
|------------------|-------------|----------------------|-----------------------|---------------------|
| `--soft` | Yes | Changes remain staged | Unchanged | Yes (staged) |
| `--mixed` (default) | Yes | Changes become unstaged | Unchanged | Yes (unstaged) |
| `--hard` | Yes | Cleared | Cleared | **No** (lost) |

---

## 4. Understanding HEAD

| Reference | Meaning |
|-----------|---------|
| `HEAD` | Current commit (latest) |
| `HEAD~1` | One commit before current |
| `HEAD~2` | Two commits before current |
| `HEAD~3` | Three commits before current |

You can also use the full commit hash instead of `HEAD~1`.

---

## 5. git revert – Introduction

### What is `git revert`?

`git revert` creates a **new commit** that undoes the changes of a previous commit.  
It does **not** remove history. It adds a new commit that reverses the effect.

### Visual Example

```text
Before:
C0 → C1 → C2 (HEAD)

After git revert C2:
C0 → C1 → C2 → C3 (revert of C2) (HEAD)
```

- History remains safe and clean for collaboration.
- Preferred when the commits are already pushed to a shared repository (GitHub).

### Basic Command

```bash
git revert <commit_hash>
# or
git revert HEAD
```

Git will open an editor asking for a commit message for the revert commit.

---

## 6. reset vs revert – Quick Difference

| Point | `git reset` | `git revert` |
|----------------------|--------------------------------------|----------------------------------------|
| Changes history | Yes (moves HEAD backward) | No (adds a new commit) |
| Safe for shared branches | Risky (especially `--hard`) | Safe |
| Changes lost? | Possible with `--hard` | No |
| Best used when | Local commits not yet pushed | Commits already pushed / shared |

**Rule of thumb taught in class:**
- Use **reset** for local experiments and fixing recent commits.
- Use **revert** when working with others or when the commit is already on GitHub.

---

## 7. Important Warnings

- `git reset --hard` permanently discards changes. Use with extreme care.
- Avoid `git reset --hard` on public/shared branches.
- Prefer `git revert` when the commit is already pushed.
- Always run `git status` and `git log --oneline` before and after using these commands.

---

## 8. Quick Revision Cheat Sheet

| Command | Purpose |
|--------------------------------|----------------------------------------------|
| `git log --oneline` | View commit history with short hashes |
| `git reset --soft HEAD~1` | Undo commit, keep changes staged |
| `git reset --mixed HEAD~1` | Undo commit, keep changes unstaged |
| `git reset --hard HEAD~1` | Undo commit and discard all changes |
| `git reset <commit_hash>` | Reset to a specific commit (mixed by default) |
| `git revert HEAD` | Create a new commit that undoes the last commit |
| `git revert <commit_hash>` | Create a new commit that undoes a specific commit |

---

## Key Takeaway

- **HEAD** points to the current commit. `HEAD~1` means the previous commit.
- **`--soft`** → undo commit, keep changes staged.
- **`--mixed`** → undo commit, keep changes unstaged (default).
- **`--hard`** → undo commit and **delete** the changes (dangerous).
- **`git revert`** safely undoes a commit by adding a new reverse commit.
- Prefer **revert** on shared/public branches; use **reset** carefully on local work.
