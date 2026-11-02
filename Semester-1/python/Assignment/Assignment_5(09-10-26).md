# Assignment 5 — Single `for` Loop: Logic Building & Problem Solving

**Topics:** `for` loop, `range()`, loop variable, counters, accumulators, `if` inside a loop, strings, indexing, slicing, digit logic, factorial-style problems, loop tracing, and real-life problem solving

> **Core Rule:** Every programming question must be solved using **one `for` loop only**. Do not use nested loops.

---

# Objective

This assignment is intentionally designed beyond basic “print 1 to 10” exercises. It starts with a few loop-flow questions and then moves quickly into problems where students must **think about what should happen in every iteration**.

The progression is:

**Loop Flow → `range()` → Counting & Accumulation → Factorial/Product Logic → Number & Digit Logic → String Logic → Tricky Problems → Real-Life Problems → Final Challenges**

The main mental model is:

> **Start → Repeat → Process → Update → Finish**

---

# Important Rules

1. Use **exactly one `for` loop** for every programming question.
2. **Do not use nested loops.**
3. Do not use `while`, `break`, or `continue`.
4. You may use `if`, `elif`, and `else` inside the single `for` loop.
5. Do not use lists, dictionaries, sets, or functions unless a question explicitly allows them.
6. Do not hard-code the answer for the given test cases.
7. Use `%` and `//` for number/digit problems where requested.
8. For string questions, use indexing/slicing and character iteration where appropriate.
9. If a question says **without `len()`**, do not use `len()`.
10. If a question says **without `max()` / `min()`**, do not use them.
11. For output-prediction questions, do not run the code before predicting.
12. Keep the solution limited to the concepts already taught in class.

---

# Level 1 — Loop Thinking & `range()`

## Q1. Predict the Loop Values

Without running the code, write the values printed:

```python
for i in range(2, 15, 3):
    print(i)
```

### Expected Output

Write the exact output.

---

## Q2. Reverse `range()` Prediction

Predict the output:

```python
for i in range(15, 2, -3):
    print(i)
```

---

## Q3. How Many Iterations?

Without running the program, determine how many times the loop executes and list the values of `i`.

```python
for i in range(4, 31, 5):
    print(i)
```

---

## Q4. Correct the Boundary

A student wants to print every third number from `3` through `18`:

```python
for i in range(3, 18, 3):
    print(i)
```

Correct the program so that `18` is also printed.

### Expected Output

```text
3
6
9
12
15
18
```

---

## Q5. Number and Distance from 20

Print each number from `5` to `10` along with its distance from `20`.

### Expected Output

```text
5 15
6 14
7 13
8 12
9 11
10 10
```

---

## Q6. Number, Square and Cube

For every number from `1` to `6`, print the number, its square, and its cube on one line.

### Expected Output

```text
1 1 1
2 4 8
3 9 27
4 16 64
5 25 125
6 36 216
```

---

# Level 2 — Counting & Accumulation

## Q7. Sum of Numbers in a Range

Take `start` and `end`. Find the sum of all integers from `start` to `end` using one `for` loop.

### Test Cases

```text
Input: 5 10 | Output: 45
Input: 12 15 | Output: 54
```

---

## Q8. Count Multiples of 3

Take `N` and count how many numbers from `1` to `N` are divisible by `3`.

### Test Cases

```text
Input: 10 | Output: 3
Input: 20 | Output: 6
```

---

## Q9. Sum of Multiples of 4

Take `N` and calculate the sum of all numbers from `1` to `N` divisible by `4`.

### Test Cases

```text
Input: 20 | Output: 60
Input: 30 | Output: 112
```

---

## Q10. Count Numbers with Two Conditions

Take `N` and count numbers from `1` to `N` that are divisible by **both 3 and 5**.

### Test Cases

```text
Input: 50 | Output: 3
Input: 100 | Output: 6
```

---

## Q11. Sum Numbers Except Multiples of 3

Take `N` and find the sum of numbers from `1` to `N` that are **not divisible by 3**.

### Test Cases

```text
Input: 10 | Output: 37
Input: 15 | Output: 80
```

---

## Q12. Count Even and Odd Together

Take `N`. Using one loop, count how many numbers from `1` to `N` are even and how many are odd.

### Test Cases

```text
Input: 10 | Output: Even = 5, Odd = 5
Input: 7 | Output: Even = 3, Odd = 4
```

