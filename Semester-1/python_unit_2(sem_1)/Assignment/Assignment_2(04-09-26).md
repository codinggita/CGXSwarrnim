# Assignment-2

**Deadline:** 04 September 26

## Topics Covered

- Variables
- Variable Naming Rules
- Valid and Invalid Variable Names
- Case Sensitivity
- `print()`
- Strings
- Data Types: `str`, `int`, `float`, `bool`
- `type()`
- Basic Python Syntax
- Syntax Errors
- Debugging
- Type Casting
- Arithmetic Operators
- Digit Extraction using `%` and `//`
- Operator Precedence

---

## Instructions

1. Read each question carefully before writing the code.
2. Use meaningful variable names.
3. Use suitable data types.
4. Write complete Python programs wherever required.
5. For debugging questions, identify the issue and write one corrected version of the complete code.
6. For output questions, predict the output first and then verify it.
7. Use only the concepts covered in this assignment.
8. Do not use lists, loops, conditional statements, functions, or advanced concepts unless a question specifically asks for them.
9. Keep your code clean and properly indented.

---

# Topic 1: Type Casting

Type casting means converting a value from one data type to another.

Common functions:

```python
int()
float()
str()
bool()
```

---

## Question 1 — String to Integer

Convert `"25"` into an integer and print its value and type.

```python
age = "25"
```

### Expected Output

```text
25
<class 'int'>
```

---

## Question 2 — String to Float

Convert `"75.5"` into a float and print its value and type.

```python
marks = "75.5"
```

---

## Question 3 — Integer to Float

Convert `50` into a float.

```python
number = 50
```

Print the converted value and its type.

---

## Question 4 — Float to Integer

Convert `85.9` into an integer.

```python
marks = 85.9
```

Print the result and observe what happens to the decimal part.

---

## Question 5 — Integer to String

Convert the integer `101` into a string and print its value and type.

```python
roll_number = 101
```

---

## Question 6 — Multiple Conversions

Convert the following values:

- `"18"` → `int`
- `"92.5"` → `float`
- `100` → `str`
- `45.8` → `int`

Print every converted value with its type.

---

## Question 7 — Predict the Output

Predict the output before running:

```python
a = "20"
b = int(a)

c = 10.8
d = int(c)

e = 25
f = str(e)

print(b)
print(d)
print(f)
print(type(b))
print(type(d))
print(type(f))
```

---

## Question 8 — Debug Type Casting

Find the error and write one correct version of the complete code.

```python
age = "19"
new_age = age + 1

print("Age:", new_age)
```

---

## Question 9 — Marks Conversion

Marks are stored as a string:

```python
marks = "85"
```

Convert the marks into an integer and add 5 bonus marks.

### Expected Output

```text
Final Marks: 90
```

---

## Question 10 — Price Conversion

A product price is stored as a string:

```python
price = "1499.50"
```

Convert it into a float and add `99.50` delivery charges.

### Expected Output

```text
Total Amount: 1599.0
```

---

# Topic 2: Arithmetic Operators

| Operator | Meaning | Example |
|---|---|---|
| `+` | Addition | `10 + 5` |
| `-` | Subtraction | `10 - 5` |
| `*` | Multiplication | `10 * 5` |
| `/` | Division | `10 / 5` |
| `//` | Floor Division | `10 // 3` |
| `%` | Remainder | `10 % 3` |
| `**` | Power | `2 ** 3` |

---

## Question 11 — Basic Arithmetic

Create:

```python
a = 20
b = 6
```

Perform and print:

1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Floor division
6. Remainder
7. Power

---

## Question 12 — Predict the Output

Predict the output:

```python
a = 17
b = 5

print(a / b)
print(a // b)
print(a % b)
```

Explain in one or two sentences why the three results are different.

---

## Question 13 — Operator Precedence

Predict the output:

```python
result = 10 + 5 * 2
print(result)
```

Now rewrite the expression so that addition happens first.

---

## Question 14 — More Precedence Practice

Predict the output:

```python
result = 20 - 4 * 3 + 2
print(result)
```

Then rewrite the expression using parentheses to make the order of calculation clear.

---

## Question 15 — Power Operator

Predict the output:

```python
print(2 ** 3)
print(3 ** 2)
print(10 ** 2)
```

Then create:

```python
side = 5
```

and calculate the area of a square.

---

## Question 16 — Shopping Bill

A student buys:

- Notebook = ₹80
- Pen = ₹20
- Pencil = ₹10

Create variables and calculate the total amount.

### Expected Output

```text
Total Amount: 110
```

---

## Question 17 — Multiple Quantities

A student buys:

- 3 notebooks at ₹50 each
- 2 pens at ₹15 each
- 1 calculator at ₹500

Calculate the cost of each category and the total bill.

### Expected Output

```text
Notebook Cost: 150
Pen Cost: 30
Calculator Cost: 500
Total Bill: 680
```

---

## Question 18 — Complete Groups and Remainder

A class has `47` students. They are divided into groups of `5`.

Find:

1. Complete groups
2. Students left over

### Expected Output

```text
Complete Groups: 9
Students Left: 2
```

