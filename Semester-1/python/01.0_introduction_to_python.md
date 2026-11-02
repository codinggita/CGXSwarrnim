# 2.1 Introduction to Python

## Objective

After completing this topic, you should be able to understand:

- What is Python?
- Python use cases
- What is a Python interpreter?
- Python execution model
- Python files
- How to run Python programs
- Comments in Python
- Basic Python syntax
- Code readability
- Python naming conventions

> **Prerequisite:** You should understand the basic concepts of program, programming, and programming languages from the previous topic. No advanced Python knowledge is required.

---

## 1. What Is Python?

**Python** is a high-level programming language used to write instructions for computers.

Python was designed with a strong focus on readability and simplicity, which makes it suitable for beginners as well as professional developers.

In simple words:

> **Python is a programming language that allows us to write instructions for a computer in a relatively simple and readable way.**

### Why Is Python Popular?

Python is popular because:

- Its syntax is relatively easy to read.
- It is beginner-friendly.
- It can be used in many different areas.
- It has a large collection of libraries and tools.
- It is widely used in both education and industry.
- The same language can be used for many different types of projects.

### A Very Simple Python Example

```python
print("Hello, Python!")
```

This is a small Python program that asks Python to display the text:

```text
Hello, Python!
```

For now, focus only on the idea that Python allows us to express instructions in a readable form.

We will study `print()` properly in the upcoming topics.

---

## 2. Python Use Cases

Python is a general-purpose programming language. This means it can be used for many different types of tasks.

### 2.1 Web Development

Python can be used to create websites and web applications.

Popular Python frameworks include:

- Django
- Flask
- FastAPI

For example, a company can use Python to build the software that runs behind a website.

---

### 2.2 Artificial Intelligence

Python is widely used in Artificial Intelligence (AI).

It is used for areas such as:

- Natural language processing
- Computer vision
- Generative AI
- Intelligent applications

---

### 2.3 Machine Learning

Python is widely used to develop machine learning applications.

Popular libraries and frameworks include:

- NumPy
- Pandas
- Scikit-learn
- TensorFlow
- PyTorch

---

### 2.4 Data Science

Python is commonly used for:

- Data analysis
- Data processing
- Data visualization
- Statistical work
- Building predictive models

---

### 2.5 Automation

Python can be used to automate repetitive tasks.

Examples include:

- Processing files
- Generating reports
- Organizing data
- Performing repeated calculations
- Automating routine computer tasks

---

### 2.6 Game Development

Python can also be used to create games and to learn game programming.

One popular Python library for game development is:

```text
Pygame
```

---

### 2.7 Cybersecurity

Python can be useful in cybersecurity for tasks such as:

- Security automation
- Network analysis
- Log analysis
- Security testing
- Building security tools

---

### 2.8 Cloud and DevOps

Python is also used for:

- Automation
- Cloud infrastructure management
- Data processing
- Server-side applications
- DevOps workflows

---

## 3. What Is a Python Interpreter?

A **Python interpreter** is a program that reads and processes Python code so that the computer can execute the instructions.

In simple words:

> **The Python interpreter acts as a bridge between the Python program written by the programmer and the computer's execution process.**

Suppose we have:

```python
print("Hello")
```

The programmer writes this instruction in Python.

The Python interpreter processes the Python code and makes it possible for the instruction to be executed.

### Why Do We Need an Interpreter?

The computer cannot directly execute Python source code in the same form in which a programmer writes it.

The interpreter is part of the process that takes Python code and prepares it for execution.

### Important Point

Do not think of the interpreter as the Python programming language itself.

- **Python:** The programming language.
- **Python interpreter:** The software that processes Python code.

---

## 4. Python Execution Model

The **Python execution model** explains how a Python program moves from a `.py` file to the final output on the screen.

For example, consider this file:

```python
# hello.py
print("Hello World")
```

The complete flow is shown below.

```text
hello.py
  ↓
Python Interpreter (CPython)
  ↓
Source Code
  ↓
Tokenizer and Parser (syntax check)
  ↓
Compiler
  ↓
Bytecode
  ↓
Python Virtual Machine (PVM)
  ↓
Execute print()
  ↓
Hello World
```

### Step-by-Step Execution Process

#### 1. `hello.py`

`hello.py` is a **Python source-code file**. It stores the instructions written by the programmer.

#### 2. Python Interpreter (CPython)

When we run the file, the **Python interpreter** starts. The standard and most commonly used Python interpreter is called **CPython**.

CPython reads and processes the Python program. The steps below, from reading the source code to executing `print()`, are performed by CPython.

#### 3. Source Code

The code written by the programmer is called **source code**.

```python
print("Hello World")
```

