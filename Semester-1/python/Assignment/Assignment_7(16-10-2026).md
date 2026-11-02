# Assignment-7

**Topic:** Python While Loop

**Instruction:** Predict the exact output of each program before running it. Pay attention to the condition, statement order, indentation, and variable updates. Write **No output** if nothing is printed and **Infinite loop** if the program does not terminate.

------------------------------------------------------------------------

## Type 1: Output Guessing

### Level 1: Understand the Basic Flow

### Q1. Simple Counting

``` python
i = 1

while i <= 4:
    print(i)
    i += 1
```

**Predicted output:**

``` text
```

### Q2. Counting by Two

``` python
n = 2

while n <= 8:
    print(n, end=" ")
    n += 2
```

**Predicted output:**

``` text
```

### Q3. Reverse Counting

``` python
x = 5

while x >= 1:
    print(x, end=" ")
    x -= 1
```

**Predicted output:**

``` text
```

### Q4. The Condition Is Initially False

``` python
count = 7

while count < 5:
    print("Hello")
    count += 1

print("Finished")
```

**Predicted output:**

``` text
```

------------------------------------------------------------------------

### Level 2: Track the Order of Statements

### Q5. Update Before Printing

``` python
i = 1

while i <= 4:
    i += 1
    print(i, end=" ")
```

**Predicted output:**

``` text
```

### Q6. Print After the Loop

``` python
n = 1

while n <= 3:
    print(n, end=" ")
    n += 1

print("Done")
```

**Predicted output:**

``` text
```

### Q7. Two Updates in One Iteration

``` python
x = 1

while x < 10:
    print(x, end=" ")
    x += 2
    x += 1
```

**Predicted output:**

``` text
```

### Q8. Change the Variable Before Checking Again

``` python
value = 10

while value > 0:
    value -= 3
    print(value, end=" ")
```

**Predicted output:**

``` text
```

------------------------------------------------------------------------

### Level 3: Arithmetic and Accumulation

### Q9. Add the Counter Values

``` python
i = 1
total = 0

while i <= 4:
    total += i
    i += 1

print(total)
```

**Predicted output:**

``` text
```

### Q10. Multiply During Each Iteration

``` python
n = 1
result = 1

while n <= 4:
    result *= 2
    n += 1

print(result)
```

**Predicted output:**

``` text
```

### Q11. Use the Remainder Operator

``` python
n = 11

while n > 0:
    print(n % 3, end=" ")
    n -= 4
```

**Predicted output:**

``` text
```

### Q12. Integer Division

``` python
number = 583

while number > 0:
    print(number // 10, end=" ")
    number //= 10
```

**Predicted output:**

``` text
```

------------------------------------------------------------------------

### Level 4: Conditions and Logical Thinking

### Q13. Print Only When a Condition Is True

``` python
i = 1

while i <= 6:
    if i % 2 == 0:
        print(i, end=" ")
    i += 1
```

**Predicted output:**

``` text
```

### Q14. A Conditional Expression Inside a Loop

``` python
n = 1

while n <= 5:
    print("Even" if n % 2 == 0 else "Odd", end=" ")
    n += 1
```

**Predicted output:**

``` text
```

### Q15. The Condition Changes Inside the Loop

``` python
x = 1

while x < 10:
    print(x, end=" ")
    x *= 2
```

**Predicted output:**

``` text
```

### Q16. A Tricky Starting Value

``` python
i = 5

while i > 0:
    print(i, end=" ")
    i -= 2

print("Stop:", i)
```

**Predicted output:**

``` text
```

------------------------------------------------------------------------

### Level 5: Strings and Tricky Cases

### Q17. Build a String Repeatedly

``` python
i = 1
result = ""

while i <= 4:
    result += "A"
    print(result)
    i += 1
```

**Predicted output:**

``` text
```

### Q18. A String Variable Changes Each Time

``` python
word = "PY"

while len(word) < 6:
    print(word)
    word += "T"

print(word)
```

**Predicted output:**

``` text
```

### Q19. Does the Loop Run at All?

``` python
x = 3

while x > 10:
    print("Inside")
    x += 1

print(x)
```

**Predicted output:**

``` text
```

### Q20. Find the Problem

``` python
i = 1

while i <= 4:
    print(i, end=" ")
    i -= 1

print("Finished")
```

**What happens when this program runs?**

Choose one: - A. It prints `1 2 3 4 Finished` - B. It prints
`1 0 -1 -2 ...` and continues indefinitely - C. It prints nothing - D.
It produces a syntax error

**Your answer and reasoning:**

``` text
```

------------------------------------------------------------------------

## Type 2: Basic While Loop Problems — Statement Based

**Instructions:** Solve each problem using **one `while` loop only**. Do not use lists, nested loops, or functions. Read the input and output format carefully. Test cases show sample inputs and the expected outputs.

### Level 1: Basic Counting

### Q21. Print Numbers from 1 to N

**Task:** Take a positive integer `N` and print all numbers from `1` to `N`, each on a new line.

**Input:**
```text
5
```

**Expected Output:**
```text
1
2
3
4
5
```

**Test Cases:**

