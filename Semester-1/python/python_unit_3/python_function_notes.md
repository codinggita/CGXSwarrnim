# Python Functions

## Learning Objectives

After completing this chapter, students should be able to:

1.  Explain what a function is and why programmers use functions.
2.  Create a function using `def`.
3.  Call a function to execute its code.
4.  Understand parameters and arguments.
5.  Pass information to a function.
6.  Return a result from a function.
7.  Explain the difference between `print()` and `return`.
8.  Use positional, keyword, and default arguments.
9.  Understand local and global variables at a basic level.
10. Read, write, test, and debug simple user-defined functions.

------------------------------------------------------------------------

## 1. What Is a Function?

A **function** is a named, reusable block of code that performs a
particular task.

Think about a calculator. Whenever you press the `+` button, the
calculator performs an addition task. You do not need to explain the
addition process every time you press the button.

In Python, we can create a function for a task and use it whenever
required.

### Real-life example: A juice machine

Imagine a juice machine:

-   You give it fruits.
-   The machine performs some work.
-   It gives you juice.

A Python function can work in a similar way:

-   It may receive some input.
-   It performs a task.
-   It may give a result back.

### Why do we use functions?

Suppose we need to calculate the area of a rectangle at several places
in a program.

Without a function, we may have to write the same calculation
repeatedly:

``` python
length = 10
breadth = 5
area = length * breadth
print(area)

length = 8
breadth = 4
area = length * breadth
print(area)

length = 12
breadth = 6
area = length * breadth
print(area)
```

Instead, we can write the calculation once inside a function and reuse
it:

``` python
def calculate_area(length, breadth):
    area = length * breadth
    print(area)

calculate_area(10, 5)
calculate_area(8, 4)
calculate_area(12, 6)
```

### Main benefits

-   **Code reusability:** Write code once and use it many times.
-   **Less repetition:** Avoid writing the same logic again and again.
-   **Better readability:** Give a meaningful name to a task.
-   **Easy maintenance:** If the logic changes, update it in one place.
-   **Easy testing:** Test a small task separately.

------------------------------------------------------------------------

## 2. Types of Functions in Python

At a beginner level, we can understand two common categories.

### 2.1 Built-in functions

Python already provides some functions. These are called **built-in
functions**.

Examples:

``` python
print("Hello")
length = len("Python")
number = int("25")
result = max(10, 20, 30)

print(length)
print(number)
print(result)
```

Here, `print()`, `len()`, `int()`, and `max()` are built-in functions.

### 2.2 User-defined functions

A function created by the programmer is called a **user-defined
function**.

Example:

``` python
def greet():
    print("Welcome to Python!")

greet()
```

Here, `greet()` is a user-defined function.

------------------------------------------------------------------------

## 3. Creating a Function: The `def` Keyword

In Python, we use the `def` keyword to define a function.

### Basic syntax

``` python
def function_name():
    statement
    statement
```

Understand each part:

  Part                  Meaning
  --------------------- ---------------------------------------------
  `def`                 Keyword used to define a function
  `function_name`       Name given to the function
  `()`                  Parentheses; parameters can be written here
  `:`                   Marks the beginning of the function body
  Indented statements   Code that belongs to the function

Example:

``` python
def say_hello():
    print("Hello!")
    print("Welcome to the class.")
```

**Important:** Defining a function does not execute its body. It only
tells Python what the function should do when it is called.

### Function definition vs function call

``` python
def say_hello():              # Function definition
    print("Hello!")

say_hello()                   # Function call
```

Output:

``` text
Hello!
```

-   **Function definition:** Creating the function.
-   **Function call:** Asking Python to execute the function.

### What happens if we do not call the function?

``` python
def say_hello():
    print("Hello!")

print("Program ended.")
```

Output:

``` text
Program ended.
```

The function body does not run because `say_hello()` was never called.

------------------------------------------------------------------------

## 3.1 Choosing a Good Function Name

