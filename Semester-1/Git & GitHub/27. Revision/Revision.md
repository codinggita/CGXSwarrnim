# Day 27 – Git & GitHub Revision Question Bank

### Part 1: Foundations — Modules 1–3

1. Why do we need a Version Control System?
2. What are the three types of Version Control Systems?
3. Which type of VCS is Git?
4. Why is Git suitable for team projects?
5. What is the difference between Git and GitHub?
6. Can we use Git without GitHub? Can we use GitHub without Git?
7. What is the difference between a local repository and a remote repository?
8. What is the difference between CLI and GUI?
9. Which command verifies that Git is installed?
10. Which command shows the current folder in Git Bash?
11. Which command lists all files, including hidden files, in long format?
12. Which commands create a folder named `project` and enter it?
13. Which command creates an empty file named `index.html`?
14. Which command displays the content of a file named `notes.txt`?
15. Which command moves one level up from the current directory?

### Part 2: Configuration and Basic Workflow — Modules 4–6

16. Why do we configure Git before committing?
17. Write the commands to set the global Git user name and email.
18. How can you verify your Git configuration?
19. Does setting `user.name` and `user.email` log you into GitHub?
20. What is the difference between Git configuration, GitHub authentication, and permission?
21. What is a staging area?
22. What is the complete Git workflow from working directory to GitHub?
23. What does `git status` show?
24. What is the difference between `git add index.html` and `git add .`?
25. Does `git commit` upload code to GitHub?
26. Write a good commit message for adding a login page.
27. Why should commit messages such as `update`, `done`, or `test` be avoided?
28. What does `git log` display?
29. What does `git log --oneline` display?
30. What does `git remote -v` show?
31. What does `origin` mean in the command `git push origin main`?
32. What does the `-u` flag do in `git push -u origin main`?
33. Which command initializes a new Git repository in an existing folder?
34. Which command connects a local repository to a GitHub repository?
35. Which command renames the current branch to `main`?

### Part 3: Branching, Merge and Pull Requests — Modules 7–11

36. What is a branch?
37. Why should we avoid working directly on `main`?
38. What is a feature branch?
39. Write the command to create and switch to a branch named `feature/login`.
40. Write the older alternative command to create and switch to `feature/login`.
41. Which command lists all local branches?
42. How can you identify the current branch in the output of `git branch`?
43. Which command switches to an existing branch named `feature/about`?
44. Which branch must you be on before merging `feature/about` into `main`?
45. Write the command to merge `feature/about` into `main`.
46. What is the difference between `git branch -d` and `git branch -D`?
47. What is the difference between clone and fork?
48. When should you use a fork?
49. What is a Pull Request?
50. In a Pull Request, what are the base branch and compare branch?
51. A reviewer requests changes on your PR. Should you open a new PR or push changes to the same branch?
52. After a PR is merged on GitHub, why must you update local `main`?
53. Which command updates local `main` after a PR merge?
54. What is the difference between `git fetch` and `git pull`?
55. What does `git pull` combine?
56. What is the correct local branch workflow from creating a branch to deleting it?
57. What is the correct Pull Request workflow from branch creation to cleanup?
58. What is the difference between a local merge and a GitHub PR merge?
59. Why is a Pull Request considered safer for team projects?
60. Which command deletes a remote feature branch after it has been merged?

### Part 4: Conflicts and Repository Hygiene — Modules 12, 13, 15

61. When does a merge conflict occur?
62. What do the conflict markers `<<<<<<<`, `=======`, and `>>>>>>>` represent?
63. What must you do after resolving a merge conflict?
64. What is a modify/delete conflict?
65. How can you resolve a modify/delete conflict locally?
66. What is the difference between `git diff` and `git diff --staged`?
67. What does `git restore <file>` do?
68. What does `git restore --staged <file>` do?
69. Does `git restore` work on an untracked file? Why or why not?
70. What is the difference between `rm`, `git rm`, and `git rm --cached`?
71. Which command should you use if `.env` was accidentally committed but must remain on your computer?
72. Why should `.env` be added to `.gitignore`?
73. Why should `node_modules/` be added to `.gitignore`?
74. Should `.gitignore` be added inside `.gitignore`? Why or why not?
75. What happens if conflict markers are left in a file before committing?
76. After resolving a conflict during `git pull`, which commands complete the process?
77. What is the purpose of a `.gitignore` file?
78. Write three items that should commonly be added to `.gitignore`.
79. What does a clean working tree mean in `git status`?
80. What is the difference between an untracked file and a modified tracked file?

