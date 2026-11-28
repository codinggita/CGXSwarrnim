# 3.6 Variable Scope and Lifetime

## Learning Objectives

After completing this topic, you will be able to:

- Understand variable scope and variable lifetime.
- Identify local and global variables.
- Know where a variable can be accessed.
- Understand how long a variable remains available.
- Use the `global` keyword when a function needs to modify a global variable.

---

## 1. What Is Variable Scope?

**Variable scope** means the part of a program where a variable can be accessed or used.

In simple words:

> Scope tells us **where we can use a variable**.

Python introduces two important types of variables when learning function scope:

1. Local variables
2. Global variables

---

## 2. Local Variables

A **local variable** is a variable created inside a function. It can normally be accessed only inside that function.

### Example

```python
def show_message():
    message = "Hello, students!"
    print(message)


show_message()
```

**Output**

```text
Hello, students!
```

### How does it work?

- `message` is created inside `show_message()`.
- The function can use `message`.
- When the function is called, its code runs and prints the value.

The variable `message` is local to `show_message()`.

### Can we use a local variable outside its function?

No. A local variable cannot normally be accessed outside the function in which it was created.

```python
def show_message():
    message = "Hello, students!"
    print(message)


show_message()
print(message)
```

**Output**

```text
Hello, students!
NameError: name 'message' is not defined
```

**Why does this error occur?**

The variable `message` was created inside `show_message()`. It is not available outside that function.

### Same Variable Name in Different Functions

Two different functions can have local variables with the same name. They are separate variables.

```python
def first_function():
    number = 10
    print("First function:", number)


def second_function():
    number = 50
    print("Second function:", number)


first_function()
second_function()
```

**Output**

```text
First function: 10
Second function: 50
```

Both functions have a local variable named `number`. One does not automatically affect the other.

---

## 3. Global Variables

A **global variable** is a variable created outside all functions.

It can be accessed inside functions as well as outside functions, as long as a local variable with the same name does not take its place inside that function.

### Example

```python
college_name = "ABC College"


def show_college():
    print("College:", college_name)


show_college()
print("Outside function:", college_name)
```

**Output**

```text
College: ABC College
Outside function: ABC College
```

### How does it work?

- `college_name` is created outside the function.
- Therefore, it is a global variable.
- `show_college()` can read and print it.
- It can also be used outside the function.

**Important:** A function can read a global variable without using the `global` keyword.

---

## 4. Local and Global Variables with the Same Name

If a local variable and a global variable have the same name, the local variable is used inside that function. The global variable remains unchanged.

### Example

```python
number = 100


def show_number():
    number = 50
    print("Inside function:", number)


show_number()
print("Outside function:", number)
```

**Output**

```text
Inside function: 50
Outside function: 100
```

### Why is the output different?

- `number = 100` is a global variable.
- `number = 50` inside the function creates a separate local variable.
- Inside the function, Python uses the local variable.
- Outside the function, Python uses the global variable.

**Remember:** A local variable with the same name does not automatically change the global variable.

---

## 5. Modifying a Global Variable Inside a Function

There is an important difference between **reading** a global variable and **changing** it.

A function can read a global variable directly. But if you want to assign a new value to that global variable from inside a function, you must declare it using the `global` keyword.

### Example: Without the `global` Keyword

```python
score = 10


def update_score():
    score = 50
    print("Inside function:", score)


update_score()
print("Outside function:", score)
```

**Output**

```text
Inside function: 50
Outside function: 10
```

Here, `score = 50` creates a local variable. It does not update the global variable.

### Example: With the `global` Keyword

```python
score = 10


def update_score():
    global score
    score = 50
    print("Inside function:", score)


update_score()
print("Outside function:", score)
```

**Output**

```text
Inside function: 50
Outside function: 50
```

### How does `global` work?

```python
global score
```

This statement tells Python:

> Use the global variable named `score`; do not create a new local variable with this name.

Now, the assignment `score = 50` updates the global variable.

### Important Rules

- Use `global variable_name` inside a function when you need to assign a new value to a global variable.
- You do not need `global` just to read a global variable.
- Use the `global` keyword carefully. Changing global variables from many functions can make a program harder to understand.

---

## 6. What Is Variable Lifetime?

**Variable lifetime** means how long a variable exists while a program is running.

In simple words:

> Lifetime tells us **how long a variable stays available**.

A variable's scope tells us where it can be used. Its lifetime tells us how long it exists.

Local and global variables have different lifetimes.

---

## 7. Lifetime of a Local Variable

A local variable is created when its function starts executing.

It remains available while that function call is running. When the function finishes, its local variables are no longer available for use outside that call.

### Example

```python
def calculate_square(number):
    result = number * number
    print("Square:", result)


calculate_square(5)
calculate_square(8)
```