A function name should clearly describe its task.

Good examples: `calculate_area()`, `display_student_details()`, `find_largest_number()`.

Avoid unclear names such as `abc()` or `x1()`.

### Function naming rules

- Use letters, digits, and underscores.
- Do not start a name with a digit.
- Do not use Python keywords such as `if`, `for`, or `return`.
- Function names are case-sensitive.
- Prefer meaningful `snake_case` names: lowercase words separated by underscores.

---

## 4. How Does a Function Execute?

Python executes a function when it reaches a function call.

Consider this program:

``` python
print("Start")

def greet():
    print("Hello from function")

print("Before calling")
greet()
print("End")
```

Output:

``` text
Start
Before calling
Hello from function
End
```

### Execution flow diagram

``` mermaid
flowchart TD
    A([Program starts]) --> B[Print Start]
    B --> C[Read and define greet function]
    C --> D[Print Before calling]
    D --> E[Call greet]
    E --> F[Execute function body]
    F --> G[Print Hello from function]
    G --> H[Return to the next statement]
    H --> I[Print End]
    I --> J([Program ends])
```

**Remember:** Python reads the function definition and makes the
function available. The function body runs when the function is called.

------------------------------------------------------------------------

## 5. Calling a Function Multiple Times

A function can be called as many times as needed.

``` python
def welcome():
    print("Welcome!")

welcome()
welcome()
welcome()
```

Output:

``` text
Welcome!
Welcome!
Welcome!
```

The same function is reused three times. We do not need to write the
`print()` statement three times.

------------------------------------------------------------------------

## 6. Parameters and Arguments

A function often needs information to perform its task.

For example, an addition function needs two numbers. We can send those
numbers to the function.

### Example

``` python
def add(a, b):
    print(a + b)

add(10, 20)
```

Output:

``` text
30
```

In this example:

-   `a` and `b` are **parameters**.
-   `10` and `20` are **arguments**.

### Parameter vs argument

  -----------------------------------------------------------------------
  Parameter                           Argument
  ----------------------------------- -----------------------------------
  A variable written in the function  The actual value supplied during a
  definition                          function call

  Receives the value                  Sends the value

  Example: `a`, `b`                   Example: `10`, `20`
  -----------------------------------------------------------------------

### Real-life example: Booking a movie ticket

Imagine a ticket-booking function that needs a movie name and number of
tickets.

``` python
def book_ticket(movie_name, ticket_count):
    print("Movie:", movie_name)
    print("Tickets:", ticket_count)

book_ticket("Avengers", 3)
```

Output:

``` text
Movie: Avengers
Tickets: 3
```

Here, `movie_name` and `ticket_count` are parameters. `"Avengers"` and
`3` are arguments.

### How are values passed?

``` mermaid
flowchart LR
    A["Function call<br/>add(10, 20)"] --> B["Parameter a = 10"]
    A --> C["Parameter b = 20"]
    B --> D["Function body<br/>a + b"]
    C --> D
    D --> E["Output: 30"]
```

------------------------------------------------------------------------

## 7. Functions With Different Numbers of Parameters

A function can have one, two, or more parameters.

### One parameter

``` python
def square(number):
    print(number * number)

square(5)
square(8)
```

Output:

``` text
25
64
```

### Two parameters

``` python
def multiply(a, b):
    print(a * b)

multiply(4, 5)
```

Output:

``` text
20
```

### Three parameters

``` python
def calculate_total(price, quantity, delivery_charge):
    total = price * quantity + delivery_charge
    print("Total:", total)

calculate_total(100, 3, 40)
```

Output:

``` text
Total: 340
```

**Important:** The number of required arguments in a function call must
match the number of required parameters, unless default values or other
supported argument forms are used.

------------------------------------------------------------------------

## 7.1 Rest Parameters: Accepting Many Arguments

Sometimes we do not know in advance how many values a function will receive. For example, we may want to calculate the total of 2, 3, or 5 numbers.

