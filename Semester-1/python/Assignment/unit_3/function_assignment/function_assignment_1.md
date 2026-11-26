# Python Functions — Practice Assignment

**Subject:** Python Programming  
**Assignment:** Functions  
**Total Questions:** 20  
**Submission Deadline:** 27 November 2026

---

## Instructions

1. Solve all questions in the given order. The questions gradually increase in difficulty.
2. Use user-defined functions for the main task in every question.
3. Use only the topics covered in class.
4. Do not use rest parameters (`*args`).
5. Do not use lists or list methods.
6. Use meaningful function and variable names.
7. For questions that ask you to calculate a result, use `return` where specified.
8. Dry-run your code with the given test cases before submitting.
9. Write the output clearly wherever a question asks you to display information.

---

## Section A — Basic Function Practice

### Q1. Display a Welcome Message

**Task**

Create a function named `display_welcome()` that displays the following message:

```text
================================
   Welcome to Python Programming
       Let's learn Functions!
================================
```

Call the function three times.

**Test your program**

| Test | Expected behaviour |
|---|---|
| 1 | The welcome message is displayed. |
| 2 | The same message is displayed again when the function is called a second time. |
| 3 | The same message is displayed a third time. |

---

### Q2. Student Introduction Card

**Task**

Create a function named `display_student_card(name, age, course)`.

The function should display the student's details in the following format:

**Sample function call**

```python
display_student_card("Rahul", 18, "B.Tech")
```

**Expected output**

```text
+--------------------------------+
|         STUDENT CARD           |
+--------------------------------+
| Name  : Rahul                  |
| Age   : 18                     |
| Course: B.Tech                 |
+--------------------------------+
```

Call the function for at least three students.

**Test cases**

| Name | Age | Course |
|---|---:|---|
| Rahul | 18 | B.Tech |
| Priya | 19 | BCA |
| Aman | 20 | B.Sc |

---

### Q3. Square, Cube, and Double

**Task**

Create three separate functions:

- `calculate_square(number)`
- `calculate_cube(number)`
- `calculate_double(number)`

Each function should calculate and display its respective result.

**Sample function calls**

```python
calculate_square(4)
calculate_cube(4)
calculate_double(4)
```

**Expected output**

```text
Square: 16
Cube: 64
Double: 8
```

**Test cases**

| Input | Square | Cube | Double |
|---:|---:|---:|---:|
| 2 | 4 | 8 | 4 |
| 4 | 16 | 64 | 8 |
| 5 | 25 | 125 | 10 |

---

### Q4. Simple Interest Calculator

**Task**

Create a function named `calculate_simple_interest(principal, rate, time)`.

Calculate simple interest using:

\[
SI = \frac{P \times R \times T}{100}
\]

Also calculate the final amount:

\[
Amount = Principal + SI
\]

Display both values.

**Sample function call**

```python
calculate_simple_interest(5000, 5, 2)
```

**Expected output**

```text
Principal: 5000
Rate: 5%
Time: 2 years
Simple Interest: 500
Total Amount: 5500
```

**Test cases**

| Principal | Rate | Time |
|---:|---:|---:|
| 5000 | 5 | 2 |
| 10000 | 7 | 3 |
| 2500 | 4 | 1 |

---

### Q5. Even or Odd Checker

**Task**

Create a function named `check_even_odd(number)`.

The function should display whether the given number is even or odd.

**Sample function calls**

```python
check_even_odd(12)
check_even_odd(7)
```

**Expected output**

```text
12 is an Even number.
7 is an Odd number.
```

**Test cases**

| Input | Expected output |
|---:|---|
| 12 | Even |
| 7 | Odd |
| 0 | Even |
| -5 | Odd |

---

## Section B — Parameters, Arguments, and Return Values

### Q6. Find the Larger Number

**Task**

Create a function named `find_largest(number_1, number_2)` that returns the larger of the two numbers.

Outside the function:

1. Call the function.
2. Store the returned value in a variable.
3. Display the result.

Do not print the answer from inside the function.

**Sample**

```python
result = find_largest(25, 40)
print("Largest number:", result)
```

**Expected output**

```text
Largest number: 40
```

**Test cases**

| Number 1 | Number 2 | Expected result |
|---:|---:|---:|
| 25 | 40 | 40 |
| 90 | 15 | 90 |
| 12 | 12 | 12 |
| -5 | -2 | -2 |

---

### Q7. Temperature Converter

**Task**

Create two functions:

- `celsius_to_fahrenheit(celsius)` — returns Fahrenheit.
- `fahrenheit_to_celsius(fahrenheit)` — returns Celsius.

Use these formulas:

\[
F = \frac{9}{5} \times C + 32
\]

\[
C = \frac{5}{9} \times (F - 32)
\]

Display the returned values outside the functions.

**Sample**

```python
fahrenheit = celsius_to_fahrenheit(0)
print(fahrenheit)

celsius = fahrenheit_to_celsius(98.6)
print(celsius)
```

**Expected output**

