# PYTHON FUNDAMENTALS --- UNIT TEST

**Course:** B.Tech --- 1st Semester\
**Subject:** Python Programming\
**Time:** 80 Minutes\
**Maximum Marks:** 80

------------------------------------------------------------------------

## Topics

Conditional Statements (`if`, `if-else`, `if-elif-else`, nested
conditions), logical conditions, `for` loops, `while` loops, `range()`,
`break`, `continue`, and basic problem-solving using conditions and
loops.

------------------------------------------------------------------------

## General Instructions

1.  Attempt all questions.
2.  The total duration of the test is **80 minutes**.
3.  In Section A, each question has **only ONE correct answer**.
4.  Select only one option for each MCQ.
5.  Write complete Python programs wherever required.
6.  Use only the concepts covered in class.
7.  For output-based questions, write the exact output.
8.  Unless a question says otherwise, assume the input is valid.
9.  Do not use lists, dictionaries, or functions unless explicitly
    required.

------------------------------------------------------------------------

# SECTION A --- MULTIPLE CHOICE QUESTIONS

**15 × 1 = 15 Marks**\
**Suggested Time: 15 Minutes**

------------------------------------------------------------------------

### Q1. What will be the output?

``` python
x = 7

if x > 5:
    print("A")
print("B")
```

**A.** `A` only  **B.** `B` only  **C.** `A` then `B`  **D.** Error

------------------------------------------------------------------------

### Q2. What will be the output?

``` python
num = 8

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```

**A.** `Odd`  **B.** `Even`  **C.** `8`  **D.** Error

------------------------------------------------------------------------

### Q3. What will be printed?

``` python
marks = 72

if marks >= 80:
    print("A")
elif marks >= 60:
    print("B")
else:
    print("C")
```

**A.** `A`  **B.** `B`  **C.** `C`  **D.** Nothing

------------------------------------------------------------------------

### Q4. What will be the output?

``` python
x = 10

if x > 5:
    if x < 12:
        print("Yes")
    else:
        print("No")
```

**A.** `Yes`  **B.** `No`  **C.** `Yes` then `No`  **D.** Nothing

------------------------------------------------------------------------

### Q5. What will be printed?

``` python
x = 4

if x > 2 and x < 5:
    print("Inside")
else:
    print("Outside")
```

**A.** `Inside`  **B.** `Outside`  **C.** `True`  **D.** Error

------------------------------------------------------------------------

### Q6. How many times will the loop execute?

``` python
for i in range(2, 8, 2):
    print(i)
```

**A.** 2  **B.** 3  **C.** 4  **D.** 6

------------------------------------------------------------------------

### Q7. What will be the output?

``` python
for i in range(1, 4):
    print(i, end=" ")
```

**A.** `1 2 3`  **B.** `1 2 3 4`  **C.** `0 1 2 3`  **D.** `2 3 4`

------------------------------------------------------------------------

### Q8. What is the final value of `total`?

``` python
total = 0

for i in range(1, 5):
    total += i

print(total)
```

**A.** 4  **B.** 6  **C.** 10  **D.** 15

------------------------------------------------------------------------

### Q9. What will be the output?

``` python
i = 1

while i < 4:
    print(i, end=" ")
    i += 1
```

**A.** `1 2 3`  **B.** `1 2 3 4`  **C.** `0 1 2 3`  **D.** Infinite loop

------------------------------------------------------------------------

### Q10. What will be printed?

``` python
for i in range(5):
    if i == 3:
        break
    print(i, end=" ")
```

**A.** `0 1 2`  **B.** `0 1 2 3`  **C.** `1 2 3`  **D.** `0 1 2 3 4`

------------------------------------------------------------------------

### Q11. What will be printed?

``` python
for i in range(5):
    if i == 2:
        continue
    print(i, end=" ")
```

**A.** `0 1 2 3 4`  **B.** `0 1 3 4`  **C.** `2` only  **D.** `0 1`

------------------------------------------------------------------------

### Q12. What will be the output?

``` python
count = 0

for i in range(1, 6):
    if i % 2 == 0:
        count += 1

print(count)
```

**A.** 1  **B.** 2  **C.** 3  **D.** 5

------------------------------------------------------------------------

### Q13. What will be printed?

``` python
for i in range(3, 0, -1):
    print(i, end=" ")
```

**A.** `1 2 3`  **B.** `3 2 1`  **C.** `3 2 1 0`  **D.** Nothing

------------------------------------------------------------------------

### Q14. How many times will the body of this loop execute?

``` python
for i in range(4, 4):
    print(i)
```

**A.** 0  **B.** 1  **C.** 4  **D.** Infinite times

------------------------------------------------------------------------

### Q15. What will be the output?

``` python
x = 1

while x <= 5:
    x += 2

print(x)
```

**A.** 5  **B.** 6  **C.** 7  **D.** 8

------------------------------------------------------------------------

# SECTION B --- PROGRAMMING & PROBLEM SOLVING

**8 Questions = 32 Marks**\
**Suggested Time: 32 Minutes**