Python provides `*` to collect extra positional arguments. The common name is `*args`. The word `args` is only a convention; the `*` is important.

```python
def show_values(*args):
    print(args)

show_values(10, 20)
show_values(10, 20, 30)
show_values(5, 10, 15, 20)
```

Output:

```text
(10, 20)
(10, 20, 30)
(5, 10, 15, 20)
```

The extra arguments are collected into a **tuple**.

### Using `*args` to calculate a total

```python
def calculate_total(*args):
    total = 0

    for number in args:
        total = total + number

    return total

print(calculate_total(10, 20))
print(calculate_total(10, 20, 30))
print(calculate_total(5, 10, 15, 20))
```

Output:

```text
30
60
50
```

### Combining a normal parameter with `*args`

```python
def show_student(subject, *marks):
    print("Subject:", subject)
    print("Marks:", marks)

show_student("Python", 80, 90, 85)
```

Output:

```text
Subject: Python
Marks: (80, 90, 85)
```

`subject` receives the first argument. `*marks` collects the remaining positional arguments into a tuple.

**Remember:**
- `*args` allows a variable number of positional arguments.
- The collected values are stored as a tuple.
- `args` can be replaced with another valid name, such as `*numbers`.
- The `*` is what makes it a rest parameter.

---

## 8. The `return` Statement

A function can display a result, but sometimes another part of the
program needs to use that result.

For this, Python provides the `return` statement.

The `return` statement sends a value back to the place where the
function was called.

### Example

``` python
def add(a, b):
    result = a + b
    return result

answer = add(10, 20)
print(answer)
```

Output:

``` text
30
```

What happens?

1.  `add(10, 20)` calls the function.
2.  `a` receives `10` and `b` receives `20`.
3.  The function calculates `30`.
4.  `return result` sends `30` back.
5.  The returned value is stored in `answer`.
6.  `print(answer)` displays `30`.

### Flow diagram of `return`

``` mermaid
flowchart TD
    A["Call: answer = add(10, 20)"] --> B["Function receives a = 10, b = 20"]
    B --> C["Calculate result = a + b"]
    C --> D["return result"]
    D --> E["Value 30 goes back to caller"]
    E --> F["answer = 30"]
    F --> G["print(answer)"]
```

### Using the returned value in another calculation

``` python
def square(number):
    return number * number

result = square(5) + square(3)
print(result)
```

Output:

``` text
34
```

Explanation:

-   `square(5)` returns `25`.
-   `square(3)` returns `9`.
-   Python adds `25 + 9`.
-   The final result is `34`.

------------------------------------------------------------------------

## 8.1 Returning Multiple Values

A function can return more than one value in a single `return` statement.

```python
def calculate(number_1, number_2):
    total = number_1 + number_2
    difference = number_1 - number_2
    return total, difference

answer = calculate(20, 5)
print(answer)
```

Output:

```text
(25, 15)
```

Python groups the returned values into a **tuple**.

### Store returned values separately

```python
def calculate(number_1, number_2):
    total = number_1 + number_2
    difference = number_1 - number_2
    return total, difference

sum_result, difference_result = calculate(20, 5)

print("Sum:", sum_result)
print("Difference:", difference_result)
```

Output:

```text
Sum: 25
Difference: 15
```

This is called unpacking: the returned values are assigned to separate variables.

**Important:** A function can return multiple values, but only the first `return` statement reached during a particular call is executed.

---

## 9. Difference Between `print()` and `return`

This is one of the most important concepts in functions.

### `print()`

-   Displays information on the screen.
-   Does not send that displayed information back as the function's
    result.

### `return`

-   Sends a value back to the caller.
-   The returned value can be stored, printed, or used in another
    calculation.
-   Ends the current function execution.

Compare these two functions:

``` python
def add_and_print(a, b):
    print(a + b)

def add_and_return(a, b):
    return a + b

first_result = add_and_print(10, 20)
second_result = add_and_return(10, 20)

print("First result:", first_result)
print("Second result:", second_result)
```