### Part 5: Undo, Recovery, Stash and Tags — Modules 16–20

81. What is `HEAD`?
82. What do `HEAD~1` and `HEAD~2` mean?
83. What does `git reset` do?
84. What is the difference between `git reset --soft`, `--mixed`, and `--hard`?
85. Which reset option is most dangerous, and why?
86. What is the difference between `git reset` and `git revert`?
87. Which command creates a revert commit for commit `abc1234`?
88. Why is `git revert` safer than `git reset` on a shared branch?
89. You accidentally reset away a commit. Which command helps you find it?
90. How can you recover a commit found through `git reflog`?
91. What is `git stash` used for?
92. Write the command to stash current tracked changes.
93. Which command lists all saved stashes?
94. How do you reapply the latest stash without removing it from the stash list?
95. How do you reapply and remove the latest stash?
96. What is a Git tag?
97. Write a command to create a lightweight tag named `v1.0.0`.
98. In semantic version `v2.4.1`, identify the major, minor, and patch numbers.
99. What is a GitHub Release?
100. What is the difference between a Git tag and a GitHub Release?

### Part 6: Rebase, Cherry-Pick and Collaboration — Modules 21–25

101. What does `git merge` do?
102. What does `git rebase` do?
103. What is the difference between merge and rebase in the resulting history?
104. When should you avoid rebasing commits?
105. What is `git cherry-pick` used for?
106. Write a command to cherry-pick commit `abc1234`.
107. What is a GitHub Issue?
108. What is a GitHub milestone?
109. What is a GitHub Project board?
110. What are the typical columns in a GitHub Project board?
111. What is the professional team workflow from Issue to Done?
112. What does `Closes #1` do in a Pull Request description?
113. You do not have write access to an open-source repository. What is the correct contribution workflow?
114. What is the first GitHub action you should take before contributing to someone else’s repository?
115. Why should each issue or feature have its own branch?
116. Why should feature branches start from an updated `main`?
117. What should a reviewer check while reviewing a Pull Request?
118. What should you do after receiving review comments on a PR?
119. What should you do after a PR is merged and before deleting the local feature branch?
120. Why should you never force-push to `main` or another shared branch?

### Rapid-Fire Questions

121. Git is a ______ version control system.
122. GitHub is a ______ platform.
123. Command to check Git version.
124. Command to show the current directory.
125. Command to list hidden files.
126. Command to set the global user email.
127. Command to initialize a repository.
128. Command to check repository status.
129. Command to stage all changes.
130. Command to save a local snapshot.
131. Command to upload commits to GitHub.
132. Command to download and merge remote changes.
133. Command to create and switch to a new branch.
134. Command to merge a feature branch.
135. Command to safely delete a merged local branch.
136. Command to see unstaged changes.
137. Command to unstage a file.
138. Command to stop tracking a file but keep it locally.
139. Command to temporarily save uncommitted work.
140. Command to reverse one commit safely.

### Scenario-Based Questions

141. You created a project locally, but it is not yet a Git repository. Write the complete commands to upload it to GitHub for the first time.

142. You are given an existing GitHub repository. Write the complete commands to clone it, make a change, commit it, and push it back to GitHub.

143. Your team is building an e-commerce website. You are assigned the Cart Page issue. Write the complete workflow from creating a branch to opening a Pull Request.

144. A teammate changed the same line in `list.txt` that you changed in your feature branch. What problem may occur, and how would you resolve it?

145. You are working on a feature but need to switch branches urgently without committing incomplete work. Which Git feature should you use, and write the commands to save and later restore the work.

146. You accidentally committed a `.env` file containing database credentials. Write the steps to stop tracking it while keeping it on your computer.

147. Your local `main` and remote `main` both changed the same file. You run `git pull origin main` and receive a conflict. What steps should you follow?

148. You need to add only one specific bug-fix commit from another branch into your current branch. Which command should you use?

149. Your project has reached version 1.0.0. Write the commands to create a tag and push it to GitHub.

150. You are contributing to an open-source project without write access. Explain the complete fork-based contribution workflow.