---

## Question 19 — Average Marks

A student scored:

- Python = 85
- Mathematics = 78
- Physics = 92

Calculate total and average marks.

---

## Question 20 — Percentage

A student scored:

- English = 78
- Mathematics = 85
- Python = 92
- Physics = 81
- Chemistry = 74

Each subject is out of 100.

Calculate total marks and percentage.

---

# Topic 3: Digit Extraction using `%` and `//`

## Instructions

For these questions, **do not convert the number into a string**.

Use arithmetic operators.

Useful ideas:

```python
number % 10
```

finds the last digit.

```python
number // 10
```

removes the last digit.

---

## Question 21 — Ones Digit

Given:

```python
number = 583
```

Find the ones digit.

### Expected Output

```text
Ones Digit: 3
```

---

## Question 22 — Tens Digit

Given:

```python
number = 583
```

Find the tens digit using arithmetic operators.

### Expected Output

```text
Tens Digit: 8
```

---

## Question 23 — Hundreds Digit

Given:

```python
number = 583
```

Find the hundreds digit.

### Expected Output

```text
Hundreds Digit: 5
```

---

## Question 24 — Three-Digit Number Analyzer

Given:

```python
number = 746
```

Find:

1. Ones digit
2. Tens digit
3. Hundreds digit

### Expected Output

```text
Ones Digit: 6
Tens Digit: 4
Hundreds Digit: 7
```

---

## Question 25 — Four-Digit Number

Given:

```python
number = 5829
```

Find:

1. Ones digit
2. Tens digit
3. Hundreds digit
4. Thousands digit

### Expected Output

```text
Ones Digit: 9
Tens Digit: 2
Hundreds Digit: 8
Thousands Digit: 5
```

---

## Question 26 — Sum of Digits

Given:

```python
number = 583
```

Find the three digits and calculate their sum.

### Expected Output

```text
Sum of Digits: 16
```

---

## Question 27 — Four-Digit Sum

Given:

```python
number = 4726
```

Find all four digits and calculate their sum.

### Expected Output

```text
Sum of Digits: 19
```

---

## Question 28 — Product of Digits

Given:

```python
number = 234
```

Find the three digits and calculate their product.

### Expected Output

```text
Product of Digits: 24
```

---

## Question 29 — Reverse a Three-Digit Number

Given:

```python
number = 583
```

Create the reversed number using arithmetic operators.

### Expected Output

```text
Original Number: 583
Reversed Number: 385
```

---

## Question 30 — Reverse a Four-Digit Number

Given:

```python
number = 4726
```

Reverse the number using arithmetic operators.

### Expected Output

```text
Original Number: 4726
Reversed Number: 6274
```

---

## Question 31 — Place Value

Given:

```python
number = 5834
```

Display the place-value contribution of every digit.

### Expected Output

```text
Thousands Place: 5000
Hundreds Place: 800
Tens Place: 30
Ones Place: 4
```

---

## Question 32 — Difference Between First and Last Digit

Given:

```python
number = 583
```

Find the hundreds digit and ones digit and calculate their difference.

### Expected Output

```text
Difference: 2
```

---

## Question 33 — Digit Extraction Debugging

The program is intended to print the ones digit.

Find the error and correct the code.

```python
number = 583
ones = number / 10

print("Ones Digit:", ones)
```

Expected result:

```text
Ones Digit: 3
```

---

## Question 34 — Four-Digit Extraction

Write a program for:

```python
number = 9365
```

Print:

```text
Thousands Digit:
Hundreds Digit:
Tens Digit:
Ones Digit:
```

Use only `%` and `//` for extracting digits.

---

## Question 35 — Build a Number

Given:

```python
hundreds = 5
tens = 8
ones = 3
```

Use arithmetic operators to create the number `583`.

### Expected Output

```text
Number: 583
```

---

# Topic 4: Real-Life Arithmetic Problems

## Question 36 — Simple Interest

Given:

```text
Principal = ₹10000
Rate = 5%
Time = 2 years
```

Use:

```text
Simple Interest = (Principal × Rate × Time) / 100
```

Calculate the simple interest.

---

## Question 37 — Rectangle

A rectangle has:

```text
Length = 15 cm
Width = 8 cm
```

Calculate:

1. Area
2. Perimeter

Use:

```text
Area = length × width
Perimeter = 2 × (length + width)
```

---

## Question 38 — Circle

A circle has radius `7` cm.

Use:

```python
pi = 3.14
```

and:

```text
Area = π × r²
```

Calculate the area.

---

## Question 39 — Temperature Conversion

Given:

```python
celsius = 35
```

Convert Celsius into Fahrenheit.

Formula:

```text
Fahrenheit = (Celsius × 9 / 5) + 32
```

---

## Question 40 — Time Conversion

A video is `367` seconds long.

Use `//` and `%` to find complete minutes and remaining seconds.

### Expected Output

```text
Minutes: 6
Seconds: 7
```

---

## Question 41 — Hours, Minutes and Seconds

Given:

```python
total_seconds = 7384
```

Convert into:

- Hours
- Minutes
- Seconds

