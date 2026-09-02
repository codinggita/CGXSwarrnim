
#  Assignments-git reset (--soft, --mixed, --hard) • HEAD • git revert**

---

## Instructions

- Use your assignment repository (recommended name: CodingGita_assignments repo).
- Complete all 4 assignments in order.
- Take screenshots where asked.
- Submit the **GitHub repository link** along with the required screenshots.

**Before you start:**  
Make sure your working directory is clean (`git status`).  
Run `git log --oneline` frequently so you can see the commit history clearly.

---

## Assignment 1 – Understanding HEAD and Basic Reset (Easy)

**Goal:** Practice viewing history and using a simple mixed reset.

1. Create or open your practice repository.
2. Make three simple commits (you can create/edit a file called `notes.txt`):
   - Commit 1: Add some text → commit message `"First note"`
   - Commit 2: Add more text → commit message `"Second note"`
   - Commit 3: Add more text → commit message `"Third note"`
3. Run:
   ```bash
   git log --oneline
   ```
4. Reset to the previous commit using:
   ```bash
   git reset HEAD~1
   ```
5. Run `git log --oneline` and `git status` again.
6. Observe what happened to the latest commit and the file changes.

**Submit:**
- Screenshot of `git log --oneline` **before** reset
- Screenshot of `git log --oneline` and `git status` **after** reset
- Repository link

---

## Assignment 2 – Difference between --soft, --mixed and --hard (Medium)

**Goal:** Clearly see how the three reset modes behave differently.

1. Create a new file `demo.txt` and make **two commits** on it.
2. Perform the following one by one (create fresh commits each time if needed):

   **A. Soft Reset**
   ```bash
   git reset --soft HEAD~1
   git status
   ```

   **B. Mixed Reset**
   ```bash
   git reset --mixed HEAD~1
   git status
   ```

   **C. Hard Reset**
   ```bash
   git reset --hard HEAD~1
   git status
   ```

3. Create a file named `reset-comparison.txt` and write in your own words:
   - What is the difference between `--soft`, `--mixed`, and `--hard`?
   - Which one keeps changes staged?
   - Which one discards the changes completely?
   - When should you avoid `--hard`?

**Submit:**
- Screenshots of `git status` after each type of reset (`--soft`, `--mixed`, `--hard`)
- Content of `reset-comparison.txt`
- Repository link

---

## Assignment 3 – Practice git revert (Medium)

**Goal:** Safely undo a commit using `git revert` instead of reset.

1. Make sure you have at least 2–3 commits on `main`.
2. Choose the latest commit and revert it:
   ```bash
   git revert HEAD
   ```
   (Save the commit message that Git opens)
3. Run:
   ```bash
   git log --oneline
   ```
4. Observe that a **new commit** was created (the history was not deleted).
5. Create a file `revert-explanation.txt` and answer:
   - What does `git revert` do?
   - How is it different from `git reset`?
   - When is `git revert` safer than `git reset`?

**Submit:**
- Screenshot of `git log --oneline` showing the revert commit
- Content of `revert-explanation.txt`
- Repository link

---

## Assignment 4 – Combined Practice + Safety Rules (Hard)

**Goal:** Combine reset and revert knowledge and demonstrate safe practices.

1. Create a small project flow:
   - Make 3 commits on a file called `project.txt`.
2. Use `git reset --soft HEAD~1` and then create a new improved commit.
3. Later, use `git revert` on one commit and show that history is preserved.
4. Create a final file named `day16-safety.txt` and write:
   - When should you use `git reset --soft`?
   - When should you use `git reset --hard`? (and why be careful)
   - When should you prefer `git revert`?
   - What do `HEAD`, `HEAD~1`, and `HEAD~2` mean?

**Submit:**
- Screenshot of final `git log --oneline`
- Content of `day16-safety.txt`
- Repository link

---

## Submission Checklist

| # | Item | Required? |
|---|------|-----------|
| 1 | Assignment 1 – before/after reset screenshots | Yes |
| 2 | Assignment 2 – three reset mode screenshots + comparison file | Yes |
| 3 | Assignment 3 – revert screenshot + explanation file | Yes |
| 4 | Assignment 4 – final log + safety file | Yes |
| — | GitHub repository link | Yes |

**Important Notes:**
- Be very careful with `git reset --hard` — it can delete your work.
- Prefer `git revert` when commits are already pushed to GitHub.
- Always check `git log --oneline` and `git status` before and after these commands.

# Deadline: 5th September, 2026