**Output**

```text
Square: 25
Square: 64
```

### Understand the execution

**First function call:**

1. The function starts.
2. The local parameter `number` receives `5`.
3. The local variable `result` stores `25`.
4. The function prints the result.
5. The function finishes. Its local variables are no longer available for use outside that call.

**Second function call:**

1. The function starts again.
2. A new local parameter `number` receives `8`.
3. The local variable `result` stores `64`.
4. The function prints the result.
5. The function finishes.

Each function call gets its own local variables.

---

## 8. Lifetime of a Global Variable

A global variable is created when the program reaches its definition.

It generally remains available until the program finishes.

### Example

```python
college_name = "ABC College"


def show_college():
    print(college_name)


show_college()
show_college()
print(college_name)
```

**Output**

```text
ABC College
ABC College
ABC College
```

The global variable `college_name` remains available across both function calls and can also be used outside the function.

---

## 9. Difference Between Local and Global Variables

| Point | Local Variable | Global Variable |
|---|---|---|
| Where is it created? | Inside a function | Outside all functions |
| Where can it be accessed? | Normally only inside its function | Inside functions and outside them |
| Lifetime | During the function call | Generally until the program ends |
| Can another function use it directly? | No | Yes, it can read the global variable |
| How is it modified? | Direct assignment inside its function | Use `global` before assigning to it inside a function |

---

## 10. Scope vs Lifetime

These two terms are related, but they do not mean the same thing.

| Scope | Lifetime |
|---|---|
| Tells where a variable can be accessed | Tells how long a variable exists |
| Answers: "Where can I use it?" | Answers: "How long does it stay available?" |
| Example: A local variable is accessible inside its function | Example: A local variable exists during that function call |

**Easy way to remember:**

- **Scope = Where**
- **Lifetime = How long**

---

## 11. Common Mistakes to Avoid

### Mistake 1: Using a Local Variable Outside Its Function

```python
def display():
    message = "Welcome"


display()
print(message)
```

**Problem:** `message` is local to `display()`. It cannot be accessed outside the function.

### Mistake 2: Expecting a Local Assignment to Update a Global Variable

```python
count = 5


def update_count():
    count = 20


update_count()
print(count)
```

**Output**

```text
5
```

**Problem:** The assignment inside the function creates a local variable named `count`. The global variable remains `5`.

### Mistake 3: Forgetting the `global` Keyword When Updating a Global Variable

```python
total = 100


def update_total():
    global total
    total = 500


update_total()
print(total)
```

**Output**

```text
500
```

**Remember:** Use `global total` when you want the assignment inside the function to update the global variable.

---

## 12. Quick Revision

- A local variable is created inside a function.
- A global variable is created outside all functions.
- A local variable is normally accessible only inside its function.
- A function can read a global variable without using `global`.
- To assign a new value to a global variable inside a function, use the `global` keyword.
- A local variable's lifetime is associated with its function call.
- A global variable generally remains available until the program finishes.
- Scope means where a variable can be accessed.
- Lifetime means how long a variable exists.

---

## 13. Practice Questions

### A. Predict the Output

**Q1.**

```python
number = 25


def display():
    number = 10
    print(number)


display()
print(number)
```

*Hint: Check whether the function uses the local or global variable.*

**Q2.**

```python
message = "Python"


def show_message():
    print(message)


show_message()
print(message)
```

*Hint: The function is reading a global variable.*

**Q3.**

```python
value = 100


def update():
    global value
    value = 200


update()
print(value)
```

*Hint: The `global` keyword allows the function to update the global variable.*

**Q4.**

```python
def calculate(a):
    result = a * 2
    print(result)


calculate(5)
calculate(10)
```

*Hint: Each function call receives its own local parameter and local variable.*

**Q5.**

```python
x = 50


def first():
    x = 20
    print("First:", x)


def second():
    print("Second:", x)


first()
second()
print("Outside:", x)
```

*Hint: The local variable in `first()` does not change the global variable used by `second()`.*

### B. Find and Correct the Error

**Q6.** Find the error and correct the program so that it displays the message.

```python
def display_message():
    message = "Welcome to Python"


display_message()
print(message)
```

*Hint: Think about where the local variable can be accessed.*

**Q7.** Correct the program so that the global variable `price` is updated to `500`.

```python
price = 100


def update_price():
    price = 500


update_price()
print(price)
```

*Hint: The function should update the global variable, not create a local one.*

### C. Short Answer Questions

1. What is variable scope?
2. What is variable lifetime?
3. What is a local variable?
4. What is a global variable?
5. Can a function read a global variable without using the `global` keyword?
6. When do we use the `global` keyword?
7. What happens to a local variable when a function call finishes?
8. Write two differences between local and global variables.