```text
32.0
37.0
```

**Test cases**

| Celsius | Fahrenheit |
|---:|---:|
| 0 | 32 |
| 25 | 77 |
| 100 | 212 |

| Fahrenheit | Celsius |
|---:|---:|
| 32 | 0 |
| 68 | 20 |
| 98.6 | 37 |

---

### Q8. Understand the Difference Between print() and return

**Given code**

Study the following functions:

```python
def calculate_sum_1(a, b):
    print(a + b)


def calculate_sum_2(a, b):
    return a + b
```

**Task**

1. Call both functions with the values `10` and `20`.
2. Store the result of each function call in a separate variable.
3. Display both variables.
4. Predict the output before running the code.

**Expected output structure**

```text
30
30
Result from first function: None
Result from second function: 30
```

**Answer these questions in comments:**

- Which function returns a value?
- Why does the first variable contain `None`?
- Can the value displayed by `print()` be directly stored as the function's return value?

**Additional test cases**

Repeat the experiment with:

| A | B |
|---:|---:|
| 5 | 7 |
| 100 | 250 |

---

### Q9. Total Marks and Percentage

**Task**

Create a function named:

```python
calculate_result(mark_1, mark_2, mark_3, mark_4, mark_5)
```

The function should:

1. Calculate the total marks.
2. Calculate the percentage, assuming every subject is out of 100.
3. Return both the total marks and percentage.

Outside the function, receive both returned values in separate variables and display them.

**Sample**

```python
total, percentage = calculate_result(75, 80, 65, 90, 70)
```

**Expected output**

```text
Total Marks: 380
Percentage: 76.0%
```

**Test cases**

| Subject 1 | Subject 2 | Subject 3 | Subject 4 | Subject 5 |
|---:|---:|---:|---:|---:|
| 75 | 80 | 65 | 90 | 70 |
| 50 | 60 | 55 | 65 | 70 |
| 100 | 95 | 90 | 85 | 80 |

---

### Q10. Rectangle Area and Perimeter

**Task**

Create a function named `rectangle_details(length, breadth)`.

Calculate:

- Area = Length × Breadth
- Perimeter = 2 × (Length + Breadth)

Return both values from the function. Store them in two separate variables outside the function and display them.

**Sample**

```python
area, perimeter = rectangle_details(10, 5)
```

**Expected output**

```text
Area: 50
Perimeter: 30
```

**Test cases**

| Length | Breadth | Area | Perimeter |
|---:|---:|---:|---:|
| 10 | 5 | 50 | 30 |
| 8 | 4 | 32 | 24 |
| 7 | 7 | 49 | 28 |

---

## Section C — Default and Keyword Arguments

### Q11. Personalized Greeting

**Task**

Create a function:

```python
greet_user(name, message="Welcome to Python!")
```

The function should display the user's name and greeting message.

Call the function in all three ways:

**A. Pass both arguments**

```python
greet_user("Rahul", "Good Morning!")
```

**B. Use the default message**

```python
greet_user("Priya")
```

**C. Pass the message using a keyword argument**

```python
greet_user("Aman", message="Keep Learning!")
```

**Expected output**

```text
Hello Rahul!
Good Morning!

Hello Priya!
Welcome to Python!

Hello Aman!
Keep Learning!
```

**Test cases:** Use the three function calls shown above and add one more name of your choice.

---

### Q12. Electricity Bill Calculator

**Task**

Create a function named:

```python
calculate_electricity_bill(units, rate=7)
```

Calculate the bill using:

```text
Bill = Units × Rate
```

The default rate is ₹7 per unit. Return the bill and display it outside the function.

Call the function:

1. By passing only units.
2. By passing units and a different rate.
3. By using keyword arguments.

**Sample calls**

```python
bill_1 = calculate_electricity_bill(100)
bill_2 = calculate_electricity_bill(100, 8)
bill_3 = calculate_electricity_bill(rate=6, units=100)
```

**Expected output**

```text
Bill 1: 700
Bill 2: 800
Bill 3: 600
```

**Test cases**

| Units | Rate | Expected bill |
|---:|---:|---:|
| 100 | Default (7) | 700 |
| 150 | 8 | 1200 |
| 200 | 6 | 1200 |

---

### Q13. Employee Salary Calculator

**Task**

Create a function:

```python
calculate_salary(basic_salary, bonus=2000, deduction=500)
```

Calculate the final salary using:

```text
Final Salary = Basic Salary + Bonus - Deduction
```

Return the final salary.

Call the function in these four ways:

1. Pass only the basic salary.
2. Pass basic salary and bonus.
3. Pass all three arguments positionally.
4. Pass the arguments using keyword names.

**Sample calls**

```python
calculate_salary(25000)
calculate_salary(25000, 3000)
calculate_salary(25000, 3000, 1000)
calculate_salary(basic_salary=25000, deduction=800, bonus=4000)
```

**Expected results**