This code is easy for humans to read, but it must be processed before Python can execute it.

#### 4. Tokenizer and Parser: Syntax Check

First, CPython reads the code and checks its **syntax**. This stage is handled by the **tokenizer and parser**.

For example, this code has a syntax error because the closing bracket is missing:

```python
print("Hello World"
```

Python stops here and shows a `SyntaxError`. In this case, bytecode is not created and the program does not execute.

#### 5. Compiler

If the syntax is correct, CPython's compiler converts the source code into **bytecode**.

#### 6. Bytecode

**Bytecode** is an intermediate form of Python instructions. It is not the original source code, and it is not machine code.

Some bytecode instructions may look like `LOAD_CONST` and `CALL`. Beginners do not need to memorize these instructions.

#### 7. Python Virtual Machine (PVM)

The **Python Virtual Machine (PVM)** reads the bytecode instructions one by one and executes them.

The PVM is an internal part of CPython; it is not a separate program that we normally start ourselves.

#### 8. Execute `print()`

For the statement below, the PVM executes the `print()` function:

```python
print("Hello World")
```

The `print()` function sends the text to the terminal or output screen.

#### 9. Final Output

The final result appears on the screen:

```text
Hello World
```

### Easy Way to Remember

> **We WRITE source code → CPython CHECKS syntax → CPython CREATES bytecode → PVM RUNS it → We GET the output.**

```text
WRITE → CHECK → CREATE → RUN → OUTPUT
  ↓       ↓        ↓       ↓       ↓
Source → Syntax → Bytecode → PVM → Result
```

### Why Is This Important?

Understanding this model helps us know where an error can happen. For example, a `SyntaxError` happens before the program runs, while an error during execution happens when the PVM is running the code.

The main point to remember is:

> **CPython processes the source code, checks syntax, creates bytecode, and uses the PVM to execute it.**

---

## 5. Python Files

Python programs are commonly stored in files with the `.py` extension.

### Example

Suppose we create a Python file named:

```text
hello.py
```

The `.py` extension tells us that the file contains Python source code.

A file could contain:

```python
print("Hello, Python!")
```

### Why Are Python Files Useful?

Instead of writing a program again every time we want to use it, we can save the program in a file.

For example:

```text
calculator.py
student.py
game.py
automation.py
```

These are Python source files.

### Important Terms

| Term | Meaning |
|---|---|
| `.py` | Common file extension for Python source files |
| Python source code | Python instructions written by a programmer |
| Python file | A file containing Python source code |

---

## 6. Running Python Programs

There are several ways to run a Python program.

### Method 1: Using a Python File

Suppose we create:

```text
hello.py
```

with:

```python
print("Hello, Python!")
```

We can run this Python file using a Python installation.

A common command is:

```text
python hello.py
```

On some systems, the command may be:

```text
python3 hello.py
```

The exact command can depend on the operating system and Python installation.

---

### Method 2: Using an IDE or Code Editor

A Python program can also be written and run using software such as:

- Visual Studio Code
- PyCharm
- IDLE
- Jupyter Notebook

These tools make it easier to write, run, and manage Python programs.

---

### Method 3: Interactive Python Interpreter

Python can also be used interactively.

In an interactive environment, we can enter Python instructions and see the result immediately.

For example:

```text
>>> print("Hello")
Hello
```

The `>>>` symbol shown above represents the Python interactive prompt.

> **Note:** The interactive prompt is different from a normal `.py` source file.

---

## 7. Comments in Python

A **comment** is text written in a program for humans to understand or document the code. Python does not execute a comment as a program instruction.

Comments are useful for explaining code.

### Single-Line Comment

In Python, a single-line comment begins with `#`.

Example:

```python
# This program displays a message
print("Hello")
```

The line beginning with `#` is a comment.

Python ignores that comment during normal execution.

### Why Use Comments?

Comments can help:

- Explain what a section of code does.
- Make code easier to understand.
- Leave notes for yourself or other programmers.
- Document important information.

### Example

```python
# Display a welcome message
print("Welcome to Python!")
```

The comment tells the reader what the next instruction is intended to do.

### Important Rule

A comment should normally explain something useful.

Avoid writing unnecessary comments such as:

```python
# Print hello
print("Hello")
```

when the code is already obvious and the comment adds no useful information.

---

## 8. Basic Python Syntax

**Syntax** means the rules for writing code correctly in a programming language.

Just as a human language has rules for forming sentences, Python has rules for writing valid programs.

### Example

```python
print("Hello")
```

This follows Python's syntax rules.

If we write code in a form that Python does not understand, Python may report an error.

### Why Is Syntax Important?

Syntax helps Python understand what the programmer wants the computer to do.