| Input | Expected Output |
|---|---|
| `3` | `1`<br>`2`<br>`3` |
| `1` | `1` |
| `6` | `1`<br>`2`<br>`3`<br>`4`<br>`5`<br>`6` |

### Q22. Print Numbers from N to 1

**Task:** Take a positive integer `N` and print the numbers in descending order, from `N` to `1`.

**Input:**
```text
5
```

**Expected Output:**
```text
5
4
3
2
1
```

**Test Cases:**

| Input | Expected Output |
|---|---|
| `3` | `3`<br>`2`<br>`1` |
| `1` | `1` |
| `4` | `4`<br>`3`<br>`2`<br>`1` |

### Q23. Print Even Numbers up to N

**Task:** Take a positive integer `N` and print all even numbers from `2` up to `N`. If `N` is odd, stop at the last even number below it.

**Input:**
```text
10
```

**Expected Output:**
```text
2
4
6
8
10
```

**Test Cases:**

| Input | Expected Output |
|---|---|
| `7` | `2`<br>`4`<br>`6` |
| `4` | `2`<br>`4` |
| `1` | No output |

### Q24. Print Odd Numbers up to N

**Task:** Take a positive integer `N` and print all odd numbers from `1` up to `N`.

**Input:**
```text
9
```

**Expected Output:**
```text
1
3
5
7
9
```

**Test Cases:**

| Input | Expected Output |
|---|---|
| `6` | `1`<br>`3`<br>`5` |
| `5` | `1`<br>`3`<br>`5` |
| `1` | `1` |

### Q25. Print Multiples of a Number

**Task:** Take two positive integers, `K` and `N`. Print the multiples of `K` that are less than or equal to `N`.

**Input:**
```text
K = 3
N = 15
```

**Expected Output:**
```text
3
6
9
12
15
```

**Test Cases:**

| Input | Expected Output |
|---|---|
| `K = 4, N = 18` | `4`<br>`8`<br>`12`<br>`16` |
| `K = 5, N = 12` | `5`<br>`10` |
| `K = 7, N = 6` | No output |

------------------------------------------------------------------------

### Level 2: Counting with Small Changes

### Q26. Multiplication Table

**Task:** Take an integer `N` and print its multiplication table from `N × 1` to `N × 10`.

**Input:**
```text
4
```