Write a complete Python program for each question. Each question carries
**4 marks**.

------------------------------------------------------------------------

### Q16. Positive, Negative, or Zero

Take an integer from the user and display whether it is positive,
negative, or zero.

**Sample Input**

``` text
Enter a number: -7
```

**Sample Output**

``` text
Negative
```

------------------------------------------------------------------------

### Q17. Greatest of Two Numbers

Take two numbers from the user and print the greater number. If both
numbers are equal, print `Both numbers are equal`.

**Sample Input**

``` text
Enter first number: 12
Enter second number: 12
```

**Sample Output**

``` text
Both numbers are equal
```

------------------------------------------------------------------------

### Q18. Grade Calculator

Take marks out of 100 and display the grade using these rules:

-   90--100: A
-   75--89: B
-   60--74: C
-   40--59: D
-   Below 40: Fail

Assume the input is between 0 and 100.

**Sample Input**

``` text
Enter marks: 78
```

**Sample Output**

``` text
Grade: B
```

------------------------------------------------------------------------

### Q19. Sum from 1 to N

Take a positive integer `N` and calculate the sum of all integers from
`1` to `N` using a loop.

**Sample Input**

``` text
Enter N: 5
```

**Sample Output**

``` text
Sum: 15
```

------------------------------------------------------------------------

### Q20. Multiplication Table

Take an integer from the user and print its multiplication table from 1
to 10.

**Sample Input**

``` text
Enter number: 4
```

**Sample Output**

``` text
4 x 1 = 4
4 x 2 = 8
4 x 3 = 12
4 x 4 = 16
4 x 5 = 20
4 x 6 = 24
4 x 7 = 28
4 x 8 = 32
4 x 9 = 36
4 x 10 = 40
```

------------------------------------------------------------------------

### Q21. Count Even Numbers

Take a positive integer `N` and count how many even numbers exist from
`1` to `N`, inclusive.

**Sample Input**

``` text
Enter N: 10
```

**Sample Output**

``` text
Even count: 5
```

------------------------------------------------------------------------

### Q22. Number of Digits

Take a positive integer and count its digits using a `while` loop. Do
not convert the number to a string.

**Sample Input**

``` text
Enter number: 58321
```

**Sample Output**

``` text
Number of digits: 5
```

------------------------------------------------------------------------

### Q23. Reverse Counting with a Condition

Take a positive integer `N` and print the numbers from `N` down to `1`,
but skip numbers divisible by 3. Use a loop and `continue`.

**Sample Input**

``` text
Enter N: 7
```

**Sample Output**

``` text
7 5 4 2 1
```

------------------------------------------------------------------------

# SECTION C --- INTEGRATED PROBLEM SOLVING

**2 Questions = 13 Marks**\
**Suggested Time: 13 Minutes**

------------------------------------------------------------------------

### Q24. Find the Factorial

**6 Marks**

Take a non-negative integer `N` and calculate its factorial using a
loop.

The factorial of `N` is the product of all integers from `1` to `N`. The
factorial of `0` is `1`.

**Sample Input**

``` text
Enter N: 5
```

**Sample Output**

``` text
Factorial: 120
```

**Another Test Case**

``` text
Input: 0
Output: Factorial: 1
```

------------------------------------------------------------------------

### Q25. Check Whether a Number Is Prime

**7 Marks**

Take an integer greater than `1` and determine whether it is a prime
number using a loop and conditional statements.

A prime number has exactly two positive factors: `1` and itself.

**Sample Input**

``` text
Enter number: 13
```

**Sample Output**

``` text
13 is a prime number
```

**Another Test Case**

``` text
Input: 12
Output: 12 is not a prime number
```

------------------------------------------------------------------------

# SECTION D — PATTERN PRINTING

**4 × 5 = 20 Marks**  
**Suggested Time: 20 Minutes**

Write a Python program for each pattern. Use nested loops where appropriate. Match the spacing and line breaks shown in the expected output.

---

### Q26. Right-Angled Star Triangle

Take an integer `N` and print a right-angled triangle of stars with `N` rows.

**Sample Input**
```text
Enter N: 4
```

**Expected Output**
```text
*
* *
* * *
* * * *
```

---

### Q27. Inverted Number Triangle

Take an integer `N` and print numbers from `1` to the current row number, starting with `N` numbers in the first row and decreasing by one number in each following row.

**Sample Input**
```text
Enter N: 4
```

**Expected Output**
```text
1 2 3 4
1 2 3
1 2
1
```

---

### Q28. Increasing Number Triangle

Take an integer `N` and print the following pattern. Each row contains the row number repeated that many times.

**Sample Input**
```text
Enter N: 4
```

**Expected Output**
```text
1
2 2
3 3 3
4 4 4 4
```

---

### Q29. Centered Star Pyramid

Take an odd or even positive integer `N` representing the number of rows and print a centered star pyramid. Each row should have leading spaces followed by stars separated by single spaces.

**Sample Input**
```text
Enter N: 4
```

**Expected Output**
```text
   *
  * *
 * * *
* * * *
```

---

# END OF QUESTION PAPER