A programmer must therefore follow the rules of the Python language.

---

## 9. Python Is Case-Sensitive

Python is **case-sensitive**.

This means uppercase and lowercase letters are treated as different.

For example, these are different names:

```text
name
Name
NAME
```

They should not be treated as the same thing.

This is an important Python rule to remember from the beginning.

---

## 10. Code Readability

**Code readability** means how easily a person can understand code by looking at it.

Good code should not only work correctly; it should also be easy for humans to read and understand.

### Example of Readable Code

```python
student_name = "Rahul"
student_age = 18
```

The names make the purpose of the stored information easier to understand.

### Example of Poor Readability

```python
x = "Rahul"
y = 18
```

This may work, but the names do not clearly explain what the values represent.

> **Readable code reduces confusion and makes programs easier to maintain.**

### Why Is Readability Important?

Good readability helps:

- Beginners understand code.
- Developers find mistakes more easily.
- Teams work together more effectively.
- Future changes become easier.
- Large programs remain manageable.

---

## 11. Naming Conventions

A **naming convention** is a commonly followed way of naming things in code.

Python has recommended naming styles that help make code consistent and readable.

### 11.1 Variable and Function Names

Python commonly uses **snake_case** for variable and function names.

Example:

```text
student_name
total_marks
calculate_total
```

Words are written in lowercase and separated using underscores.

---

### 11.2 Class Names

Python commonly uses **CapWords** (also called PascalCase) for class names.

Example:

```text
StudentRecord
BankAccount
StudentDetails
```

We will study classes later, so for now remember only the naming style.

---

### 11.3 Constants

Constants are commonly written using uppercase letters with underscores.

Example:

```text
MAX_SIZE
PI_VALUE
DEFAULT_TIMEOUT
```

The detailed concept of constants will be discussed later.

---

## 12. Good Naming Practices

A good name should give the reader an idea about what it represents.

### Better Names

```text
student_name
total_marks
phone_number
```

### Less Descriptive Names

```text
x
a
temp
```

Short names are not always wrong. Sometimes they are appropriate in small contexts.

However, for beginners and larger programs, meaningful names are generally easier to understand.

### Avoid Confusing Names

Do not choose names that are unnecessarily difficult to understand.

Prefer:

```text
total_price
```

over a name that gives no clue about its purpose.

---

## 13. A Small Complete Example

Here is a small example combining comments, readable code, and a Python file:

```python
# Display a welcome message
student_name = "Rahul"

print("Welcome,", student_name)
```

Suppose this code is saved in:

```text
welcome.py
```

The overall process is:

1. Create the Python file.
2. Write Python source code in the file.
3. Save the file.
4. Run the Python program.
5. Python processes the code.
6. The program produces the required result.

We will learn each individual concept in more detail in later topics.

---

## 14. Common Beginner Mistakes

### Mistake 1: Treating Python as the Interpreter

Remember:

- Python → programming language
- Python interpreter → software that processes Python code

---

### Mistake 2: Forgetting the `.py` Extension

A normal Python source file is commonly saved with:

```text
.py
```

For example:

```text
program.py
```

---

### Mistake 3: Ignoring Case

Remember that Python is case-sensitive.

These are different:

```text
student_name
Student_Name
STUDENT_NAME
```

---

### Mistake 4: Using Unclear Names

Prefer:

```text
student_name
```

instead of:

```text
x
```

when the name represents a student's name.

---

### Mistake 5: Writing Unnecessary Comments

Comments should add useful information rather than simply repeat what the code already makes obvious.

---

## 15. Quick Comparison

| Concept | Meaning |
|---|---|
| Python | A programming language |
| Interpreter | Software that processes Python code |
| Source Code | Python code written by the programmer |
| `.py` File | A common Python source file |
| Execution | The process of running the program |
| Comment | Human-readable note in code |
| Syntax | Rules for writing Python code |
| Readability | How easily humans can understand code |
| Naming Convention | Recommended style for naming code elements |

---

## 16. Key Points to Remember

1. Python is a high-level, general-purpose programming language.
2. Python is widely used in web development, AI, machine learning, data science, automation, cybersecurity, and many other areas.
3. A Python interpreter processes Python source code so that it can be executed.
4. Python programs are commonly stored in `.py` files.
5. Python programs can be run using a terminal, IDE, or interactive interpreter.
6. Comments are used to provide information for human readers.
7. Python syntax defines the rules for writing Python code.
8. Python is case-sensitive.
9. Readable code is easier to understand and maintain.
10. Meaningful names make code easier to understand.
11. `snake_case` is commonly used for variable and function names.
12. `CapWords` is commonly used for class names.
13. Uppercase names with underscores are commonly used for constants.