**Expected Output:**
```text
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

**Test Cases:**

| Input | Expected Output |
|---|---|
| `2` | Print the table of 2 from `2 x 1 = 2` to `2 x 10 = 20` |
| `5` | Print the table of 5 from `5 x 1 = 5` to `5 x 10 = 50` |

### Q27. Count by a Given Step

**Task:** Take two positive integers, `START` and `STEP`. Starting from `START`, print the next five values, adding `STEP` after each value. Print exactly five numbers.

**Input:**
```text
START = 2
STEP = 3
```

**Expected Output:**
```text
2
5
8
11
14
```

**Test Cases:**

| Input | Expected Output |
|---|---|
| `START = 1, STEP = 2` | `1`<br>`3`<br>`5`<br>`7`<br>`9` |
| `START = 10, STEP = 5` | `10`<br>`15`<br>`20`<br>`25`<br>`30` |

### Q28. Sum of Numbers from 1 to N

**Task:** Take a positive integer `N` and calculate the sum of all integers from `1` to `N`. Print only the final sum.

**Input:**
```text
5
```

**Expected Output:**
```text
15
```

**Test Cases:**

| Input | Expected Output |
|---|---|
| `3` | `6` |
| `1` | `1` |
| `10` | `55` |

### Q29. Sum of Even Numbers up to N

**Task:** Take a positive integer `N` and calculate the sum of all even numbers from `2` up to `N`.

**Input:**
```text
10
```

**Expected Output:**
```text
30
```

**Test Cases:**

| Input | Expected Output |
|---|---|
| `6` | `12` |
| `9` | `20` |
| `1` | `0` |

### Q30. Sum of Odd Numbers up to N

**Task:** Take a positive integer `N` and calculate the sum of all odd numbers from `1` up to `N`.

**Input:**
```text
7
```

**Expected Output:**
```text
16
```

**Test Cases:**

| Input | Expected Output |
|---|---|
| `5` | `9` |
| `8` | `16` |
| `1` | `1` |

------------------------------------------------------------------------

### Level 3: Simple Repeated Calculations

### Q31. Calculate the Total Cost

**Task:** A shop sells one notebook for `PRICE` rupees. Take the price of one notebook and the number of notebooks purchased, `QUANTITY`. Calculate the total cost using repeated addition.

**Input:**
```text
PRICE = 20
QUANTITY = 4
```

**Expected Output:**
```text
80
```

**Test Cases:**

| Input | Expected Output |
|---|---|
| `PRICE = 15, QUANTITY = 3` | `45` |
| `PRICE = 7, QUANTITY = 5` | `35` |
| `PRICE = 50, QUANTITY = 1` | `50` |

### Q32. Calculate Total Savings

**Task:** A student saves the same amount of money every day. Take `DAILY_SAVING` and `DAYS`. Calculate the total amount saved after that many days using a loop.

**Input:**
```text
DAILY_SAVING = 25
DAYS = 6
```

**Expected Output:**
```text
150
```

**Test Cases:**

| Input | Expected Output |
|---|---|
| `DAILY_SAVING = 10, DAYS = 7` | `70` |
| `DAILY_SAVING = 50, DAYS = 2` | `100` |
| `DAILY_SAVING = 12, DAYS = 1` | `12` |

### Q33. Calculate a Number Raised to a Power

**Task:** Take two non-negative integers, `BASE` and `POWER`. Calculate `BASE` raised to `POWER` using repeated multiplication. Assume `POWER` is between `0` and `8`.

**Input:**
```text
BASE = 3
POWER = 4
```

**Expected Output:**
```text
81
```

**Test Cases:**

| Input | Expected Output |
|---|---|
| `BASE = 2, POWER = 3` | `8` |
| `BASE = 5, POWER = 1` | `5` |
| `BASE = 7, POWER = 0` | `1` |

### Q34. Calculate Factorial

**Task:** Take a non-negative integer `N` and calculate its factorial. The factorial of `N` is the product of all integers from `1` to `N`. Remember that `0! = 1`.

**Input:**
```text
5
```

**Expected Output:**
```text
120
```

**Test Cases:**

| Input | Expected Output |
|---|---|
| `3` | `6` |
| `4` | `24` |
| `0` | `1` |

### Q35. Find the Sum from START to END

**Task:** Take two integers, `START` and `END`, where `START` is less than or equal to `END`. Calculate the sum of all integers from `START` through `END`, including both endpoints.

**Input:**
```text
START = 3
END = 7
```

**Expected Output:**
```text
25
```

**Test Cases:**

| Input | Expected Output |
|---|---|
| `START = 1, END = 4` | `10` |
| `START = 5, END = 5` | `5` |
| `START = 10, END = 12` | `33` |

------------------------------------------------------------------------

### Level 4: Read the Condition Carefully

### Q36. Count Down by Two

**Task:** Take a positive even integer `N`. Print numbers from `N` down to `2`, decreasing by `2` each time.

**Input:**
```text
10
```

**Expected Output:**
```text
10
8
6
4
2
```

**Test Cases:**

| Input | Expected Output |
|---|---|
| `6` | `6`<br>`4`<br>`2` |
| `2` | `2` |
| `12` | `12`<br>`10`<br>`8`<br>`6`<br>`4`<br>`2` |

### Q37. Repeatedly Divide by Two

**Task:** Take a positive integer `N`. Print the value of `N` after repeatedly applying integer division by `2`. Continue while the value is greater than `0`. Print each new value after dividing.

**Input:**
```text
20
```

**Expected Output:**
```text
10
5
2
1
0
```

**Test Cases:**

| Input | Expected Output |
|---|---|
| `8` | `4`<br>`2`<br>`1`<br>`0` |
| `5` | `2`<br>`1`<br>`0` |
| `2` | `1`<br>`0` |

### Q38. Count How Many Steps Are Needed

**Task:** Start with a positive integer `N`. In each step, subtract `3` from the number. Continue until the value becomes less than or equal to `0`. Print the number of steps taken.

**Input:**
```text
N = 11
```

**Expected Output:**
```text
4
```

**Test Cases:**

| Input | Expected Output |
|---|---|
| `N = 10` | `4` |
| `N = 6` | `2` |
| `N = 2` | `1` |

### Q39. Save Until the Target Is Reached

**Task:** A student already has `SAVED` rupees and adds `DAILY_AMOUNT` rupees each day. Calculate how many days are needed for the savings to become greater than or equal to `TARGET`. Assume `SAVED` is less than `TARGET` and `DAILY_AMOUNT` is positive.

**Input:**
```text
SAVED = 20
DAILY_AMOUNT = 15
TARGET = 70
```

**Expected Output:**
```text
4
```

**Test Cases:**

| Input | Expected Output |
|---|---|
| `SAVED = 0, DAILY_AMOUNT = 10, TARGET = 35` | `4` |
| `SAVED = 25, DAILY_AMOUNT = 25, TARGET = 75` | `2` |
| `SAVED = 5, DAILY_AMOUNT = 7, TARGET = 20` | `3` |

### Q40. Print a Number Sequence in Reverse Steps

**Task:** Take two positive integers, `START` and `STEP`, where `START` is divisible by `STEP`. Print values starting from `START`, subtracting `STEP` each time, and stop after printing `0`.

**Input:**
```text
START = 20
STEP = 5
```

**Expected Output:**
```text
20
15
10
5
0
```

**Test Cases:**

| Input | Expected Output |
|---|---|
| `START = 12, STEP = 3` | `12`<br>`9`<br>`6`<br>`3`<br>`0` |
| `START = 8, STEP = 2` | `8`<br>`6`<br>`4`<br>`2`<br>`0` |
| `START = 9, STEP = 3` | `9`<br>`6`<br>`3`<br>`0` |

------------------------------------------------------------------------

**Reminder:** Use one `while` loop per question. Focus on initializing variables, checking the condition, updating the variable, and deciding when the loop should stop.


------------------------------------------------------------------------

## Type 3: Factorial and Number & Digit Logic

**Instructions:** Solve each problem using a single `while` loop. Do not use lists, nested loops, or functions. Assume number inputs are non-negative unless the statement says positive. Read each test case carefully and handle `0` where required.

### Level 1: Basic Digit Logic

### Q41. Count the Digits

**Task:** Take a non-negative integer `N` and count how many digits it contains. Treat `0` as a one-digit number.

**Input:**
```text
58321
```

**Expected Output:**
```text
5
```

**Test Cases:**

| Input | Expected Output |
|---|---:|
| `58321` | `5` |
| `700` | `3` |
| `0` | `1` |
| `9` | `1` |

### Q42. Find the Sum of Digits

**Task:** Take a non-negative integer and calculate the sum of its digits.

**Input:**
```text
583
```

**Expected Output:**
```text
16
```

**Test Cases:**

| Input | Expected Output |
|---|---:|
| `583` | `16` |
| `204` | `6` |
| `999` | `27` |
| `0` | `0` |

### Q43. Reverse a Number

**Task:** Take a non-negative integer and print its digits in reverse order as a number. Leading zeroes in the reversed result are not displayed.

**Input:**
```text
5830
```

**Expected Output:**
```text
385
```

**Test Cases:**

| Input | Expected Output |
|---|---:|
| `583` | `385` |
| `1204` | `4021` |
| `700` | `7` |
| `0` | `0` |

### Q44. Find the Product of Digits

**Task:** Take a non-negative integer and calculate the product of all its digits. The product of the digits of `0` is `0`.

**Input:**
```text
234
```

**Expected Output:**
```text
24
```

**Test Cases:**

| Input | Expected Output |
|---|---:|
| `234` | `24` |
| `105` | `0` |
| `777` | `343` |
| `0` | `0` |

### Q45. Print Digits from Right to Left

**Task:** Take a positive integer and print one digit per line, starting from the rightmost digit and moving left.

**Input:**
```text
58321
```

**Expected Output:**
```text
1
2
3
8
5
```

**Test Cases:**

| Input | Expected Output |
|---|---|
| `407` | `7`<br>`0`<br>`4` |
| `91` | `1`<br>`9` |
| `6` | `6` |

------------------------------------------------------------------------

### Level 2: Work with Specific Digits

### Q46. Find the First and Last Digit

**Task:** Take a positive integer and print its first digit and last digit on separate lines. The first digit is the leftmost digit.

**Input:**
```text
58321
```

**Expected Output:**
```text
First digit: 5
Last digit: 1
```

**Test Cases:**

| Input | Expected Output |
|---|---|
| `704` | `First digit: 7`<br>`Last digit: 4` |
| `9` | `First digit: 9`<br>`Last digit: 9` |
| `1200` | `First digit: 1`<br>`Last digit: 0` |

### Q47. Count Even Digits

**Task:** Take a non-negative integer and count how many of its digits are even. Zero is an even digit.

**Input:**
```text
583204
```

**Expected Output:**
```text
4
```

**Test Cases:**

| Input | Expected Output |
|---|---:|
| `583204` | `4` |
| `13579` | `0` |
| `2468` | `4` |
| `0` | `1` |

### Q48. Count Odd Digits

**Task:** Take a non-negative integer and count how many of its digits are odd.

**Input:**
```text
583204
```

**Expected Output:**
```text
2
```

**Test Cases:**

| Input | Expected Output |
|---|---:|
| `583204` | `2` |
| `2468` | `0` |
| `13579` | `5` |
| `0` | `0` |

### Q49. Find the Sum of Even Digits

**Task:** Take a non-negative integer and calculate the sum of only its even digits.

**Input:**
```text
583204
```

**Expected Output:**
```text
14
```

**Test Cases:**

| Input | Expected Output |
|---|---:|
| `583204` | `14` |
| `2468` | `20` |
| `13579` | `0` |
| `0` | `0` |

### Q50. Find the Largest Digit

**Task:** Take a non-negative integer and find the largest digit present in it.

**Input:**
```text
583204
```

**Expected Output:**
```text
8
```

**Test Cases:**

| Input | Expected Output |
|---|---:|
| `583204` | `8` |
| `1947` | `9` |
| `222` | `2` |
| `0` | `0` |

### Q51. Find the Smallest Digit

**Task:** Take a non-negative integer and find the smallest digit present in it.

**Input:**
```text
583204
```

**Expected Output:**
```text
0
```

**Test Cases:**

| Input | Expected Output |
|---|---:|
| `583204` | `0` |
| `1947` | `1` |
| `222` | `2` |
| `8` | `8` |

------------------------------------------------------------------------

### Level 3: Combine Digit Logic

### Q52. Check Whether a Number Is a Palindrome

**Task:** A number is a palindrome if it reads the same from left to right and right to left. Take a non-negative integer and print `Palindrome` or `Not Palindrome`. Do not convert the number to a string.

**Input:**
```text
1221
```

**Expected Output:**
```text
Palindrome
```

**Test Cases:**

| Input | Expected Output |
|---|---|
| `121` | `Palindrome` |
| `123` | `Not Palindrome` |
| `7` | `Palindrome` |
| `100` | `Not Palindrome` |

### Q53. Count How Many Times a Digit Appears

**Task:** Take a non-negative integer `N` and a digit `D` from `0` to `9`. Count how many times digit `D` appears in `N`.

**Input:**
```text
N = 505250
D = 5
```

**Expected Output:**
```text
3
```

**Test Cases:**

| Input | Expected Output |
|---|---:|
| `N = 505250, D = 5` | `3` |
| `N = 12345, D = 7` | `0` |
| `N = 7007, D = 7` | `2` |
| `N = 0, D = 0` | `1` |

### Q54. Check Whether All Digits Are the Same

**Task:** Take a positive integer and print `Yes` if every digit is the same; otherwise, print `No`.

**Input:**
```text
7777
```

**Expected Output:**
```text
Yes
```

**Test Cases:**

| Input | Expected Output |
|---|---|
| `7777` | `Yes` |
| `7077` | `No` |
| `5` | `Yes` |
| `222` | `Yes` |

### Q55. Compare the Sum of First and Last Digits with the Middle Digits' Sum

**Task:** Take a positive integer with at least three digits. Find the sum of its first and last digits. Separately, find the sum of all digits between the first and last digits. Print both sums on separate lines. Do not convert the number to a string.

**Input:**
```text
58321
```

**Expected Output:**
```text
First and last digits sum: 6
Middle digits sum: 13
```

**Test Cases:**

| Input | Expected Output |
|---|---|
| `58321` | `First and last digits sum: 6`<br>`Middle digits sum: 13` |
| `12345` | `First and last digits sum: 6`<br>`Middle digits sum: 9` |
| `90218` | `First and last digits sum: 17`<br>`Middle digits sum: 3` |

------------------------------------------------------------------------

### Level 4: Factorial Practice

### Q56. Print Factorial Values from 1! to N!

**Task:** Take a positive integer `N`. Print the factorial value for every number from `1` to `N`, one result per line. Use one loop and update the factorial result as the number increases.

**Input:**
```text
5
```

**Expected Output:**
```text
1
2
6
24
120
```

**Test Cases:**

| Input | Expected Output |
|---|---|
| `3` | `1`<br>`2`<br>`6` |
| `4` | `1`<br>`2`<br>`6`<br>`24` |
| `1` | `1` |

### Q57. Check Whether a Number Is a Factorial Value

**Task:** Take a positive integer `N`. Print `Yes` if `N` is equal to the factorial of some non-negative integer; otherwise, print `No`. Examples of factorial values are `1`, `2`, `6`, `24`, and `120`.

**Input:**
```text
24
```

**Expected Output:**
```text
Yes
```

**Test Cases:**

| Input | Expected Output |
|---|---|
| `6` | `Yes` |
| `25` | `No` |
| `1` | `Yes` |
| `120` | `Yes` |

### Q58. Find the Largest Factorial Not Greater Than N

**Task:** Take a positive integer `N`. Find the largest factorial value that is less than or equal to `N`. Consider `1` as the starting factorial value.

**Input:**
```text
20
```

**Expected Output:**
```text
6
```

**Test Cases:**

| Input | Expected Output |
|---|---:|
| `5` | `2` |
| `6` | `6` |
| `20` | `6` |
| `100` | `24` |

------------------------------------------------------------------------

**Reminder:** Every question in Type 3 should be solved using a single `while` loop. Use `% 10` to get the last digit and `// 10` to remove the last digit when solving digit-based problems. For factorial questions, keep a running product and update it carefully. Do not use lists, nested loops, or functions.