Output:

``` text
30
First result: None
Second result: 30
```

Why is the first result `None`?

`add_and_print()` displays `30`, but it does not return a value. Python
automatically returns `None` when a function finishes without an
explicit `return` value.

### Comparison table

  -----------------------------------------------------------------------
  `print()`                           `return`
  ----------------------------------- -----------------------------------
  Displays a value                    Sends a value back

  Mainly used to show output          Used when the caller needs the
                                      result

  Does not itself return the          Provides a value to the caller
  displayed value                     

  Function can continue after         Ends the function when executed
  `print()`                           
  -----------------------------------------------------------------------

### A useful rule

Use `print()` when you only need to display something.

Use `return` when you need to give a result back so that other code can
use it.

------------------------------------------------------------------------

## 10. What Happens After `return`?

When Python executes a `return` statement, the function ends
immediately. Statements written after that `return` in the same
execution path are not executed.

``` python
def check():
    print("First statement")
    return 100
    print("This will not execute")

result = check()
print(result)
```

Output:

``` text
First statement
100
```

The second `print()` inside the function is not executed.

### A function can return different values from different paths

``` python
def get_message():
    number = 10

    if number > 0:
        return "Positive number"

    return "Zero or negative number"

print(get_message())
```

Output:

``` text
Positive number
```

A function can contain more than one `return` statement. However, only
the first `return` reached during a particular function call is
executed.

------------------------------------------------------------------------

## 11. Function Without a `return` Statement

If a function does not explicitly return a value, Python returns `None`
automatically.

``` python
def greet():
    print("Hello!")

result = greet()

print("Stored result:", result)
```

Output:

``` text
Hello!
Stored result: None
```

`None` means that no meaningful value was returned.

------------------------------------------------------------------------

## 12. Positional Arguments

When arguments are passed according to their position, they are called
**positional arguments**.

``` python
def student_details(name, age):
    print("Name:", name)
    print("Age:", age)

student_details("Rahul", 18)
```

Output:

``` text
Name: Rahul
Age: 18
```

The first argument goes to the first parameter, and the second argument
goes to the second parameter.

### Why does order matter?

``` python
student_details(18, "Rahul")
```

Output:

``` text
Name: 18
Age: Rahul
```

Python does not automatically understand that `18` is an age. It assigns
values according to their positions.

------------------------------------------------------------------------

## 13. Keyword Arguments

We can also pass arguments by writing the parameter names in the
function call. These are called **keyword arguments**.

``` python
def student_details(name, age):
    print("Name:", name)
    print("Age:", age)

student_details(age=18, name="Rahul")
```

Output:

``` text
Name: Rahul
Age: 18
```

Notice that the order does not matter when we use the correct parameter
names.

### Positional vs keyword arguments

  -----------------------------------------------------------------------
  Positional arguments                Keyword arguments
  ----------------------------------- -----------------------------------
  Values are assigned according to    Values are assigned using parameter
  position                            names

  Order matters                       Order can be changed

  Example: `show("Aman", 20)`         Example:
                                      `show(age=20, name="Aman")`
  -----------------------------------------------------------------------

### Important rule

When positional and keyword arguments are used together, positional
arguments must come before keyword arguments.

Correct:

``` python
def show(name, age):
    print(name, age)

show("Aman", age=20)
```

Incorrect:

``` python
# This causes a SyntaxError:
# show(name="Aman", 20)
```

------------------------------------------------------------------------

## 14. Default Arguments

Sometimes we want a parameter to have a value automatically when the
caller does not provide an argument.

We can assign a default value in the function definition.

``` python
def welcome(name="Student"):
    print("Welcome", name)

welcome("Aman")
welcome()
```

Output:

``` text
Welcome Aman
Welcome Student
```

Explanation:

