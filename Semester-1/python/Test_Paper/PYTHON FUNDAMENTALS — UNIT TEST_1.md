# PYTHON FUNDAMENTALS — UNIT TEST

**Course:** B.Tech — 1st Semester  
**Subject:** Python Programming  
**Time:** 60 Minutes  
**Maximum Marks:** 60

---

## Topics

Variables, Data Types, Type Casting, Numbers & Arithmetic Operators, Assignment Operators, Comparison Operators, ASCII/Unicode, Boolean & Logical Expressions, Strings, String `split()`, List Unpacking, Input & Output, Output Formatting, String Slicing

---

## General Instructions

1. Attempt all questions.
2. The total duration of the test is **60 minutes**.
3. In Section A, each question has **only ONE correct answer**.
4. Select only one option for each MCQ.
5. Write the complete Python program wherever required.
6. Do not use `if`, `elif`, `else`, loops, functions, or list indexing.
7. Use only the concepts covered in class.
8. For output-based questions, write the exact output.

---

# SECTION A — MULTIPLE CHOICE QUESTIONS

**20 × 1 = 20 Marks**  
**Suggested Time: 20 Minutes**

---

### Q1. 

What will be the output?

```python
x = 10
y = x
x = 25

print(x + y)
```

**A. 20**  **B. 25**  **C. 35**  **D. 50**

---

### Q2.

What is the data type of the value produced by the following expression?

```python
10 / 2
```

**A. `int`**  **B. `float`**  **C. `str`**  **D. `bool`**

---

### Q3.

What will be the output?

```python
x = "10"
y = 5

print(int(x) + y)
```

**A. 105**  **B. 15**  **C. `"105"`**  **D. Error**

---

### Q4.

What will be the output?

```python
print(20 // 6 + 20 % 6)
```

**A. 5**  **B. 6**  **C. 7**  **D. 8**

---

### Q5.

What is the final value of `x`?

```python
x = 4
x += 6
x *= 2
x -= 5
```

**A. 10**  **B. 15**  **C. 20**  **D. 25**

---

### Q6.

What will be printed?

```python
x = 10
y = 10

print(x > y)
```

**A. `True`**  **B. `False`**  **C. `10`**  **D. Error**

---

### Q7.

What will be the output?

```python
print(5 + 3 * 2 ** 2)
```

**A. 64**  **B. 17**  **C. 32**  **D. 20**

---

### Q8.

What will be the output?

```python
print(10 and 20)
```

**A. `True`**  **B. `False`**  **C. `10`**  **D. `20`**

---

### Q9.

What will be the output?

```python
print(0 or 15)
```

**A. `0`**  **B. `15`**  **C. `True`**  **D. `False`**

---

### Q10.

What will be the output?

```python
print(4 and 6 + 0 and 4)
```

**A. 4**  **B. 6**  **C. 0**  **D. 10**

---

### Q11.

What will be the output?

```python
print(0 or 7 + 6 or 0)
```

**A. 0**  **B. 6**  **C. 7**  **D. 13**

---

### Q12.

What will be the output?

```python
a = 10 and 6
b = 0 and 7

print(a + b)
```

**A. 0**  **B. 6**  **C. 10**  **D. 16**

---

### Q13.

What will be the output?

```python
print(not(5 > 2))
```

**A. `True`**  **B. `False`**  **C. `5`**  **D. `2`**

---

### Q14.

What will be the output?

```python
text = "Python"
print(len(text))
```

**A. 5**  **B. 6**  **C. 7**  **D. Error**

---

### Q15.

What will be the output?

```python
a = "10"
b = "20"

print(a + b)
```

**A. 30**  **B. `"30"`**  **C. `"1020"`**  **D. Error**

---

### Q16.

What is the value of `words` after executing the following code?

```python
text = "Python is easy"
words = text.split()
```

**A. `"Python is easy"`**  **B. `["Python", "is", "easy"]`**  **C. `["Python is easy"]`**  **D. `"Python,is,easy"`**

---

### Q17.

What will be the output?

```python
numbers = [10, 20, 30]
a, b, c = numbers

print(a + c)
```

**A. 30**  **B. 40**  **C. 50**  **D. Error**

---

### Q18.

What will be the output?