------------------------------------------------------------------------

## Type 4: Output Guessing — Nested `while` Loops, `break`, and `continue`

**Instructions:** Predict the exact output of each program before running it. Track every variable carefully. Pay attention to indentation, when the inner loop starts and stops, and whether `break` or `continue` affects the inner loop or the outer loop.

For every question:
- Write the exact output, including spaces and line breaks.
- If nothing is printed, write **No output**.
- Do not run the code until you have made your prediction.
- These are output-guessing questions; do not write a program to solve them.

### Level 1: Understand Nested `while` Loops

### Q59. Two Loops, Two Values

```python
i = 1

while i <= 2:
    j = 1

    while j <= 3:
        print(i, j)
        j += 1

    i += 1
```

**Predicted output:**

```text

```

### Q60. Print Values on the Same Line

```python
i = 1

while i <= 3:
    j = 1

    while j <= 2:
        print(j, end=" ")
        j += 1

    print()
    i += 1
```

**Predicted output:**

```text

```

### Q61. Different Inner Loop Limits

```python
i = 1

while i <= 3:
    j = 1

    while j <= i:
        print("*", end=" ")
        j += 1

    print()
    i += 1
```

**Predicted output:**

```text

```

### Q62. Outer Value Changes the Inner Starting Point

```python
i = 1

while i <= 3:
    j = i

    while j <= 3:
        print(j, end=" ")
        j += 1

    print()
    i += 1
```