-   In `welcome("Aman")`, the supplied argument is used.
-   In `welcome()`, no argument is supplied, so the default value
    `"Student"` is used.

### Real-life example: Delivery charge

Suppose an online store normally charges a delivery fee of 50.

``` python
def calculate_bill(price, delivery_charge=50):
    total = price + delivery_charge
    print("Total bill:", total)

calculate_bill(500)
calculate_bill(500, 0)
```

Output:

``` text
Total bill: 550
Total bill: 500
```

The second call supplies `0`, so the supplied value replaces the default
value.

### Important rules for default arguments

1.  A parameter with a default value can be omitted from the function
    call.
2.  If an argument is supplied, it replaces the default value.
3.  Parameters without default values must come before parameters with
    default values.

Correct:

``` python
def calculate(price, tax=10):
    print(price + tax)
```

Incorrect:

``` python
# This causes a SyntaxError:
# def calculate(tax=10, price):
#     print(price + tax)
```

------------------------------------------------------------------------

## 15. Local Variables

A variable created inside a function is generally called a **local
variable**.

It can be used inside that function.

``` python
def calculate():
    number = 10
    print(number)

calculate()
```

Output:

``` text
10
```

Here, `number` is created inside `calculate()`. It is a local variable.

### Can we use a local variable outside the function?

``` python
def calculate():
    number = 10

calculate()
print(number)
```

This causes a `NameError` because `number` is local to the function and
is not available in the outer part of the program.

------------------------------------------------------------------------

## 16. Global Variables

A variable created outside all functions is called a **global
variable**.

It can generally be read inside a function.

``` python
college_name = "ABC College"

def show_college():
    print(college_name)

show_college()
```

Output:

``` text
ABC College
```

Here, `college_name` is created outside the function and read inside it.

### Local vs global variables

  -----------------------------------------------------------------------
  Local variable                      Global variable
  ----------------------------------- -----------------------------------
  Created inside a function           Created outside functions

  Normally used inside that function  Can be read in different parts of
                                      the program

  Its scope is limited to the         Its scope is wider
  function                            
  -----------------------------------------------------------------------

**Beginner guideline:** Prefer passing information through parameters
and returning results. This makes functions easier to understand and
test. Changing global variables from inside functions using `global` is
not needed for our beginner examples.

------------------------------------------------------------------------

## 16.1 Variable Scope and Lifetime

Two important ideas help us understand variables:

- **Scope:** Where can we access a variable?
- **Lifetime:** During which period does the variable remain available?

### Local variable

A local variable is created inside a function. It can normally be accessed only inside that function. Its local lifetime lasts while that function call is executing.

```python
def calculate():
    number = 10
    print(number)

calculate()
```

Output:

```text
10
```

Trying to use `number` outside the function causes a `NameError`:

```python
def calculate():
    number = 10

calculate()
print(number)  # NameError
```

### Global variable

A global variable is created outside functions. It can be read inside functions and normally remains available while the program is running.

```python
college = "ABC College"

def show_college():
    print(college)

show_college()
print(college)
```

Output:

```text
ABC College
ABC College
```

### Local and global variables with the same name

```python
number = 100

def show():
    number = 20
    print("Inside function:", number)

show()
print("Outside function:", number)
```

Output:

```text
Inside function: 20
Outside function: 100
```

The assignment `number = 20` creates a local variable. It does not change the global variable.

### Changing a global variable

Python provides the `global` keyword when a function needs to assign to a global variable.

```python
number = 100

def update():
    global number
    number = 200

update()
print(number)
```

Output:

```text
200
```

For beginner programs, prefer passing information through parameters and sending results back with `return`. Avoid changing global variables unless there is a clear reason.

### Scope and lifetime summary

| Variable | Scope | Lifetime |
|---|---|---|
| Local variable | Inside the function where it is created | During that function call |
| Global variable | In the module; can be read inside its functions | Normally for the duration of the program |