| Function call | Expected salary |
|---|---:|
| `calculate_salary(25000)` | 26500 |
| `calculate_salary(25000, 3000)` | 27500 |
| `calculate_salary(25000, 3000, 1000)` | 27000 |
| `calculate_salary(basic_salary=25000, deduction=800, bonus=4000)` | 28200 |

**Think and answer:** Why must parameters with default values be placed after parameters without default values?

---

## Section D — Applying Functions with Previously Learned Topics

### Q14. Number Digit Counter

**Task**

Create a function named `count_digits(number)` that returns the total number of digits in the given integer.

Do not convert the number into a string. Use arithmetic operators and a loop.

**Sample**

```python
count = count_digits(4826)
print("Total digits:", count)
```

**Expected output**

```text
Total digits: 4
```

**Test cases**

| Input | Expected digit count |
|---:|---:|
| 7 | 1 |
| 4826 | 4 |
| 90000 | 5 |
| 0 | 1 |

---

### Q15. Sum of Digits

**Task**

Create a function named `sum_of_digits(number)` that returns the sum of all digits of the given number.

Use a loop and the `%` and `//` operators.

**Sample**

```python
result = sum_of_digits(482)
print("Sum of digits:", result)
```

**Expected output**

```text
Sum of digits: 14
```

**Test cases**

| Input | Expected sum |
|---:|---:|
| 123 | 6 |
| 482 | 14 |
| 9005 | 14 |
| 7 | 7 |

---

### Q16. Reverse a Number

**Task**

Create a function named `reverse_number(number)` that returns the number formed by reversing its digits.

Use a loop and arithmetic operators. Do not convert the number into a string.

**Sample**

```python
result = reverse_number(4826)
print("Reversed number:", result)
```

**Expected output**

```text
Reversed number: 6284
```

**Test cases**

| Input | Expected result |
|---:|---:|
| 123 | 321 |
| 4826 | 6284 |
| 900 | 9 |
| 7 | 7 |

---

### Q17. Palindrome Number Checker

**Task**

Create a function named `is_palindrome(number)` that returns `True` if the given number reads the same forward and backward; otherwise, it returns `False`.

Use arithmetic operators and a loop. Do not convert the number into a string.

Outside the function, display a suitable message based on the returned value.

**Sample**

```python
result = is_palindrome(121)
print(result)
```

**Expected output**

```text
True
```

**Test cases**

| Input | Expected result |
|---:|---|
| 121 | True |
| 1331 | True |
| 123 | False |
| 7 | True |

---

### Q18. Prime Number Checker

**Task**

Create a function named `is_prime(number)` that returns `True` if the number is prime; otherwise, it returns `False`.

A prime number is greater than 1 and has exactly two factors: 1 and itself.

Display a suitable message outside the function.

**Sample**

```python
result = is_prime(17)
print(result)
```

**Expected output**

```text
True
```

**Test cases**

| Input | Expected result |
|---:|---|
| 2 | True |
| 17 | True |
| 21 | False |
| 1 | False |
| 0 | False |

---

### Q19. Display Prime Numbers in a Range

**Task**

Create a function named:

```python
display_primes(start, end)
```

The function should:

1. Check every number from `start` to `end`, including both limits.
2. Identify prime numbers.
3. Display all prime numbers found.
4. Count and display the total number of prime numbers.

You may write the prime-checking logic directly in this function. Do not use lists.

**Sample function call**

```python
display_primes(10, 30)
```

**Expected output**

```text
Prime numbers: 11 13 17 19 23 29
Total prime numbers: 6
```

**Test cases**

| Start | End | Expected prime numbers | Count |
|---:|---:|---|---:|
| 1 | 10 | 2, 3, 5, 7 | 4 |
| 10 | 30 | 11, 13, 17, 19, 23, 29 | 6 |
| 20 | 25 | 23 | 1 |
| 14 | 16 | No prime numbers | 0 |

---

### Q20. Student Result Report

**Task**

Create a function named:

```python
display_student_report(name, mark_1, mark_2, mark_3)
```

The function should:

1. Calculate the total marks.
2. Calculate the percentage, assuming each subject is out of 100.
3. Decide the result:
   - Percentage greater than or equal to 40: Pass
   - Percentage below 40: Fail
4. Display the student's complete report.

**Sample function call**

```python
display_student_report("Rahul", 75, 80, 65)
```

**Expected output**

```text
================================
         STUDENT REPORT
================================
Name       : Rahul
Subject 1  : 75
Subject 2  : 80
Subject 3  : 65
--------------------------------
Total      : 220 / 300
Percentage : 73.33%
Result     : PASS
================================
```

Call the function for at least three students.

**Test cases**

| Name | Mark 1 | Mark 2 | Mark 3 | Expected result |
|---|---:|---:|---:|---|
| Rahul | 75 | 80 | 65 | Pass |
| Priya | 35 | 45 | 40 | Pass |
| Aman | 20 | 30 | 25 | Fail |
| Neha | 100 | 100 | 100 | Pass |

---

**Submission:** Submit your Python code for all 20 questions by **27 November 2026**.