**Predicted output:**

```text

```

### Q63. Print After the Inner Loop

```python
i = 1

while i <= 3:
    j = 1

    while j <= 2:
        print(j, end=" ")
        j += 1

    print("End")
    i += 1
```

**Predicted output:**

```text

```

---

### Level 2: Trace the Flow Carefully

### Q64. Print After Both Loops

```python
i = 1

while i <= 2:
    j = 1

    while j <= 2:
        print(i + j)
        j += 1

    i += 1

print("Finished")
```

**Predicted output:**

```text

```

### Q65. Two Separate `while` Loops

```python
i = 1

while i <= 2:
    print("A", i)
    i += 1

j = 1

while j <= 3:
    print("B", j)
    j += 1
```

**Predicted output:**

```text

```

### Q66. Inner Counter Is Not Reset

```python
i = 1
j = 1

while i <= 3:
    while j <= 2:
        print(i, j)
        j += 1

    i += 1
```

**Predicted output:**

```text

```

### Q67. Update the Outer Variable After the Inner Loop

```python
i = 1

while i <= 3:
    j = 1

    while j <= 2:
        print(i, end="")
        j += 1

    print()
    i += 2
```

**Predicted output:**

```text

```

### Q68. Inner Loop Depends on the Outer Variable

```python
i = 1

while i <= 3:
    j = 1

    while j < i:
        print(j, end=" ")
        j += 1

    print("X")
    i += 1
```

