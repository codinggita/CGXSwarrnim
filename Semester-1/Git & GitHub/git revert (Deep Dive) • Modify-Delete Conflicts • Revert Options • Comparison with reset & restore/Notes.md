
# git revert (Deep Dive) • Modify/Delete Conflicts • Revert Options • Comparison with reset & restore

---

## Learning Goals

- Understand the definition and working of `git revert`.
- See how `git revert` creates a **new commit** that undoes a previous commit.
- Handle the default editor (VS Code or Vim) when reverting.
- Resolve a **Modify/Delete conflict** that can appear during revert.
- Use important revert options: `--no-edit`, `--no-commit`, `--continue`, `--abort`, `--quit`.
- Clearly understand the difference between `git restore`, `git reset`, and `git revert`.

---

## 1. What is `git revert`? (Definition & Explanation)

### Definition
`git revert` is a safe command that **undoes the changes** introduced by a previous commit by creating a **new commit**.  
It does **not** delete or rewrite existing history.

### Simple Explanation
- Imagine you made a commit that added wrong code.
- Instead of removing that commit from history, Git creates a **new opposite commit** that cancels those changes.
- The old commit still remains in the history (this makes it safe for shared branches).

### Key Points
- History is **never deleted**.
- A new commit is always created.
- Safe to use even after pushing to GitHub.
- Opposite of `git reset` (which moves history backward).

---

## 2. Visual Commit History (Starting Point)

```text
C0  – Initial commit (README.md added)
 │
C1  – "1st commit"   → created index.html with <h1>Hi Team</h1>
 │
C2  – "2nd commit"   → added <h1>Hello students</h1>
 ↑
HEAD (you are here)
```

---

## 3. Example 1 – Revert the Latest Commit (C2)

**Goal:** Undo the changes made in C2.

```bash
git log --oneline                    # copy commit hash of C2
git revert <commit_hash_of_C2>
```

### Visual – Before & After

```text
BEFORE:
C0 → C1 → C2 (HEAD)

AFTER:
C0 → C1 → C2 → C3 (C2') (HEAD)
                 ↑
           This is the revert commit
           (removes “Hello students”)
```