---

## Q13. Running Sum

Take `N`. Print the running sum after every number from `1` to `N`.

### Test Case

```text
Input: 5
```

### Expected Output

```text
1
3
6
10
15
```

---

## Q14. Running Product

Take `N`. Starting with `1`, multiply by every number from `1` to `N` and print the product after each iteration.

### Test Case

```text
Input: 5
```

### Expected Output

```text
1
2
6
24
120
```

---

# Level 3 — Factorial & Product Logic

## Q15. Factorial of a Number

Take an integer `N` and calculate `N!` using a `for` loop.

### Test Cases

```text
Input: 5 | Output: 120
Input: 7 | Output: 5040
```

---

## Q16. Factorial from 1 to N

Take `N` and print the factorial of every number from `1` to `N`.

### Test Case

```text
Input: 5
```

### Expected Output

```text
1! = 1
2! = 2
3! = 6
4! = 24
5! = 120
```

---

## Q17. Product of Even Numbers

Take `N` and find the product of all even numbers from `2` to `N`.

### Test Cases

```text
Input: 10 | Output: 3840
Input: 6 | Output: 48
```

---

## Q18. Product of Odd Numbers

Take `N` and find the product of all odd numbers from `1` to `N`.

### Test Cases

```text
Input: 7 | Output: 105
Input: 9 | Output: 945
```

---

## Q19. Double Factorial — Even Numbers

Take an even number `N`. Calculate:

`N × (N-2) × (N-4) × ... × 2`

Use one `for` loop.

### Test Cases

```text
Input: 8 | Output: 384
Input: 10 | Output: 3840
```

---

## Q20. Sum of Squares

Take `N` and calculate:

`1² + 2² + 3² + ... + N²`

### Test Cases

```text
Input: 5 | Output: 55
Input: 10 | Output: 385
```

---

## Q21. Sum of Cubes

Take `N` and calculate:

`1³ + 2³ + 3³ + ... + N³`

### Test Cases

```text
Input: 4 | Output: 100
Input: 5 | Output: 225
```

---

## Q22. Factorial-Based Sum

Take `N` and calculate:

`1! + 2! + 3! + ... + N!`

Use only one `for` loop.

### Test Cases

```text
Input: 4 | Output: 33
Input: 5 | Output: 153
```

---

# Level 4 — Number & Digit Logic

## Q23. Count Digits Using a Loop

Take a positive integer and count its digits using a `for` loop. Do not convert the number to a string.

### Test Cases

```text
Input: 58321 | Output: 5
Input: 904 | Output: 3
```

---

## Q24. Sum of Digits

Take an integer and find the sum of its digits using one `for` loop.

### Test Cases

```text
Input: 58321 | Output: 19
Input: 907 | Output: 16
```

---

## Q25. Product of Digits

Take an integer and find the product of its digits.

### Test Cases

```text
Input: 234 | Output: 24
Input: 105 | Output: 0
```

---

## Q26. Count Even Digits

Count how many digits of a given integer are even.

### Test Cases

```text
Input: 58321 | Output: 2
Input: 24680 | Output: 5
```

---

## Q27. Sum of Even Digits

Find the sum of only the even digits of a number.

### Test Cases

```text
Input: 58321 | Output: 10
Input: 24681 | Output: 20
```

---

## Q28. Largest Digit Without `max()`

Find the largest digit of a number using one `for` loop. Do not use `max()` and do not convert the number to a string.

### Test Cases

```text
Input: 58321 | Output: 8
Input: 40796 | Output: 9
```

---

## Q29. Smallest Digit Without `min()`

Find the smallest digit of a number using one `for` loop. Do not use `min()`.

### Test Cases

```text
Input: 58321 | Output: 1
Input: 40796 | Output: 0
```

---

## Q30. Reverse a Number

Reverse the digits of a positive integer using one `for` loop and `%` / `//`.

### Test Cases

```text
Input: 58321 | Output: 12385
Input: 12040 | Output: 4021
```

---

## Q31. Palindrome Number

Check whether a number reads the same from left to right and right to left. Use one `for` loop.

### Test Cases

```text
Input: 1221 | Output: Palindrome
Input: 1234 | Output: Not Palindrome
```

---

## Q32. Count a Specific Digit

Take an integer and a target digit. Count how many times that digit occurs.