**Predicted output:**

```text

```

---

### Level 3: Nested Loops with `break`

### Q69. Break the Inner Loop

```python
i = 1

while i <= 3:
    j = 1

    while j <= 4:
        if j == 3:
            break

        print(i, j)
        j += 1

    i += 1
```

**Predicted output:**

```text

```

### Q70. Break After Printing a Value

```python
i = 1

while i <= 2:
    j = 1

    while j <= 4:
        print(j, end=" ")

        if j == 2:
            break

        j += 1

    print("|")
    i += 1
```

**Predicted output:**

```text

```

### Q71. Break Condition Is Never Reached

```python
i = 1

while i <= 2:
    j = 1

    while j <= 2:
        if j == 5:
            break

        print(i, j)
        j += 1

    i += 1
```

**Predicted output:**

```text

```

### Q72. `break` Does Not Stop the Outer Loop

```python
i = 1

while i <= 3:
    j = 1

    while j <= 3:
        if j == 2:
            break

        print(i, j)
        j += 1

    print("Next row")
    i += 1
```

**Predicted output:**

```text

```

---

### Level 4: Nested Loops with `continue`

### Q73. Skip One Inner-Loop Value

```python
i = 1

while i <= 2:
    j = 0

    while j < 4:
        j += 1

        if j == 2:
            continue

        print(i, j)

    i += 1
```

**Predicted output:**

```text

```

### Q74. Continue After Updating the Counter

```python
i = 1

while i <= 5:
    i += 1

    if i == 3:
        continue

    print(i, end=" ")
```

**Predicted output:**

```text

```

### Q75. Continue in the Inner Loop

```python
i = 1

while i <= 3:
    j = 0

    while j < 3:
        j += 1

        if j == 2:
            continue

        print(j, end=" ")

    print("Row")
    i += 1
```

**Predicted output:**

```text

```

### Q76. `continue` Does Not Skip the Whole Outer Loop

```python
i = 1

while i <= 3:
    j = 1

    while j <= 3:
        if j == i:
            j += 1
            continue

        print(i, j)
        j += 1

    i += 1
```

**Predicted output:**

```text

```

---

### Level 5: Combine Nested Loops, `break`, and `continue`

### Q77. Skip One Value, Then Break

```python
i = 1

while i <= 2:
    j = 0

    while j < 5:
        j += 1

        if j == 2:
            continue

        if j == 4:
            break

        print(i, j)

    i += 1
```

**Predicted output:**

```text

```

### Q78. Predict the Complete Output

```python
i = 1

while i <= 3:
    j = 1

    while j <= 4:
        if j == 2:
            j += 1
            continue

        if i == 3 and j == 4:
            break

        print(i * j, end=" ")
        j += 1

    print("End")
    i += 1

print("Done")
```

**Predicted output:**

```text

```

---

**Reminder:** In a nested loop, `break` exits the nearest loop containing it. `continue` skips the remaining statements in the current iteration of the nearest loop containing it. Always check which loop the statement belongs to by following indentation.


------------------------------------------------------------------------

## Type 5: Statement-Based Programming Problems — Single and Nested `while` Loops

**Instructions:**
- Solve each problem using `while` loops.
- Questions Q79–Q86 should use **one `while` loop only**.
- Questions Q87–Q98 should use **nested `while` loops**.
- Do not use lists, tuples, sets, dictionaries, or user-defined functions.
- Read the input/output format and test cases carefully.
- For number problems, do not convert the number to a string unless the task explicitly allows it.

### Part A: Single `while` Loop Problems

### Q79. Check Whether a Number Is Prime

**Task:** Take a positive integer `N`. Print `Prime` if it is a prime number; otherwise, print `Not Prime`. A prime number is greater than `1` and has exactly two positive factors.

**Input:**
```text
17
```

**Expected Output:**
```text
Prime
```

**Test Cases:**

| Input | Expected Output |
|---|---|
| `2` | `Prime` |
| `12` | `Not Prime` |
| `1` | `Not Prime` |
| `29` | `Prime` |