```python
print(ord("A") + ord("B"))
```

**A. 129**  **B. 130**  **C. 131**  **D. 132**

---

### Q19.

What is the data type of `age`?

```python
age = input("Enter age: ")
```

**A. `int`**  **B. `float`**  **C. `str`**  **D. `bool`**

---

### Q20.

What will be the output?

```python
age = "18"

print("Age: " + str(int(age) + 2))
```

**A. `Age: 18`**  **B. `Age: 20`**  **C. `Age: 182`**  **D. Error**

---

# SECTION B — PROGRAMMING & PROBLEM SOLVING

**10 × 3 = 30 Marks**  
**Suggested Time: 40 Minutes**

---

### Q21.

Write a Python program that takes a number from the user and displays:

- Original number
- Double of the number
- Triple of the number
- Square of the number

### Sample Input

```text
Enter number: 5
```

### Sample Output

```text
Number: 5
Double: 10
Triple: 15
Square: 25
```

---

### Q22.

Write a Python program that takes two numbers from the user and displays:

- Addition
- Subtraction
- Multiplication
- Division
- Floor Division
- Remainder

### Sample Input

```text
Enter first number: 17
Enter second number: 5
```

### Sample Output

```text
Addition: 22
Subtraction: 12
Multiplication: 85
Division: 3.4
Floor Division: 3
Remainder: 2
```

---

### Q23.

Write a Python program that takes a three-digit number as input and displays:

- Hundreds digit
- Tens digit
- Units digit
- Sum of digits

### Sample Input

```text
Enter number: 583
```

### Sample Output

```text
Hundreds digit: 5
Tens digit: 8
Units digit: 3
Sum: 16
```

---

### Q24.

Write a Python program that takes a three-digit number as input and constructs its reverse.

### Sample Input

```text
Enter number: 583
```

### Sample Output

```text
Original: 583
Reverse: 385
```

---

### Q25.

Write a Python program that takes marks of three subjects from the user and calculates:

- Total marks
- Average marks

### Sample Input

```text
Physics: 80
Maths: 90
Python: 85
```

### Sample Output

```text
Total: 255
Average: 85.0
```

---

### Q26.

A student buys:

- 3 notebooks at ₹40 each
- 2 pens at ₹15 each
- 1 calculator at ₹250

Write a Python program to calculate and display the total bill.

### Sample Output

```text
Notebook Total: ₹120
Pen Total: ₹30
Calculator: ₹250
Total Bill: ₹400
```

---

### Q27.

Write a Python program that takes a word from the user and displays:

- Original word
- Length
- Uppercase word
- Lowercase word

### Sample Input

```text
Enter word: Python
```

### Sample Output

```text
Word: Python
Length: 6
Uppercase: PYTHON
Lowercase: python
```

---

### Q28.

Write a Python program that takes the following string:

```text
Programming
```

and displays:

- The first 4 characters
- The last 4 characters
- All characters except the first and last character
- The string in reverse order

Use **negative indexing/slicing wherever applicable**.

### Expected Output

```text
First 4 characters: Prog
Last 4 characters: ming
Middle characters: rogrammin
Reverse: gnimmargorP
```

---

### Q29.

Write a Python program that takes a sentence containing exactly three words from the user.

Use `split()` and list unpacking to store the three words in three variables and display them separately.

### Sample Input

```text
Enter sentence: Learn Python Daily
```

### Sample Output

```text
First Word: Learn
Second Word: Python
Third Word: Daily
```

---

### Q30.

Write a Python program that takes one character from the user and displays:

- Its ASCII/Unicode value
- The character represented by ASCII value `65`

### Sample Input

```text
Enter character: B
```

### Sample Output

```text
ASCII value of B: 66
Character for 65: A
```
---

# TIME MANAGEMENT

| Section | Questions | Marks | Time |
|---|---:|---:|---:|
| Section A — MCQ | 20 | 20 | 20 min |
| Section B — Programming | 10 | 30 | 40 min |
| Section C — Integrated Programming | 2 | 10 | 12 min |
| **Total Solving Time** | **32** | **60** | **60 min** |
| **Review / Buffer** | — | — | **3 min** |
| **Total Test Duration** | | **60 Marks** | **60 min** |

---

# END OF QUESTION PAPER