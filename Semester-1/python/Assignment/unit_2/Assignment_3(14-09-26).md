# Assignment 3 — Operators, Strings, Input & Output

**Deadline:** 14 September 26

## Objective

This assignment builds on the concepts already covered in Assignment 2 and focuses mainly on:

- Comparison Operators
- Assignment Operators
- Membership Operators with Strings
- Strings
- ASCII / Unicode
- `ord()` and `chr()`
- String Indexing
- String Slicing
- String `split()`
- `input()` and Output
- Escape Sequences
- f-strings
- `sep` and `end`
- Debugging
- Combining previous and new concepts

> **Important:** This assignment does **not** require `if`, `elif`, `else`, loops, functions, lists, dictionaries, bitwise operators, identity operators, or unary operators.

---

# Topic-1 — Comparison Operators

## Q1. Predict the Output

Predict the output before running the code.

```python
a = 15
b = 20

print(a < b)
print(a > b)
print(a == b)
print(a != b)
print(a <= b)
print(a >= b)
```

---

## Q2. Compare Expressions

Predict the output:

```python
x = 10
y = 10

print(x == y)
print(x != y)
print(x < y)
print(x <= y)
print(x >= y)
```

Pay special attention to the difference between `==` and `=`.

---

## Q3. Comparison with Arithmetic

Predict the output:

```python
a = 10
b = 5

print(a + b == 15)
print(a * b > 40)
print(a - b != 5)
print(a // b == 2)
```

---

## Q4. String Comparison

Predict the output:

```python
print("Python" == "Python")
print("Python" == "python")
print("Hello" != "hello")
```

What does this tell you about string comparison and case sensitivity?

---

# Topic-2 — Assignment Operators

## Q5. Trace the Value

Predict the final value of `x`:

```python
x = 20

x += 10
x -= 5
x *= 2
x //= 5

print(x)
```

Write the value of `x` after each statement.

---

## Q6. Assignment Operator Practice

Start with:

```python
marks = 50
```

Use assignment operators to:

1. Increase marks by `10`
2. Decrease marks by `5`
3. Multiply marks by `2`

Print the final value.

---

# Topic-3 — Membership Operators with Strings

## Q7. Basic Membership

Predict the output:

```python
text = "Python Programming"

print("Python" in text)
print("Java" in text)
print("Python" not in text)
```

---

## Q8. Character Membership

Given:

```python
word = "computer"
```

Write expressions to check:

1. Whether `"p"` is present.
2. Whether `"x"` is present.
3. Whether `"c"` is not present.

---

## Q9. Case Sensitivity in Membership

Predict the output:

```python
text = "Python"

print("P" in text)
print("p" in text)
print("Python" in text)
print("python" in text)
```

Explain why some results are different.

---

## Q10. Membership with User Input

Take a word or sentence as input and check whether the character `"a"` occurs in it.

### Test Cases

| Input | Expected Output |
|---|---|
| `apple` | `True` |
| `Python` | `False` |
| `banana` | `True` |

---

## Q11. Email Symbol Check

Take an email address as input and check whether `"@"` is present.

### Test Cases

| Input | Expected Output |
|---|---|
| `rahul@gmail.com` | `True` |
| `student@yahoo.com` | `True` |
| `rahulgmail.com` | `False` |

Use the string membership operator.

---

# Topic-4 — ASCII and Unicode

## Q12. Find Character Codes

Use `ord()` to find the Unicode code point of:

```text
A
a
Z
z
0
9
@
```

---

## Q13. Convert Codes to Characters

Use `chr()` to find the character represented by:

```text
65
66
97
98
48
57
64
```

---

## Q14. Uppercase and Lowercase

Use `ord()` to find the code points of:

```text
A
a
B
b
```

Answer:

1. Which is larger: `ord("A")` or `ord("a")`?
2. What is the difference between them?
3. Is the difference the same for `B` and `b`?

---

## Q15. Character Code Program

Take one character as input and print its Unicode code point.

### Test Cases

| Input | Expected Output |
|---|---|
| `A` | `65` |
| `a` | `97` |
| `0` | `48` |

---

## Q16. Next Character

Take a single uppercase English letter as input.

Use `ord()` and `chr()` to print the next character.

### Test Cases

| Input | Expected Output |
|---|---|
| `A` | `B` |
| `C` | `D` |
| `Y` | `Z` |

---

## Q17. Character Comparison and Unicode

Predict the output:

```python
print("A" < "B")
print("a" < "b")
print("A" < "a")
print("0" < "9")
```