### What happens?
- Git creates a **new commit C3** (also called C2').
- C3 is the opposite of C2.
- The line `<h1>Hello students</h1>` is removed from `index.html`.

### Editor opens
- Most students see the **VS Code** commit message editor.
- Some students see **Vim**.

**If Vim opens:**
1. Press `Esc`
2. Type `:wq`
3. Press `Enter`

Default commit message: `Revert "2nd commit"`

Verify:
```bash
git log --oneline
```

---

## 4. Example 2 – Revert an Older Commit (C1) → Modify/Delete Conflict

**Goal:** Undo C1 while we are already at C3.

```bash
git log --oneline
git revert <commit_hash_of_C1>
```

### Visual – Conflict Situation

```text
Current history:
C0 → C1 → C2 → C3 (HEAD)

Trying to revert C1:
Git wants to delete index.html (because C1 created it)
But index.html still exists in C3
→ Modify/Delete Conflict
```

### Why conflict happens?
- C1 originally **created** `index.html`.
- Reverting C1 means Git wants to **delete** `index.html`.
- Current commit (C3) still has the file → conflict.

**Note:** In Modify/Delete conflicts you usually **do not** see:
```
<<<<<<< 
=======
>>>>>>>
```

### How to resolve

**Option A – Delete the file** (to fully undo C1)
```bash
rm index.html
git add .
git revert --continue
```

**Option B – Keep the file** with your required content
```bash
git add .
git revert --continue
```

### Visual – After resolving

```text
C0 → C1 → C2 → C3 → C4 (C1') (HEAD)
                     ↑
               Revert of C1
```

---

## 5. Example 3 – Revert C0 (Remove README)

```bash
git revert <commit_hash_of_C0>
```

### Visual

```text
BEFORE:
C0 → C1 → C2 → C3 → C4 (HEAD)

AFTER:
C0 → C1 → C2 → C3 → C4 → C5 (C0') (HEAD)
                          ↑
                    README.md deleted
```

- Successfully removes `README.md`.
- Creates **C5** (complement of C0).

---

## 6. Example 4 – Revert the Revert (Bring README back)

```bash
git revert <commit_hash_of_C5>
```

### Visual

```text
BEFORE:
C0 → C1 → C2 → C3 → C4 → C5 (HEAD)

AFTER:
C0 → C1 → C2 → C3 → C4 → C5 → C6 (C5') (HEAD)
                               ↑
                         README.md restored
```

This shows that you can **revert a revert**.

---

## 7. Important Revert Options with Simple Examples

### 1. `git revert --no-edit <commit_id>`

**Meaning:** Revert + use default commit message (no editor opens).

**Example:**
```bash
git revert --no-edit HEAD
```

**When to use:** When the default message `Revert "..."` is enough.

---

### 2. `git revert --no-commit <commit_id>`

**Meaning:** Apply the reverse changes but **do not create a commit** yet.

**Example:**
```bash
git revert --no-commit <commit_hash_of_C2>
git status
```
You can review the changes and commit later manually.

**When to use:** When you want to revert several commits and combine them into one commit.

---

### 3. `git revert --continue`

**Meaning:** Continue the revert after you resolve a conflict.

**Example:**
```bash
git add .
git revert --continue
```

---

### 4. `git revert --abort`

**Meaning:** Cancel the entire revert and return to the previous state.

**Example:**
```bash
git revert --abort
```

**When to use:** When you change your mind or the conflict is too difficult.

---

### 5. `git revert --quit`

**Meaning:** Stop the revert process but **keep** the current changes in the working directory.

**Example:**
```bash
git revert --quit
```

**Difference from `--abort`:**  
- `--abort` → fully cancels and restores original state.  
- `--quit` → stops revert but leaves file changes as they are.

---

## 8. Editors – Quick Info

| Editor | How it appears | How to save & exit |
|--------|----------------|--------------------|
| VS Code | Graphical editor | Save + close / confirm |
| Vim | Terminal editor | `Esc` → `:wq` → `Enter` |
| Nano | Simple terminal editor | `Ctrl + O` then `Ctrl + X` |

**Change default editor (optional):**
```bash
git config --global core.editor "code --wait"   # VS Code
git config --global core.editor "vim"           # Vim
git config --global core.editor "nano"          # Nano
```

---

## 9. Detailed Comparison: git restore vs git reset vs git revert

| Feature | `git restore` | `git reset` | `git revert` |
|-----------------------------|----------------------------------------------|-----------------------------------------------|-----------------------------------------------|
| Main purpose | Discard or unstage file changes | Move HEAD to a previous commit | Create a new commit that undoes a previous commit |
| Changes history? | No | Yes (rewrites history) | No (history stays safe) |
| Creates new commit? | No | No | Yes |
| Safe on public/shared branch? | Yes | Risky (especially `--hard`) | Yes (recommended) |
| Can lose work? | Only uncommitted changes | Yes (with `--hard`) | No |
| Common use case | Undo uncommitted changes | Fix recent local commits | Undo a commit that is already pushed |
| Typical commands | `git restore file.txt`<br>`git restore --staged file.txt` | `git reset --soft/--mixed/--hard HEAD~1` | `git revert HEAD`<br>`git revert <commit_id>` |
| Conflict possible? | No | Rare | Yes (especially Modify/Delete) |

### Simple way to remember
- **`git restore`** → Fix my current files (uncommitted changes).
- **`git reset`** → Move my branch pointer backward (careful!).
- **`git revert`** → Safely undo a commit by adding an opposite commit.

---

## 10. Key Points to Remember

- `git revert` **never deletes** history — it only adds new commits.
- Reverting a commit that added a file can cause a **Modify/Delete conflict**.
- In Modify/Delete conflicts there are usually **no** `<<<<<<<` markers.
- After fixing a conflict always run `git add` + `git revert --continue`.
- Use `git revert --abort` if you want to cancel the whole revert.
- Prefer `git revert` over `git reset` when the commit is already pushed.

---

## 11. Quick Revision Cheat Sheet

```bash
git log --oneline                     # find commit hashes

git revert <commit_id>                # normal revert (opens editor)
git revert --no-edit <commit_id>      # revert with default message
git revert --no-commit <commit_id>    # apply reverse changes, no commit

# After conflict:
git add .
git revert --continue

# Cancel:
git revert --abort
git revert --quit
```

---

## Key Takeaway

- **`git revert`** = safe undo (creates opposite commit).
- History is preserved — perfect for shared branches.
- Older reverts can produce **Modify/Delete conflicts**.
- Resolve conflict → `git add` → `git revert --continue`.
- Useful flags: `--no-edit`, `--no-commit`, `--continue`, `--abort`, `--quit`.
- **restore** = fix files, **reset** = move history, **revert** = safe undo.