### Test Cases

```text
Input: 1223342, 2 | Output: 3
Input: 505550, 5 | Output: 4
```

---

## Q33. First Digit Using Repeated Division

Find the first/leftmost digit of a positive integer using a `for` loop and repeated integer division. Do not convert the number to a string.

### Test Cases

```text
Input: 58321 | Output: 5
Input: 9047 | Output: 9
```

---

## Q34. Difference Between Largest and Smallest Digit

Find the largest digit and smallest digit of a number, then print their difference. Do not use `max()` or `min()`.

### Test Cases

```text
Input: 58321 | Output: 7
Input: 40796 | Output: 9
```

---

## Q35. Digit Position Value

Take a positive integer and print each digit with its position from the right, starting from position `1`.

### Test Case

```text
Input: 58321
```

### Expected Output

```text
1 1
2 2
3 3
8 4
5 5
```

The first value is the digit and the second value is its position from the right.

---

## Q36. Armstrong Number — 3 Digit

Take a 3-digit number and check whether it is an Armstrong number.

For example:

`153 = 1³ + 5³ + 3³`

### Test Cases

```text
Input: 153 | Output: Armstrong Number
Input: 123 | Output: Not Armstrong Number
```

---

# Level 5 — String & Character Logic

## Q37. Print Characters with Index

Take a string and print every character along with its index.

### Test Case

```text
Input: Python
```

### Expected Output

```text
0 P
1 y
2 t
3 h
4 o
5 n
```

---

## Q38. Count Characters Without `len()`

Take a string and find its length without using `len()`. Use a `for` loop to count the characters.

### Test Cases

```text
Input: Python | Output: 6
Input: Hello World | Output: 11
```

---

## Q39. Count Vowels and Consonants

Take a string containing English letters and spaces. Count vowels and consonants using one `for` loop. Ignore spaces.

### Test Cases

```text
Input: Python | Output: Vowels = 1, Consonants = 5
Input: Hello World | Output: Vowels = 3, Consonants = 7
```

---

## Q40. Character Frequency

Take a string and a target character. Count how many times the target appears.

### Test Cases

```text
Input: programming, g | Output: 2
Input: banana, a | Output: 3
```

---

## Q41. First Occurrence Position

Take a string and a target character. Find the index of the **first occurrence** of that character.

If it does not occur, print `Not Found`.

### Test Cases

```text
Input: programming, g | Output: 3
Input: banana, n | Output: 2
Input: Python, z | Output: Not Found
```

> **Hint:** Think carefully about how a variable can remember the first position found.

---

## Q42. Count Uppercase and Lowercase

Take a string containing English letters. Count uppercase and lowercase characters using one `for` loop.

### Test Cases

```text
Input: PyThOn | Output: Uppercase = 3, Lowercase = 3
Input: HelloWORLD | Output: Uppercase = 6, Lowercase = 4
```

---

## Q43. Character Code Analyzer

Take a string and print every character along with its Unicode value using `ord()`.

### Test Case

```text
Input: ABC
```

### Expected Output

```text
A 65
B 66
C 67
```

---

## Q44. String Without Vowels

Take a string and print all characters except vowels. Preserve the original order.

### Test Cases

```text
Input: education | Output: dctn
Input: Python | Output: Pythn
```

---

# Level 6 — Midpoint, Half & String Logic

## Q45. Find the Middle Character

Take a string and find its middle character using its length and indexing.

For this question, assume the string length is odd.

### Test Cases

```text
Input: Python | Output: h
Input: abcde | Output: c
```

---

## Q46. First Half and Second Half

Take a string with an even number of characters. Find and print its first half and second half.

### Test Cases

```text
Input: PythonCode
Output:
First Half: Pytho
Second Half: nCode

Input: ABCDEF
Output:
First Half: ABC
Second Half: DEF
```

---

## Q47. Split a String by Length — Odd vs Even

Take a string as input.

Use the string length and a **single `for` loop** to divide the string into halves.

- If the length is **odd**:
  - Print the first half.
  - Print the middle character.
  - Print the second half.
- If the length is **even**:
  - Print the first half.
  - Print the second half.
- Do not use slicing to directly obtain the final halves.
- Use one `for` loop for the character-processing logic.

### Test Cases