Then use `ord()` to understand why the results occur.

---

## Q18. Unicode Character Challenge

Use `chr()` to display the characters represented by:

```text
9731
9829
8377
```

Then use `ord()` on those characters to verify the values.

---

# Topic-5 — String Indexing

## Q19. Basic Indexing

Given:

```python
text = "PYTHON"
```

Print:

1. First character
2. Second character
3. Last character
4. Second-last character

---

## Q20. Positive and Negative Indexing

Given:

```python
text = "COMPUTER"
```

Find the characters at:

```text
0
3
-1
-3
```

Write the Python expressions.

---

## Q21. Predict the Output

```python
text = "PYTHON"

print(text[0])
print(text[2])
print(text[-1])
print(text[-2])
```

---

## Q22. Indexing a User Input

Take a word from the user and print:

- First character
- Last character

### Test Cases

| Input | Expected Output |
|---|---|
| `Python` | `P` and `n` |
| `Computer` | `C` and `r` |
| `Hello` | `H` and `o` |

---

## Q23. Think Carefully About Indexing

Given:

```python
word = "PROGRAM"
```

Without running the code, determine:

```python
word[0]
word[2]
word[-1]
word[-4]
```

---

# Topic-6 — String Slicing

## Q24. Basic Slicing

Given:

```python
text = "PYTHON"
```

Predict:

```python
print(text[0:3])
print(text[2:5])
print(text[1:6])
```

---

## Q25. Start and Stop

Given:

```python
text = "PROGRAMMING"
```

Predict:

```python
print(text[:4])
print(text[4:])
print(text[:])
```

---

## Q26. Negative Slicing

Given:

```python
text = "COMPUTER"
```

Predict:

```python
print(text[-5:])
print(text[:-3])
print(text[-6:-2])
```

---

## Q27. Step in Slicing

Given:

```python
text = "PYTHON"
```

Predict:

```python
print(text[::2])
print(text[1::2])
print(text[::-1])
```

---

## Q28. Reverse a String

Take a string as input and reverse it using slicing.

### Test Cases

| Input | Expected Output |
|---|---|
| `Python` | `nohtyP` |
| `Hello` | `olleH` |
| `12345` | `54321` |

---

## Q29. Alternate Characters

Take a string as input and print every second character starting from index `0`.

### Test Cases

| Input | Expected Output |
|---|---|
| `ABCDEFGH` | `ACEG` |
| `Python` | `Pto` |
| `12345678` | `1357` |

---

## Q30. Extract First and Last Three Characters

Take a string as input and print:

- First three characters
- Last three characters

### Test Cases

| Input | First Three | Last Three |
|---|---|---|
| `Programming` | `Pro` | `ing` |
| `Computer` | `Com` | `ter` |
| `Python` | `Pyt` | `hon` |

Use slicing.

---

## Q31. Slicing Challenge

Given:

```python
text = "ABCDEFGHIJ"
```

Predict the output:

```python
print(text[2:8:2])
print(text[8:2:-2])
print(text[::-2])
```

For each expression, identify:

```text
start
stop
step
```

---

## Q32. Slice Without Counting from the Beginning

Take the string:

```python
text = "BTECH-CSE-2026"
```

Use slicing to extract:

```text
BTECH
CSE
2026
```

Do not manually write the extracted strings.

---

# Topic-7 — String `split()`

## Q33. Basic `split()`

Predict the output:

```python
text = "Python is easy"

print(text.split())
```

Explain what separates the words.

---

## Q34. Custom Separator

Predict the output:

```python
data = "apple,banana,mango"

print(data.split(","))
```

---

## Q35. Separator Not Present

Predict the output:

```python
text = "Python is easy"

print(text.split(","))
```

Why does it not split at the spaces?

---

## Q36. Split a Full Name

Take:

```text
Rahul Kumar Sharma
```

as input.

Use `.split()` and print each word on a separate line.

### Expected Output

```text
Rahul
Kumar
Sharma
```

---

## Q37. Multiple Inputs Using `split()`

Take two values from the user in one line.

Example:

```text
Input:
Rahul Kumar
```

Store them in:

```text
first_name
last_name
```

Then display:

```text
First Name: Rahul
Last Name: Kumar
```

---

## Q38. Three Numeric Inputs

Take three integers in one line using `.split()`.

Example:

```text
10 20 30
```

Convert them to integers and print their sum.

### Test Cases

| Input | Expected Output |
|---|---|
| `10 20 30` | `60` |
| `5 7 8` | `20` |
| `100 200 300` | `600` |

---

## Q39. Student Record

