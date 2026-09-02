# git restore • git restore --staged • rm vs git rm vs git rm --cached • .gitignore

---

## Learning Goals

- Understand how `git restore` and```markdown
# Day 15 – Student Notes

**git restore • git restore --staged • rm vs git rm vs git rm --cached • .gitignore**

---

## Learning Goals

- Understand how `git restore` and `git restore --staged` work.
- Know when `git restore` works and when it does not (untracked files).
- Understand the difference between normal `rm`, `git rm`, and `git rm --cached`.
- Learn how to recover a deleted tracked file using `git restore`.
- Learn how to stop tracking a file while keeping it locally using `git rm --cached`.
- Create and use a `.gitignore` file properly.
- Understand why we ignore `node_modules` and `.env`.
- Know that `.gitignore` itself should **not** be added inside `.gitignore`.

---

## 1. git restore and git restore --staged

### What is `git restore`?

`git restore` is used to **discard changes** in the working directory or to **unstage** files.

| Command | Purpose |
| ----------------------------- | ---------------------------------------------------------------------------- |
| `git restore <file>` | Discard changes in the working directory (restore to last committed version) |
| `git restore --staged <file>` | Unstage a file (move it from Staging Area back to Working Directory) |

---

### Example with `about.txt`

#### Case 1: Untracked file

1. Create a new file `about.txt` (Git does not track it yet).
2. Check status:
```bash
git status
```
→ Shows `about.txt` under **Untracked files**.

3. Try:
```bash
git restore about.txt
```
→ **Does not work**, because the file is untracked.  
Git has no previous version of this file to restore.

4. Try:
```bash
git diff
```
→ Also shows nothing useful for untracked files.

**Key Point:**  
`git restore` and `git diff` work only on **tracked** files (files that Git already knows).

---

#### Case 2: Staging and Unstaging

1. Stage the file:
```bash
git add about.txt
```
2. Check status → file is now in **Changes to be committed** (Staging Area).

3. Unstage it (move back to Working Directory):
```bash
git restore --staged about.txt
```
4. Check status again → file is back under **Untracked files** or **Changes not staged**.

**Flow:**
```text
Working Directory → git add → Staging Area
Staging Area → git restore --staged → Working Directory
```

---

## 2. rm vs git rm vs git rm --cached

### Normal `rm` (system delete)

```bash
rm about.txt
git status
```

- The file is deleted from the folder.
- Git shows it as **deleted** under “Changes not staged for commit”.
- The deletion is **not staged** yet.

You can recover the file easily:
```bash
git restore about.txt
```
→ File comes back from the last commit.

---

### `git rm` (Git-aware delete)

```bash
git rm about.txt
git status
```

- The file is deleted **and** the deletion is **staged** automatically.
- Git shows it under “Changes to be committed”.

To complete the removal you still need to commit:
```bash
git commit -m "Remove about.txt"
```

---

### `git rm --cached` (Untrack but keep the file)

```bash
git rm --cached .env
git status
```

- Removes the file from Git tracking (index/staging area).
- The file **stays on your computer**.
- Extremely useful when you accidentally committed a file that should be ignored (for example `.env`).

**Common workflow (when `.env` was committed by mistake):**

```bash
# 1. Stop tracking the file (keep it locally)
git rm --cached .env

# 2. Make sure .env is listed in .gitignore

# 3. Commit the change
git add .gitignore
git commit -m "Stop tracking .env and update .gitignore"
git push
```

---

### Comparison: `rm` vs `git rm` vs `git rm --cached`

| Point | `rm <file>` | `git rm <file>` | `git rm --cached <file>` |
| ------------------- | ----------------------- | -------------------------------- | -------------------------------- |
| Deletes from working directory | Yes | Yes | **No** |
| Stages the change | No | Yes | Yes (untracks the file) |
| File remains on disk | No | No | **Yes** |
| Typical use | Casual delete | Intentionally remove a tracked file from the repository | Stop tracking a file (e.g. `.env`) but keep it locally |

**Recommendation:**
- Use `git rm` when you want to permanently remove a tracked file from the project.
- Use `git rm --cached` when you want Git to stop tracking a file but still need the file on your machine.

---

## 3. .gitignore

### What is `.gitignore`?

A special file that tells Git **which files or folders to ignore** (not track).

### Common things we ignore

| Item | Why we ignore it |
| ---------------------------------- | -------------------------------------------------------------------------------------------- |
| `node_modules/` | Very large folder. Contains installed packages. Can be recreated with `npm install`. |
| `.env` | Contains **secrets** (passwords, API keys, database URIs). Should never be pushed to GitHub. |
| log files, build folders, OS files | Not needed in the repository |

---

### Example – Creating `.gitignore`

Create a file named `.gitignore` in the root of your project and write:

```gitignore
# Dependencies
node_modules/

# Environment variables / secrets
.env

# Optional extras
*.log
.DS_Store
```

### Sample `.env` file (DO NOT push this)

```env
MONGO_URI=mongodb+srv://username:password@cluster.mongodb.net/myDB
JWT_SECRET_KEY=mySuperSecretKey12345
```

If you accidentally commit `.env`, anyone with access to your repository can see your secrets.  
In that case use `git rm --cached .env` as shown above.

---

### Importance of these files

| File / Folder | Importance |
| --------------- | ---------------------------------------------------------------------------------- |
| `node_modules/` | Contains all installed packages. Ignoring it keeps the repository small and clean. |
| `.env` | Stores sensitive data. Must be ignored to keep secrets safe. |
| `.gitignore` | Controls what Git should ignore. Essential for clean and secure repositories. |

---

### Important Rule about `.gitignore`

**Do NOT add `.gitignore` inside `.gitignore`.**

- `.gitignore` itself should be **tracked** by Git.
- The whole team needs the same ignore rules.
- Adding `.gitignore` to itself is a bad practice.

---

## 4. Useful Commands Recap

```bash
# See current status
git status

# See unstaged changes
git diff

# See staged changes
git diff --staged
# or
git diff --cached

# Unstage a file
git restore --staged about.txt

# Discard changes in working directory (tracked files only)
git restore about.txt

# Delete a tracked file and stage the deletion
git rm about.txt

# Stop tracking a file but keep it locally
git rm --cached .env

# Recover a deleted tracked file (if not committed yet)
git restore about.txt
```

---

## 5. Quick Revision Cheat Sheet

| Command | Purpose |
| ----------------------------- | ------------------------------------------ |
| `git restore <file>` | Discard changes in working directory |
| `git restore --staged <file>` | Unstage a file |
| `rm <file>` | Delete file (system level, not staged) |
| `git rm <file>` | Delete file and stage the deletion |
| `git rm --cached <file>` | Untrack file but keep it on disk |
| `git status` | Check what is tracked / staged / untracked |
| `git diff` | Show unstaged changes |
| `git diff --staged` | Show staged changes |
| Create `.gitignore` | Tell Git which files/folders to ignore |

---

## Key Takeaway

- **`git restore`** → discard changes or unstage files (works only on tracked files).
- **`git restore --staged`** → move file from Staging Area back to Working Directory.
- **`rm`** just deletes the file; **`git rm`** deletes + stages the deletion.
- **`git rm --cached`** stops tracking a file but keeps it on your computer (very useful for `.env`).
- Always use **`.gitignore`** for `node_modules/` and `.env`.
- Never put secrets in the repository.
- Never add `.gitignore` to `.gitignore`.