```text
Input: PROGRAM
Output:
First Half: PRO
Middle: G
Second Half: RAM

Input: PYTHON
Output:
First Half: PYT
Second Half: HON

Input: HELLO
Output:
First Half: HE
Middle: L
Second Half: LO
```
## Q48. Compare Two Halves

Take a string of even length. Split it logically into two equal halves and check whether both halves are identical.

Use one `for` loop.

### Test Cases

```text
Input: ABCABC | Output: Equal Halves
Input: ABCABD | Output: Different Halves
Input: XYZXYZ | Output: Equal Halves
```

---

## Q49. Mirror the String

Take a string and determine whether its first and last characters match, second and second-last match, and so on.

Print `Symmetric` if all corresponding characters match; otherwise print `Not Symmetric`.

Use one `for` loop.

### Test Cases

```text
Input: ABCCBA | Output: Symmetric
Input: ABCD | Output: Not Symmetric
Input: MADAM | Output: Symmetric
```

---

## Q50. Alternate Character Extraction

Take a string and print characters at even indexes only.

### Test Cases

```text
Input: ABCDEFGH | Output: ACEG
Input: Python | Output: Pto
```

---

## Q51. Count Characters at Even and Odd Indexes

Take a string and count how many characters occur at even indexes and how many occur at odd indexes.

### Test Cases

```text
Input: Python | Output: Even Index = 3, Odd Index = 3
Input: ABCDE | Output: Even Index = 3, Odd Index = 2
```

---

## Q52. Swap Adjacent Characters

Take a string with an even number of characters. Print the string after swapping every adjacent pair.

Example:

`ABCDEFGH → BADCFEHG`

Use one `for` loop.

### Test Cases

```text
Input: ABCD | Output: BADC
Input: ABCDEFGH | Output: BADCFEHG
```

---

# Level 7 — Tricky Single-Loop Problems

## Q53. Second Largest Digit

Take a number and find the **second largest distinct digit** using one `for` loop.

Do not use `sort()`, `max()`, or convert the number to a string.

### Test Cases

```text
Input: 58321 | Output: 5
Input: 987654 | Output: 8
Input: 99852 | Output: 8
```

> Repeated digits should not count twice. For example, in `99852`, the largest digit is `9` and the second largest distinct digit is `8`.

---

## Q54. Longest Consecutive Equal Character Run

Take a string and find the length of the longest consecutive run of the same character.

### Test Cases

```text
Input: aaabbccccd | Output: 4
Input: programming | Output: 2
Input: abcde | Output: 1
```

> You must solve this with one `for` loop. Think about a **current count** and a **best count**.

---

## Q55. Most Frequent Character — Controlled Approach

Take a string and a target character. Count how many times the target occurs and compare it with the number of characters in the string to determine its frequency percentage.

Use one `for` loop. Do not use dictionaries.

### Test Cases

```text
Input: banana, a | Output: Count = 3, Frequency = 50.0%
Input: programming, g | Output: Count = 2, Frequency = 18.18%
```

> The challenge is to maintain the count and calculate the final percentage correctly.

---

## Q56. Running Digit Sum Until the End

Take a positive integer. Process its digits from right to left and print the running sum after each digit is processed.

### Test Case

```text
Input: 58321
```

### Expected Output

```text
1
3
6
14
19
```

---

## Q57. Number with Most Even Digits

Take a positive integer and determine whether it contains more even digits or more odd digits.

### Test Cases

```text
Input: 24681 | Output: More Even Digits
Input: 13579 | Output: More Odd Digits
Input: 1234 | Output: Equal
```

---

## Q58. Alternating Digit Sum

Take a positive integer. Starting from the **rightmost digit**, add the 1st digit, subtract the 2nd digit, add the 3rd digit, subtract the 4th digit, and continue this pattern.

Use exactly one `for` loop and `%` / `//`.

### Test Cases

```text
Input: 12345 | Output: 3
Input: 58321 | Output: -1
Input: 2468 | Output: 4
```

For `12345`:

`5 - 4 + 3 - 2 + 1 = 3`

> This question tests whether you can maintain changing logic from one iteration to the next.

---

## Q59. Output Prediction — Accumulator Trap

Predict the output without running the code:

```python
total = 0
for i in range(1, 6):
    total = total + i * 2
    print(total)
```

### Expected Output

Write the exact five lines.

---

## Q60. Output Prediction — Condition Inside Loop

