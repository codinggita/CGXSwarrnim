
# Git & GitHub Practical Exam

**Time:** 1 Hour
**Total Marks:** 50

## Part A — Basic Git Commands

### Q1. Create a Git Repository — 10 Marks

Create a new folder named `git-practical`.

Perform the following tasks:

1. Initialize the folder as a Git repository.
2. Create a file named `README.md`.
3. Add some content to the file.
4. Check the repository status.
5. Add the file to the staging area.
6. Commit the changes with the message:
   `Initial commit`
7. Display the commit history.

**Commands expected:**

```bash
git init
git status
git add
git commit
git log
```

---

## Part B — Git Workflow

### Q2. Modify and Commit Changes — 10 Marks

Continue working on the repository created in Q1.

1. Modify `README.md`.
2. Create another file named `about.txt`.
3. Check which files have changed.
4. Add all changes to the staging area.
5. Create a commit with the message:
   `Updated project files`
6. Display the commit history using both normal and one-line formats.

**Commands expected:**

```bash
git status
git add .
git commit -m "Updated project files"
git log
git log --oneline
```

---

## Part C — GitHub Repository

### Q3. Clone an Existing Repository — 10 Marks

Your instructor will provide you with a GitHub repository URL.

Perform the following:

1. Clone the repository to your computer.
2. Enter the cloned project directory.
3. Check the Git status.
4. Create a new file named `student.txt`.
5. Add your name and roll number to the file.
6. Check the status again.
7. Add the file to staging.
8. Commit the changes with the message:
   `Added student information`
9. Push the changes to GitHub.
10. Verify that the file appears in the GitHub repository.

**Commands expected:**

```bash
git clone <repository-url>
cd <repository-name>
git status
git add .
git commit -m "Added student information"
git push
```

---

# Part D — Upload a New Local Project

### Q4. Upload Local Project to GitHub — 20 Marks

You have been given a project folder named `student-management`.

The folder is **not currently a Git repository**.

Create a new GitHub repository and upload the local project to it.

Perform the following:

1. Open the project directory.
2. Initialize Git.
3. Check the Git status.
4. Add all project files.
5. Create the first commit with the message:
   `Initial project upload`
6. Connect the local repository to the GitHub repository using `origin`.
7. Rename the branch to `main`.
8. Push the project to GitHub.
9. Verify the uploaded files on GitHub.

**Commands expected:**

```bash
cd student-management

git init
git status
git add .
git commit -m "Initial project upload"

git remote add origin <github-repository-url>

git branch -M main

git push -u origin main
```

---

# 🔥 Most Important Practical Questions to Practice

Your examiner can also ask you these individually:

1. **Create a Git repository using `git init`.**
2. **How do you check the current Git status?**
3. **How do you add one file to staging?**
4. **How do you add all files to staging?**
5. **How do you create a commit?**
6. **How do you view commit history?**
7. **What is the difference between `git log` and `git log --oneline`?**
8. **Clone a GitHub repository to your computer.**
9. **Make a change and push it to GitHub.**
10. **Create a new GitHub repository and upload an existing local project.**
11. **How do you connect a local repository to GitHub?**
12. **How do you rename the current branch to `main`?**
13. **What does `git push -u origin main` do?**
14. **How do you check whether a remote repository is configured?**
15. **What is the purpose of `origin`?**

### ⭐ Commands you should definitely memorize

```bash
git init
git status
git add .
git add <filename>
git commit -m "message"
git log
git log --oneline
git clone <URL>
git remote add origin <URL>
git branch -M main
git push
git push -u origin main
```