### Q80. Find the HCF (GCD) of Two Numbers

**Task:** Take two positive integers `A` and `B`. Find their highest common factor (HCF), also called the greatest common divisor (GCD), using a `while` loop.

**Input:**
```text
A = 18
B = 24
```

**Expected Output:**
```text
6
```

**Test Cases:**

| Input | Expected Output |
|---|---:|
| `A = 6, B = 120` | `6` |
| `A = 25, B = 15` | `5` |
| `A = 7, B = 9` | `1` |
| `A = 12, B = 12` | `12` |

### Q81. Find the LCM of Two Numbers

**Task:** Take two positive integers `A` and `B`. Find their least common multiple (LCM) using a `while` loop.

**Input:**
```text
A = 6
B = 8
```

**Expected Output:**
```text
24
```

**Test Cases:**

| Input | Expected Output |
|---|---:|
| `A = 6, B = 120` | `120` |
| `A = 4, B = 10` | `20` |
| `A = 7, B = 9` | `63` |
| `A = 5, B = 5` | `5` |

### Q82. Check Whether a Number Is Perfect

**Task:** A positive integer is called a perfect number if the sum of its positive factors excluding itself equals the number. Print `Perfect` or `Not Perfect`.

**Input:**
```text
28
```

**Expected Output:**
```text
Perfect
```

**Test Cases:**

| Input | Expected Output |
|---|---|
| `6` | `Perfect` |
| `28` | `Perfect` |
| `12` | `Not Perfect` |
| `1` | `Not Perfect` |

### Q83. Check Whether a Number Is a Strong Number

**Task:** A number is a strong number if the sum of the factorials of its digits equals the original number. Print `Strong` or `Not Strong`. Use a single `while` loop to process the digits; calculate each digit's factorial without using another loop.

**Input:**
```text
145
```

**Expected Output:**
```text
Strong
```

**Test Cases:**

| Input | Expected Output |
|---|---|
| `145` | `Strong` |
| `2` | `Strong` |
| `123` | `Not Strong` |
| `40585` | `Strong` |

### Q84. Check Whether a Number Is an Armstrong Number

**Task:** A non-negative integer is an Armstrong number if the sum of each digit raised to the power of the total number of digits equals the original number. Print `Armstrong` or `Not Armstrong`. Use one `while` loop for digit processing; do not use strings or lists.

**Input:**
```text
153
```

**Expected Output:**
```text
Armstrong
```

**Test Cases:**

| Input | Expected Output |
|---|---|
| `153` | `Armstrong` |
| `370` | `Armstrong` |
| `123` | `Not Armstrong` |
| `9474` | `Armstrong` |

### Q85. Convert a Decimal Number to Binary

**Task:** Take a non-negative decimal integer and print its binary representation. Do not use Python's `bin()` function or convert the number to a string. You may use arithmetic and one `while` loop.

**Input:**
```text
13
```

**Expected Output:**
```text
1101
```

**Test Cases:**

| Input | Expected Output |
|---|---|
| `10` | `1010` |
| `8` | `1000` |
| `2` | `10` |
| `0` | `0` |

### Q86. Find the Sum of a Number's Divisors

**Task:** Take a positive integer `N` and calculate the sum of all its positive divisors, including `1` and `N`.

**Input:**
```text
12
```

**Expected Output:**
```text
28
```

**Test Cases:**

| Input | Expected Output |
|---|---:|
| `6` | `12` |
| `10` | `18` |
| `7` | `8` |
| `1` | `1` |

------------------------------------------------------------------------

### Part B: Nested Loops and Statement-Based Problems

**Instructions:** Only Q87–Q90 are pattern-printing questions. The remaining questions focus on number logic and problem-solving. Use `while` loops and nested loops where needed. Do not use lists, dictionaries, or user-defined functions.

### Q87. Print a Number Triangle

**Task:** Take a positive integer `N`. Print `N` rows. Row `i` should contain numbers from `1` to `i`.

**Input:**
```text
4
```

**Expected Output:**
```text
1
1 2
1 2 3
1 2 3 4
```

**Test Cases:**

| Input | Expected Output |
|---|---|
| `2` | `1`<br>`1 2` |
| `3` | `1`<br>`1 2`<br>`1 2 3` |

### Q88. Print a Hollow Rectangle

**Task:** Take rows `R` and columns `C` (both at least `2`). Print stars on the boundary and spaces inside.

**Input:**
```text
R = 4
C = 5
```

**Expected Output:**
```text
* * * * *
*       *
*       *
* * * * *
```

**Test Cases:**

| Input | Expected Output |
|---|---|
| `R = 3, C = 4` | `* * * *`<br>`*     *`<br>`* * * *` |
| `R = 2, C = 3` | `* * *`<br>`* * *` |

### Q89. Print a Right-Aligned Triangle

**Task:** Take a positive integer `N`. Print a right-aligned triangle of stars with `N` rows. Use spaces before the stars.

**Input:**
```text
3
```

**Expected Output:**
```text
    *
  * *
* * *
```

**Test Cases:**