### Expected Output

```text
Hours: 2
Minutes: 3
Seconds: 4
```

---

## Question 42 — Salary Calculation

An employee has:

```text
Basic Salary = ₹25000
HRA = ₹5000
Travel Allowance = ₹2500
Tax Deduction = ₹3000
```

Calculate:

1. Gross salary
2. Net salary

---

## Question 43 — Travel Cost

A person travels `120` km.

The vehicle gives `20` km per litre and fuel costs ₹100 per litre.

Calculate:

1. Fuel required
2. Total fuel cost

---

## Question 44 — Shopping Discount

Given:

```python
price = "2500"
discount = "10"
```

Convert the values into suitable numeric types.

Calculate:

1. Discount amount
2. Final price

---

# Topic 5: Type Casting + Arithmetic Operators

## Question 45 — String Numbers

Given:

```python
price = "1200"
quantity = "4"
```

Convert both into integers and calculate the total price.

### Expected Output

```text
Price: 1200
Quantity: 4
Total Price: 4800
```

---

## Question 46 — Student Result

Marks are stored as strings:

```python
python_marks = "85"
math_marks = "78"
physics_marks = "91"
```

Convert them into integers and calculate:

1. Total marks
2. Average marks

---

## Question 47 — Bill with Tax

Given:

```python
price = "1500"
quantity = "2"
tax_rate = "5"
```

Convert the values and calculate:

1. Subtotal
2. Tax amount
3. Final bill

---

## Question 48 — Discount + GST

A product costs ₹2000.

Discount = 15%

GST = 18%

Apply the discount first and calculate GST on the discounted price.

Display:

1. Discount amount
2. Price after discount
3. GST amount
4. Final price

---

## Question 49 — Debug the Billing Program

Find all errors and write one correct version.

```python
price = "500"
quantity = 3

total = price + quantity

print("Total:", total)
```

The program should calculate the total price of 3 items costing ₹500 each.

---

## Question 50 — Debug the Marks Program

Find the error and correct the complete code.

```python
marks1 = "80"
marks2 = "75"
marks3 = "90"

total = marks1 + marks2 + marks3

print("Total Marks:", total)
```

### Expected Output

```text
Total Marks: 245
```

---

# Topic 6: Output Prediction and Conceptual Practice

## Question 51 — Type Casting Output

Predict the output:

```python
a = "50"
b = int(a)

print(a)
print(b)
print(type(a))
print(type(b))
```

---

## Question 52 — Float to Integer

Predict the output:

```python
number = 99.99
result = int(number)

print(number)
print(result)
```

Explain what happened to the decimal portion.

---

## Question 53 — Arithmetic Output

Predict the output:

```python
a = 12
b = 5

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
```

---

## Question 54 — Parentheses Challenge

Predict the outputs:

```python
print(10 + 5 * 2)
print((10 + 5) * 2)
print(20 / 5 + 3)
print(20 / (5 + 3))
```

Explain how parentheses changed the result.

---

## Question 55 — Digit Challenge

Predict the output:

```python
number = 684

a = number % 10
b = number // 10
c = b % 10
d = number // 100

print(a)
print(c)
print(d)
```

Identify which variable represents ones, tens, and hundreds.

---

# Topic 7: Mixed Debugging

## Question 56 — Debug the Student Program

Find all errors and write one corrected version.

```python
student_name = "Ravi"
marks = "85"

total = marks + 5

print("Student:", Student_name)
print("Marks:", total)
print("Type:", type(total)
```

---

## Question 57 — Debug the Number Program

The program should print the ones, tens, and hundreds digits of `746`.

```python
number = 746

ones = number / 10
tens = number // 10
hundreds = number // 100

print("Ones:", ones)
print("Tens:", tens)
print("Hundreds:", hundreds)
```

Correct the digit extraction expressions.

---

## Question 58 — Debug the Discount Program

Find the errors:

```python
price = "2000"
discount = "15"

discount_amount = price * discount / 100
final_price = price - discount_amount

print("Discount:", discount_amount)
print("Final Price:", final_price)
```

The program should calculate a 15% discount on ₹2000.

---

## Question 59 — Complete Debugging Challenge

The following program contains multiple errors.

```python
student_name = "Rahul"
marks1 = "85"
marks2 = "90"
marks3 = "78"

total = marks1 + marks2 + marks3
average = total / 3

print("Student:", Student_name)
print("Total Marks:", total)
print("Average:", average)
print("Marks Type:", type(total)
```

Correct the program.

### Expected Output

```text
Student: Rahul
Total Marks: 253
Average: 84.33333333333333
Marks Type: <class 'int'>
```

---

## Question 60 — Final Challenge: Number + Billing

Write one complete Python program containing two parts.

### Part A — Number Analysis

Given:

```python
number = 5836
```

Find:

- Thousands digit
- Hundreds digit
- Tens digit
- Ones digit
- Sum of digits
- Reversed number

### Part B — Product Billing

Given:

```python
price = "1250"
quantity = "4"
discount = "10"
```

Convert the values and calculate:

- Subtotal
- Discount amount
- Final amount