Input:

```text
Rahul,20,BTech,Ahmedabad
```

Use:

```python
.split(",")
```

to separate the information.

Display:

```text
Name: Rahul
Age: 20
Course: BTech
City: Ahmedabad
```

---

## Q40. Email Analyzer

Take an email address:

```text
rahul.kumar@gmail.com
```

Use `.split("@")` to separate:

- Username
- Domain

### Test Cases

| Input | Username | Domain |
|---|---|---|
| `rahul@gmail.com` | `rahul` | `gmail.com` |
| `student@yahoo.com` | `student` | `yahoo.com` |

---

## Q41. Sentence Analyzer

Take a sentence from the user.

Example:

```text
Python is very powerful
```

Use `.split()` to obtain the words.

Display:

```text
First word: Python
Last word: powerful
```

Also display the total number of words using the appropriate built-in operation.

---

# Topic-8 — Escape Sequences

## Q42. New Line

Write a statement that produces exactly:

```text
Hello
World
```

Use `\n`.

---

## Q43. Tab

Write a program that produces:

```text
Name:   Rahul
Age:    20
City:   Ahmedabad
```

Use `\t`.

---

## Q44. Backslash

Write a program that displays exactly:

```text
C:\Python\Programs
```

Use `\\`.

---

## Q45. Single Quote

Write a statement that displays:

```text
It's Python
```

Use an appropriate escape sequence.

---

## Q46. Double Quote

Write a statement that displays:

```text
He said "Hello"
```

Use an appropriate escape sequence.

---

## Q47. Predict the Output

```python
print("Python\nProgramming")
```

---

## Q48. Combined Escape Sequences

Write a program that displays:

```text
Student Details

Name:   Rahul
Age:    20
Course: B.Tech
```

Use `\n` and `\t`.

---

# Topic-9 — `print()`, `sep`, `end`, and f-Strings

## Q49. `sep`

Predict the output:

```python
print("2026", "09", "09", sep="-")
```

---

## Q50. `end`

Predict the output:

```python
print("Hello", end=" ")
print("Python")
```

---

## Q51. `sep` and `end`

Write a program that produces exactly:

```text
10-20-30
40-50-60
```

Use `sep` and `end`.

---

## Q52. Student Introduction

Take:

- Name
- Age
- City
- Course

Display them using an f-string:

```text
Name: Rahul
Age: 20
City: Ahmedabad
Course: B.Tech
```

---

## Q53. Formatted Price

Take a price as input and display it with exactly two decimal places.

### Test Cases

| Input | Expected Output |
|---|---|
| `45` | `45.00` |
| `99.5` | `99.50` |
| `120.678` | `120.68` |

Use an f-string.

---

# Topic-10 — Debugging

## Q54. String and Integer

Find and correct the error:

```python
age = input("Enter age: ")
print("Age after 5 years:", age + 5)
```

---

## Q55. Incorrect Quotes

Find and correct the error:

```python
print('It's Python')
```

---

## Q56. Incorrect Slicing Syntax

Find and correct the error:

```python
text = "Python"
print(text[1,4])
```

---

## Q57. Incorrect `split()` Separator

The program is:

```python
a, b = input().split(",")
```

The user enters:

```text
10 20
```

Why does the program fail?

Rewrite it correctly for the given input.

---

## Q58. String Addition vs Numeric Addition

What will this program print?

```python
a, b = input().split()

print(a + b)
```

Input:

```text
10 20
```

Then modify the program so that it performs numeric addition.

---

## Q59. Escape Sequence Debugging

Find and correct the problem:

```python
print("C:\new\test")
```

The programmer wants to display:

```text
C:\new\test
```

What special-character problem can occur here?

---

# Topic-11 — Integrated Problems

## Q60. Student Result Information

Take:

- Student name
- Three subject marks

Calculate:

- Total
- Average

Display the student's information using an f-string.

### Test Case

```text
Input:
Rahul
70 80 90
```

Expected:

```text
Name: Rahul
Total: 240
Average: 80.00
```

Use:

- `input()`
- `.split()`
- Type casting
- Arithmetic operators
- f-strings

---

## Q61. Student ID Analyzer

A student enters:

```text
BTECH-24-CSE-105
```

Write a program that:

1. Takes the ID as input.
2. Uses `.split("-")` to separate the parts.
3. Displays:
   - Degree
   - Batch
   - Branch
   - Roll Number
4. Uses string slicing to extract the last three characters from the original ID.
5. Converts the roll number into an integer.
6. Prints the roll number.

### Test Case