Predict the output:

```python
count = 0
for i in range(1, 11):
    if i % 2 == 0:
        count = count + 1
print(count)
```

Explain why the final value is what it is.

---

## Q61. Debug the Accumulator

The following program is intended to calculate `1 + 2 + 3 + 4 + 5`, but it is incorrect:

```python
sum = 0
for i in range(1, 6):
    sum = i
print(sum)
```

1. Identify the mistake.
2. Correct the program.
3. Explain what should happen to the accumulator in every iteration.

### Expected Output

```text
15
```

---

# Level 8 — Real-Life Single-Loop Problems

## Q62. Daily Expense Analyzer

Take the number of days and then enter the expense for each day. Using one `for` loop, calculate:

- total expense
- highest expense
- lowest expense

### Test Case

```text
Input: 5
Expenses: 250 180 400 120 300
```

### Expected Output

```text
Total: 1250
Highest: 400
Lowest: 120
```

---

## Q63. Student Marks Analyzer

Take the number of subjects and enter marks one by one. Using one `for` loop, calculate:

- total marks
- average marks
- highest marks
- lowest marks

### Test Case

```text
Input: 5
Marks: 78 65 92 81 74
```

### Expected Output

```text
Total: 390
Average: 78.0
Highest: 92
Lowest: 65
```

---

## Q64. Attendance Analyzer

Take the number of working days. For each day, input `P` for Present or `A` for Absent. Count present days, absent days, and calculate attendance percentage.

### Test Case

```text
Input: 6
Status: P P A P A P
```

### Expected Output

```text
Present: 4
Absent: 2
Attendance: 66.67%
```

---

## Q65. Electricity Usage Analyzer

Take the number of days and the electricity units used each day. Calculate total units and the number of days where usage was above `10` units.

### Test Case

```text
Input: 5
Units: 8 12 15 7 13
```

### Expected Output

```text
Total Units: 55
Days Above 10: 3
```

---

## Q66. Shopping Bill Analyzer

Take the number of products and their prices. Using one `for` loop, calculate the total bill and count how many products cost more than `1000`.

### Test Case

```text
Input: 5
Prices: 450 1200 800 2500 600
```

### Expected Output

```text
Total Bill: 5550
Products Above 1000: 2
```

---

## Q67. Login Attempt Analyzer

Take `N` login attempts. For each attempt, input `success` or `failed`. Count successful and failed attempts and calculate the success percentage.

### Test Case

```text
Input: 5
Attempts: success failed success failed success
```

### Expected Output

```text
Successful: 3
Failed: 2
Success Rate: 60.0%
```

---

# Level 9 — Final Challenges

## Q68. Number Profile

Take a positive integer and, using exactly one `for` loop, find all of the following:

- number of digits
- sum of digits
- largest digit
- smallest digit
- number of even digits
- number of odd digits

Do not convert the number to a string. Do not use `max()` or `min()`.

### Test Case

```text
Input: 58321
```

### Expected Output

```text
Digits: 5
Sum: 19
Largest: 8
Smallest: 1
Even Digits: 2
Odd Digits: 3
```

---

## Q69. String Balance Challenge

Take a string containing letters. Using exactly one `for` loop, calculate:

- total characters
- vowels
- consonants
- uppercase characters
- lowercase characters
- characters at even indexes

Ignore spaces when counting vowels/consonants/uppercase/lowercase, but include them in total characters and index positions.

### Test Case

```text
Input: Hello World
```

### Expected Output

```text
Total Characters: 11
Vowels: 3
Consonants: 7
Uppercase: 2
Lowercase: 8
Even Index Characters: 6
```

---

# Submission Checklist

Before submitting, check:

- [ ] I used exactly **one `for` loop** in every programming question.
- [ ] I did not use nested loops.
- [ ] I did not use `while`, `break`, or `continue`.
- [ ] I understand what my loop variable represents.
- [ ] I initialize counters and accumulators before the loop.
- [ ] I update counters/accumulators inside the correct iteration.
- [ ] I used `%` and `//` correctly for digit problems.
- [ ] I did not use `max()` / `min()` where prohibited.
- [ ] I tested my program with the given test cases.
- [ ] I can explain what happens in at least one iteration of every solution.

> **Important:** The goal of this assignment is not simply to make the program produce the expected output. You should understand **why the loop produces that output**.