| Input | Expected Output |
|---|---|
| `2` | `  *`<br>`* *` |
| `4` | `      *`<br>`    * *`<br>`  * * *`<br>`* * * *` |

### Q90. Print a Multiplication Grid

**Task:** Take a positive integer `N`. Print an `N × N` grid where each cell in row `i` and column `j` contains `i * j`. Row and column numbers start from `1`.

**Input:**
```text
3
```

**Expected Output:**
```text
1 2 3
2 4 6
3 6 9
```

**Test Cases:**

| Input | Expected Output |
|---|---|
| `2` | `1 2`<br>`2 4` |
| `1` | `1` |

---

### Statement-Based Number and Logic Problems

### Q91. Print the Fibonacci Series up to a Limit

**Task:** Take a non-negative integer `N` and print all Fibonacci numbers less than or equal to `N`. Start the series with `0, 1`. Do not print a number greater than `N`.

**Input:**
```text
N = 20
```

**Expected Output:**
```text
0 1 1 2 3 5 8 13
```

**Test Cases:**

| Input | Expected Output |
|---|---|
| `N = 1` | `0 1 1` |
| `N = 10` | `0 1 1 2 3 5 8` |
| `N = 0` | `0` |

### Q92. Print All Prime Numbers up to N

**Task:** Take an integer `N` greater than or equal to `2`. Print every prime number from `2` to `N` in ascending order. Use nested `while` loops to test whether each number is prime.

**Input:**
```text
N = 15
```

**Expected Output:**
```text
2 3 5 7 11 13
```

**Test Cases:**

| Input | Expected Output |
|---|---|
| `N = 10` | `2 3 5 7` |
| `N = 2` | `2` |
| `N = 20` | `2 3 5 7 11 13 17 19` |

### Q93. Print All Armstrong Numbers up to N

**Task:** Take a positive integer `N`. Print all Armstrong numbers from `0` to `N`. A number is an Armstrong number if the sum of its digits, each raised to the power of the total number of digits, equals the number itself. Use loops to count digits and calculate the digit-power sum.

**Input:**
```text
N = 500
```

**Expected Output:**
```text
0 1 2 3 4 5 6 7 8 9 153 370 371 407
```

**Test Cases:**

| Input | Expected Output |
|---|---|
| `N = 20` | `0 1 2 3 4 5 6 7 8 9` |
| `N = 160` | `0 1 2 3 4 5 6 7 8 9 153` |
| `N = 500` | `0 1 2 3 4 5 6 7 8 9 153 370 371 407` |

### Q94. Print All Perfect Numbers up to N

**Task:** Take a positive integer `N`. Print all perfect numbers from `1` to `N`. A perfect number equals the sum of its positive divisors excluding itself. Use nested loops to test each number.

**Input:**
```text
N = 1000
```

**Expected Output:**
```text
6 28 496
```

**Test Cases:**

| Input | Expected Output |
|---|---|
| `N = 30` | `6 28` |
| `N = 6` | `6` |
| `N = 10` | `6` |

### Q95. Find All Pairs Whose Sum Is N

**Task:** Take a positive integer `N`. Print all pairs of positive integers `(a, b)` such that `a < b` and `a + b = N`. Print each pair once, in increasing order of `a`.

**Input:**
```text
N = 7
```

**Expected Output:**
```text
1 + 6
2 + 5
3 + 4
```

**Test Cases:**

| Input | Expected Output |
|---|---|
| `N = 5` | `1 + 4`<br>`2 + 3` |
| `N = 6` | `1 + 5`<br>`2 + 4` |
| `N = 3` | `1 + 2` |

### Q96. Print All Two-Digit Numbers with a Given Digit Sum

**Task:** Take a digit sum `S` from `1` to `18`. Print all two-digit numbers whose digits add up to `S`, in ascending order.

**Input:**
```text
S = 5
```

**Expected Output:**
```text
14 23 32 41 50
```

**Test Cases:**

| Input | Expected Output |
|---|---|
| `S = 2` | `11` |
| `S = 9` | `18 27 36 45 54 63 72 81 90` |
| `S = 18` | `99` |

### Q97. Find All Common Divisors of Two Numbers

**Task:** Take two positive integers `A` and `B`. Print all positive numbers that divide both `A` and `B`, in ascending order.

**Input:**
```text
A = 12
B = 18
```

**Expected Output:**
```text
1 2 3 6
```

**Test Cases:**

| Input | Expected Output |
|---|---|
| `A = 8, B = 12` | `1 2 4` |
| `A = 7, B = 9` | `1` |
| `A = 10, B = 20` | `1 2 5 10` |

### Q98. Find Prime Factor Pairs

**Task:** Take an integer `N` greater than `1`. Print all pairs of prime numbers `(a, b)` such that `a <= b` and `a * b = N`. Print each pair once. If no such pair exists, print `No prime factor pair`.

**Input:**
```text
N = 15
```

**Expected Output:**
```text
3 * 5
```

**Test Cases:**

| Input | Expected Output |
|---|---|
| `N = 30` | `No prime factor pair` |
| `N = 49` | `7 * 7` |
| `N = 13` | `No prime factor pair` |

------------------------------------------------------------------------