This is the beginner-level model. Python's detailed object-lifetime rules can be more complex, but they are not required for this chapter.

---

## 17. Function Calling Another Function

One function can call another function.

``` python
def greet():
    print("Welcome!")

def start_program():
    print("Program started")
    greet()
    print("Program finished")

start_program()
```

Output:

``` text
Program started
Welcome!
Program finished
```

The `start_program()` function calls `greet()`. This helps us divide a
larger task into smaller tasks.

### Flow diagram

``` mermaid
flowchart TD
    A["Call start_program()"] --> B["Print Program started"]
    B --> C["Call greet()"]
    C --> D["Print Welcome!"]
    D --> E["Return to start_program()"]
    E --> F["Print Program finished"]
```

------------------------------------------------------------------------

## 18. Complete Real-Life Example: Simple Bill Calculator

Let's create a small billing program using functions.

Requirements:

-   Receive the item price and quantity.
-   Calculate the total amount.
-   Add a delivery charge.
-   Return the final bill.
-   Display the final bill.

``` python
def calculate_total(price, quantity):
    total = price * quantity
    return total

def add_delivery_charge(amount, delivery_charge=40):
    final_amount = amount + delivery_charge
    return final_amount

item_price = 100
quantity = 3

amount = calculate_total(item_price, quantity)
final_bill = add_delivery_charge(amount)

print("Item amount:", amount)
print("Final bill:", final_bill)
```

Output:

``` text
Item amount: 300
Final bill: 340
```

### Understand the program flow

``` mermaid
flowchart TD
    A([Start]) --> B["Set item_price = 100"]
    B --> C["Set quantity = 3"]
    C --> D["Call calculate_total(100, 3)"]
    D --> E["Calculate 100 × 3"]
    E --> F["Return 300"]
    F --> G["Call add_delivery_charge(300)"]
    G --> H["Add default delivery charge 40"]
    H --> I["Return 340"]
    I --> J["Print item amount and final bill"]
    J --> K([End])
```

This example combines function definition, function calling, parameters,
arguments, return values, and default arguments.

------------------------------------------------------------------------

## 19. Common Mistakes to Avoid

### Mistake 1: Forgetting to call the function

``` python
def greet():
    print("Hello!")

# No output because the function is not called.
```

Correct:

``` python
def greet():
    print("Hello!")

greet()
```

### Mistake 2: Incorrect indentation

Incorrect:

``` python
def greet():
print("Hello!")
```

Correct:

``` python
def greet():
    print("Hello!")
```

### Mistake 3: Passing the wrong number of arguments

``` python
def add(a, b):
    print(a + b)

# Incorrect: one required argument is missing.
# add(10)
```

Correct:

``` python
add(10, 20)
```

### Mistake 4: Confusing `print()` with `return`

``` python
def add(a, b):
    print(a + b)

result = add(5, 5)
print(result)
```

Output:

``` text
10
None
```

If the caller needs the calculated value, use `return`.

### Mistake 5: Calling a function before it has been defined

``` python
# greet()  # NameError: greet is not defined yet

def greet():
    print("Hello!")

greet()
```

In a normal top-to-bottom Python program, define the function before the
line that calls it.

------------------------------------------------------------------------

## 20. Quick Revision

  Term                  Simple meaning
  --------------------- ---------------------------------------------
  Function              Reusable block of code for a task
  `def`                 Keyword used to define a function
  Function definition   Creating the function
  Function call         Executing the function
  Parameter             Variable written in the function definition
  Argument              Value supplied during a function call
  `return`              Sends a value back to the caller
  `print()`             Displays information on the screen
  Positional argument   Argument assigned according to position
  Keyword argument      Argument assigned using its parameter name
  Default argument      Value used when an argument is not supplied
  Local variable        Variable created inside a function
  Global variable       Variable created outside functions
  `None`                Represents the absence of a returned value

### Remember these points

