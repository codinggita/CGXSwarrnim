
#  Assignment - git restore • git restore --staged • rm vs git rm • .gitignore

---

## Instructions

- Use your CodingGita_assignments repository.
- Complete all assignments in order.
- Take screenshots where asked.
- Submit the **GitHub repository link** along with the required screenshots.

**Before you start:** Make sure your working directory is clean (`git status`).

---

## Assignment 1 – Practice `git restore` and `git restore --staged` 

**Goal:** Understand how staging and unstaging works with `git restore`.

1. Create a new file named `profile.txt` and write 3–4 lines about your favorite programming topic.
2. Run `git status` and note that the file is **untracked**.
3. Try the command:
   ```bash
   git restore profile.txt
   ```
   Observe that it does **not** work (because the file is untracked).
4. Stage the file:
   ```bash
   git add profile.txt
   ```
5. Unstage it using:
   ```bash
   git restore --staged profile.txt
   ```
6. Run `git status` again and confirm the file is back to untracked / unstaged.
7. Now stage and commit the file properly:
   ```bash
   git add profile.txt
   git commit -m "Add profile.txt"
   ```

**Submit:**
- Screenshot of `git status` when the file was untracked
- Screenshot after using `git restore --staged`
- Repository link

---

## Assignment 2 – `rm` vs `git rm` 

**Goal:** Understand the difference between normal delete and Git delete.

1. Make sure `profile.txt` is committed on `main`.
2. Delete the file using normal system command:
   ```bash
   rm profile.txt
   ```
3. Run `git status` and observe the output.
4. Recover the file using:
   ```bash
   git restore profile.txt
   ```
5. Now delete it properly with Git:
   ```bash
   git rm profile.txt
   ```
6. Run `git status` again and observe the difference.
7. Commit the deletion:
   ```bash
   git commit -m "Remove profile.txt using git rm"
   ```
8. Create a short file named `delete-difference.txt` and write in your own words:
   - What is the difference between `rm` and `git rm`?
   - When should you use `git rm`?

**Submit:**
- Screenshots of `git status` after `rm` and after `git rm`
- Content of `delete-difference.txt`
- Repository link

---

## Assignment 3 – Create and Use `.gitignore`

**Goal:** Properly ignore sensitive and unnecessary files.

1. Create a file named `config.env` with sample secret data:
   ```env
   DB_PASSWORD=SuperSecretPass999
   API_KEY=sk-test-abc123xyz789
   ```
2. Create a folder named `vendor` and put any dummy file inside it (for practice).
3. Create a `.gitignore` file and add:
   ```gitignore
   vendor/
   config.env
   ```
4. Run `git status` and confirm that `config.env` and `vendor/` are **not** showing as untracked files.
5. Add and commit the `.gitignore` file:
   ```bash
   git add .gitignore
   git commit -m "Add .gitignore to ignore vendor and config.env"
   git push origin main
   ```
6. Create a file named `why-gitignore.txt` and answer:
   - Why should we ignore folders like `vendor` or `node_modules`?
   - Why should we ignore files like `config.env` or `.env`?
   - Why should we **not** add `.gitignore` inside `.gitignore`?

**Submit:**
- Screenshot of `git status` showing that `config.env` and `vendor` are ignored
- Content of `why-gitignore.txt`
- Repository link (make sure `config.env` is **not** visible on GitHub)

---

## Bonus Assignment(Optional)

1. Modify a tracked file (create one if needed) and use `git restore <filename>` to discard the changes.
2. Stage a file and then unstage it using `git restore --staged`.
3. Take screenshots of both actions.

**Submit (optional):** Screenshots of both restore operations.

---

## Submission Checklist

| # | Item | Required? |
|---|------|-----------|
| 1 | Assignment 1 – screenshots of restore practice | Yes |
| 2 | Assignment 2 – `rm` vs `git rm` screenshots + explanation file | Yes |
| 3 | Assignment 3 – `.gitignore` working + explanation file | Yes |
| 4 | Bonus restore practice assignment| No (optional) |
| — | GitHub repository link | Yes |

**Important:**  
Make sure `config.env` is **not** pushed to GitHub.  
Your `.gitignore` file **should** be present in the repository.

---

### Deadline: 31st August, 2026.