```text
Input:
BTECH-24-CSE-105
```

Expected:

```text
Degree: BTECH
Batch: 24
Branch: CSE
Roll Number: 105
```

---

## Q62. Username Generator

Take a three-word full name:

```text
Rahul Kumar Sharma
```

Use `.split()` and string indexing/slicing to create:

```text
rahul.sharma
```

Think carefully about:

- `.split()`
- Indexing
- Slicing
- String concatenation

Do not use any conditional statement.

---

## Q63. Sentence Information

Take:

```text
Python is very powerful
```

as input.

Use `.split()` and string indexing to display:

```text
First word: Python
Last word: powerful
```

Also display the number of words.

---

## Q64. Email Analyzer + Membership

Take an email address as input.

Use:

- Membership operator to check for `"@"`
- `.split("@")`
- String operations

For the input:

```text
rahul@gmail.com
```

display:

```text
@ Present: True
Username: rahul
Domain: gmail.com
```

---

## Q65. Character Analyzer

Take one character from the user.

Display:

- Character
- Unicode code point
- Previous character
- Next character

Use `ord()` and `chr()`.

### Test Case

```text
Input:
B
```

Expected:

```text
Character: B
Code: 66
Previous: A
Next: C
```

---

## Q66. Product Bill

Take:

- Product name
- Price
- Quantity
- Discount percentage

Calculate:

```text
Subtotal = price × quantity
Discount = subtotal × discount_percentage / 100
Final Total = subtotal - discount
```

Display the values using an f-string with two decimal places.

### Test Case

```text
Product: Pen
Price: 20
Quantity: 5
Discount: 10
```

Expected:

```text
Product: Pen
Price: 20.00
Quantity: 5
Subtotal: 100.00
Discount: 10.00
Final Total: 90.00
```

---

## Q67. Date Analyzer

Take a date in this format:

```text
09-09-2026
```

Use `.split("-")` to separate:

- Day
- Month
- Year

Display:

```text
Day: 09
Month: 09
Year: 2026
```

Then use string slicing on the original input to extract:

```text
2026
```

---

## Q68. String Transformation Challenge

Take:

```text
Python Programming
```

as input.

Use `.split()` and slicing to display:

```text
First Word: Python
Second Word: Programming
First Word Reversed: nohtyP
Second Word Reversed: gnimmargorP
```

---

## Q69. Final Challenge — Student Code Formatter

A student enters:

```text
BTECH-2026-CSE-105
```

Create a formatted output:

```text
Degree: BTECH
Batch: 2026
Branch: CSE
Roll: 105
Code: BTECH/CSE/105
```

Requirements:

1. Use `.split("-")`.
2. Use string indexing to access the required parts.
3. Use string slicing where appropriate.
4. Use string concatenation or an f-string for the final `Code`.
5. Do not manually write the extracted values.

### Test Case

```text
Input:
BTECH-2026-CSE-105
```

Expected:

```text
Degree: BTECH
Batch: 2026
Branch: CSE
Roll: 105
Code: BTECH/CSE/105
```

---


## Q70. Final String + Input/Output Challenge

Take a full name from the user in this format:

```text
Rahul Kumar Sharma
```

Create the following output:

```text
Original: Rahul Kumar Sharma
First Name: Rahul
Last Name: Sharma
First Name (Upper Part): RAH
Last Name (Lower Part): har
Full Name Reversed: amrahS ramuK luhaR
```

Requirements:

1. Use `input()`.
2. Use `.split()` to separate the words.
3. Use indexing to access the first and last name.
4. Use slicing to create the required parts.
5. Use `[::-1]` to reverse the complete original string.
6. Use an f-string for the final output.
7. Do not manually write the extracted values.

### Test Case

```text
Input:
Rahul Kumar Sharma
```

Expected:

```text
Original: Rahul Kumar Sharma
First Name: Rahul
Last Name: Sharma
First Name (Upper Part): RAH
Last Name (Lower Part): har
Full Name Reversed: amrahS ramuK luhaR
```

# Submission Guidelines

1. Write clean and readable Python code.
2. Use meaningful variable names.
3. Do not hard-code the values from the test cases.
4. Test every program with the provided test cases.
5. For output-prediction questions, write your prediction before running the code.
6. For debugging questions, identify the reason for the error before correcting it.
7. Use the requested Python feature where the question specifies it.
8. Do not use `if`, `elif`, `else`, loops, functions, lists, dictionaries, or other concepts that have not been covered.
9. Add short comments where the logic is not obvious.
10. Make sure syntax and indentation are correct.

---