-   A function is defined using `def`.
-   Defining a function does not execute its body.
-   A function runs when it is called.
-   Parameters receive arguments.
-   `print()` displays a value; `return` sends a value back.
-   A function stops executing when it reaches `return`.
-   If no value is returned explicitly, Python returns `None`.
-   Default arguments are used when the caller does not supply a value.
-   Use meaningful function names such as `calculate_area()` or
    `find_average()`.

------------------------------------------------------------------------

# Practice Questions

Try these questions after understanding the notes. Start with output
prediction, then write programs.

## A. Understand the Basics

1.  What is a function?
2.  Why do programmers use functions?
3.  Which keyword is used to define a function in Python?
4.  What is the difference between defining and calling a function?
5.  What is a built-in function? Give three examples.
6.  What is a user-defined function? Write one example.
7.  What is the difference between a parameter and an argument?
8.  What happens if a function is defined but never called?

## B. Predict the Output

**Q1.**

``` python
def show():
    print("Python")

print("Start")
show()
print("End")
```

**Q2.**

``` python
def greet():
    print("Hello")

greet()
greet()
```

**Q3.**

``` python
def display(number):
    print(number * 2)

display(5)
display(8)
```

**Q4.**

``` python
def add(a, b):
    print(a + b)

add(10, 20)
add(5, 7)
```

**Q5.**

``` python
def calculate(a, b):
    result = a * b
    return result

answer = calculate(4, 5)
print(answer)
print(answer + 10)
```

**Q6.**

``` python
def show():
    print("Inside function")

result = show()
print(result)
```

**Q7.**

``` python
def welcome(name="Student"):
    print("Welcome", name)

welcome()
welcome("Riya")
```

**Q8.**

``` python
def details(name, age):
    print(name, age)

details(age=19, name="Aman")
```

**Q9.**

``` python
def first():
    print("First")

def second():
    print("Second")
    first()

second()
```

**Q10.**

``` python
def test():
    print("A")
    return 50
    print("B")

value = test()
print(value)
```

## C. Find the Error

For each snippet, identify the error and write the corrected code.

1.  

``` python
def greet()
    print("Hello")
```

2.  

``` python
def add(a, b):
    print(a + b)

add(10)
```

3.  

``` python
def welcome():
print("Welcome")
```

4.  

``` python
def calculate(a, b):
    return a + b

print(result)
```

5.  

``` python
def show(name, age):
    print(name, age)

show(name="Ravi", 18)
```

## D. Write Programs Using Functions

1.  Create a function named `greet()` that prints a welcome message.
2.  Create a function named `square()` that accepts a number and prints
    its square.
3.  Create a function named `cube()` that accepts a number and returns
    its cube.
4.  Create a function named `add()` that accepts two numbers and returns
    their sum.
5.  Create a function named `find_largest()` that accepts two numbers
    and returns the larger number.
6.  Create a function named `is_even()` that accepts a number and
    returns `True` if it is even; otherwise, return `False`.
7.  Create a function named `calculate_area()` that accepts the length
    and breadth of a rectangle and returns its area.
8.  Create a function named `calculate_bill()` that accepts price and
    quantity and returns the total bill.
9.  Create a function named `convert_temperature()` that accepts Celsius
    and returns Fahrenheit. Use the formula: `F = (C * 9 / 5) + 32`.
10. Create a function named `calculate_average()` that accepts three
    numbers and returns their average.

## E. Real-Life Problem Solving

1.  **Student Result:** Create a function that accepts marks in three
    subjects and returns the total marks.
2.  **Shopping Bill:** Create a function that accepts item price and
    quantity. Return the total amount.
3.  **Movie Ticket:** Create a function that accepts ticket price and
    number of tickets. Return the total cost.
4.  **Electricity Bill:** Create a function that accepts units consumed
    and rate per unit. Return the bill amount.
5.  **Travel Cost:** Create a function that accepts distance and cost
    per kilometre. Return the total travel cost.

------------------------------------------------------------------------
