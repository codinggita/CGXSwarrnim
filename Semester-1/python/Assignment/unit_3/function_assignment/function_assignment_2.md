# Python Functions — Practice Assignment
## Parameters, Arguments, Return Values, Default and Keyword Arguments

**Subject:** Python Programming  
**Total Questions:** 40  
**Submission Deadline:** 29 November 2026

---

## Instructions

1. Attempt the output-guessing questions first. Predict the complete output before running each program.
2. Do not execute the code until you have written your prediction.
3. For statement-based questions, create the function with the exact or a suitable function name.
4. Use meaningful parameter and variable names.
5. Use `return` when the question asks you to return a value. Do not replace `return` with `print()`.
6. Do not use rest parameters (`*args`) or lists.
7. Test your functions with all the given test cases.
8. Pay attention to the order of positional arguments, keyword arguments, and default parameters.

---

# Part A — Output Guessing Questions

**Total: 20 Questions**

For every question:
- Read the code carefully.
- Write the exact output, including line breaks and spaces where relevant.
- If a function returns a value but does not print it, remember that the value will not appear automatically.

## Section 1 — Parameters, Arguments, and Basic Return Values

### Q1. Function Call with Two Arguments

Predict the output:

```python
def show_details(name, age):
    print("Name:", name)
    print("Age:", age)


show_details("Riya", 19)
show_details("Aman", 20)
```

*Hint: Check how each positional argument is assigned to its matching parameter.*

### Q2. Returning a Value

Predict the output:

```python
def calculate_sum(a, b):
    return a + b


answer = calculate_sum(12, 8)
print("Answer:", answer)
print(calculate_sum(5, 7))
```

*Hint: Trace the returned values and notice where each value is printed.*

### Q3. Return Does Not Mean Print

Predict the output:

```python
def multiply(a, b):
    result = a * b
    return result


multiply(4, 5)
print("Function completed")
```

*Hint: A returned value is not displayed unless it is printed or used.*

### Q4. Using a Returned Value in Another Calculation

Predict the output:

```python
def square(number):
    return number * number


result = square(5)
final_result = result + 10

print(result)
print(final_result)
```

*Hint: First calculate the returned square, then use that value in the next expression.*

### Q5. Returning Multiple Values

Predict the output:

```python
def calculate(number):
    return number + 5, number * 2


first, second = calculate(10)

print(first)
print(second)
print(first + second)
```

*Hint: Match the first returned value with the first variable and the second with the second.*

---

## Section 2 — Returning Values and Reusing Them

### Q6. Calling a Function More Than Once

Predict the output:

```python
def get_price(price, quantity):
    return price * quantity


bill_1 = get_price(50, 3)
bill_2 = get_price(20, 4)

print("Bill 1:", bill_1)
print("Bill 2:", bill_2)
print("Total:", bill_1 + bill_2)
```

*Hint: Calculate each function call separately, then add the stored results.*

### Q7. Function Call Inside Another Function Call

Predict the output:

```python
def add(a, b):
    return a + b


def double(number):
    return number * 2


answer = double(add(5, 3))
print(answer)
```

*Hint: Evaluate the inner function call before evaluating the outer function call.*

### Q8. Returning Two Calculated Values

Predict the output:

```python
def rectangle(length, breadth):
    area = length * breadth
    perimeter = 2 * (length + breadth)
    return area, perimeter


a, p = rectangle(6, 4)

print("Area:", a)
print("Perimeter:", p)
```

*Hint: Calculate area and perimeter separately, then match them with the returned variables.*

### Q9. Using the Same Returned Value Twice

Predict the output:

```python
def get_discount(price):
    return price * 10 / 100


discount = get_discount(500)
final_price = 500 - discount

print("Discount:", discount)
print("Final price:", final_price)
print("Double discount:", discount * 2)
```

*Hint: The returned discount is stored once and reused in both later calculations.*

### Q10. Difference Between Print and Return

Predict the output:

```python
def first_function(number):
    print(number * 2)


def second_function(number):
    return number * 2


result_1 = first_function(6)
result_2 = second_function(6)

print("First result:", result_1)
print("Second result:", result_2)
```

*Hint: Compare what each function displays with what each function returns.*

---

## Section 3 — Default Arguments

### Q11. Using a Default Argument

Predict the output:

```python
def greet(name, message="Welcome"):
    print(message, name)


greet("Rohan")
greet("Meera", "Good Morning")
```

*Hint: The default message is used only when the caller does not provide one.*

### Q12. Default Value Is Used Only When an Argument Is Not Supplied

Predict the output:

```python
def calculate_bill(units, rate=5):
    return units * rate


print(calculate_bill(10))
print(calculate_bill(10, 8))
print(calculate_bill(5))
```

*Hint: Check which calls use the default rate and which supply a new rate.*

### Q13. Multiple Default Parameters

Predict the output:

```python
def calculate_salary(basic, bonus=1000, deduction=500):
    return basic + bonus - deduction


print(calculate_salary(20000))
print(calculate_salary(20000, 3000))
print(calculate_salary(20000, 3000, 1000))
```

*Hint: For each call, identify which values are supplied and which default values remain.*

### Q14. Default Parameter and Returned Value

Predict the output:

```python
def calculate_total(price, quantity=2):
    total = price * quantity
    return total


amount = calculate_total(150)
print(amount)

amount = calculate_total(150, 4)
print(amount)
```

*Hint: The first call uses the default quantity; the second call overrides it.*

### Q15. Default Parameters with a String

Predict the output:

```python
def make_message(name, course="Python", institute="ABC College"):
    return name + " is learning " + course + " at " + institute


print(make_message("Asha"))
print(make_message("Kabir", "Java"))
print(make_message("Neha", "C++", "XYZ Institute"))
```

*Hint: Track the default course and institute values in each function call.*

---

## Section 4 — Keyword Arguments

### Q16. Passing Arguments by Keyword

Predict the output:

```python
def student(name, age, course):
    print(name)
    print(age)
    print(course)


student(age=18, course="B.Tech", name="Arjun")
```

*Hint: Keyword arguments are matched by parameter name, not by their order in the call.*

### Q17. Keyword Arguments in a Different Order

Predict the output:

```python
def calculate(a, b, c):
    return a + b * c


print(calculate(c=4, a=2, b=3))
print(calculate(b=5, c=2, a=10))
```

*Hint: Assign values by keyword first, then apply the function's arithmetic expression.*

### Q18. Keyword Arguments with Return Values

Predict the output:

```python
def calculate_amount(price, quantity, discount):
    total = price * quantity
    return total - discount


amount = calculate_amount(discount=50, quantity=3, price=200)
print("Payable amount:", amount)
```

*Hint: Match each keyword with its parameter before calculating the total and discount.*

---

## Section 5 — Combining Positional, Keyword, and Default Arguments

### Q19. Positional Arguments with a Default Parameter

Predict the output:

```python
def order(item, quantity=1, price=100):
    return quantity * price


print(order("Pen"))
print(order("Notebook", 3))
print(order("Bag", 2, 500))
```

*Hint: Check how many positional arguments are supplied and which parameters keep defaults.*

### Q20. Positional and Keyword Arguments Together

Predict the output:

```python
def introduce(name, age, city):
    print(name, "is", age, "years old and lives in", city)


introduce("Rahul", city="Ahmedabad", age=19)
```

*Hint: Positional arguments fill parameters first; keyword arguments fill the named remaining parameters.*

---

# Part B — Find and Correct the Mistakes

**Total: 10 Questions**

Each program below contains one or more intentional mistakes. Some programs may show an incorrect result, while others may produce a Python error.

For every question:
1. Read the given input.
2. Identify the mistake in the code.
3. Correct the code.
4. Run the corrected program and compare its output with the expected output.

**Do not write only the expected output. Your task is to debug and correct the program.**

### Q21. Input Values Are Strings

The program should accept two numbers and display their sum.

**Given code (contains a mistake)**

```python
def calculate_sum(a, b):
    return a + b

num_1 = input("Enter first number: ")
num_2 = input("Enter second number: ")

result = calculate_sum(num_1, num_2)
print("Sum:", result)
```

**Test case**

```text
Input:
10
20
```

**Expected output**

```text
Sum: 30
```

**Your task:** Find why the program displays an unexpected result and correct it.

### Q22. Missing Function Argument

**Given code (contains a mistake)**

```python
def calculate_total(price, quantity):
    return price * quantity

total = calculate_total(50)
print("Total:", total)
```

The function should calculate the total for a price of 50 and quantity of 4.

**Expected output**

```text
Total: 200
```

**Your task:** Correct the function call so that the function receives all required values.

### Q23. Returning a Value vs Displaying a Value

**Given code (contains a mistake)**

```python
def calculate_square(number):
    print(number * number)

result = calculate_square(6)
print("Square:", result)
```

**Test input:** `6`

**Expected output**

```text
Square: 36
```

**Your task:** Correct the function so that the calculated value is returned to the caller.

### Q24. Wrong Default Argument Placement

**Given code (contains a mistake)**

```python
def calculate_price(quantity=1, price):
    return price * quantity

print(calculate_price(100))
print(calculate_price(100, 3))
```

**Test cases**

| Price | Quantity | Expected total |
|---:|---:|---:|
| 100 | Default (1) | 100 |
| 100 | 3 | 300 |

**Your task:** Correct the parameter order and function calls so that both test cases work.

### Q25. Incorrect Keyword Argument Name

**Given code (contains a mistake)**

```python
def calculate_total(price, quantity):
    return price * quantity

result = calculate_total(price=80, qty=5)
print("Total:", result)
```

**Test case:** Price = 80, Quantity = 5

**Expected output**

```text
Total: 400
```

**Your task:** Find the mismatch between the parameter name and keyword argument name. Correct the function call.

### Q26. Positional Argument After a Keyword Argument

**Given code (contains a mistake)**

```python
def display_student(name, age, course):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)

display_student(name="Riya", 19, course="B.Tech")
```

**Expected output**

```text
Name: Riya
Age: 19
Course: B.Tech
```

**Your task:** Correct the function call using a valid combination of positional and keyword arguments.

### Q27. Incorrect Default Value Calculation

**Given code (contains a mistake)**

```python
def calculate_bill(amount, tax=5):
    tax_amount = amount * tax / 100
    return amount + tax

print("Bill:", calculate_bill(1000))
```

**Test case:** Amount = 1000, default tax = 5%

**Expected output**

```text
Bill: 1050.0
```

**Your task:** Find the calculation mistake. The function should add the calculated tax amount, not the tax percentage.

### Q28. Incorrect Order of Positional Arguments

**Given code (contains a mistake)**

```python
def calculate_final_price(price, discount):
    discount_amount = price * discount / 100
    return price - discount_amount

price = 1000
discount = 10

result = calculate_final_price(discount, price)
print("Final price:", result)
```

**Test case:** Price = 1000, Discount = 10%

**Expected output**

```text
Final price: 900.0
```

**Your task:** Correct the function call so that the arguments follow the intended positional order. Explain why the program runs without an error even though the arguments are passed in the wrong order.

### Q29. Incorrectly Combining Default and Keyword Arguments

**Given code (contains a mistake)**

```python
def calculate_delivery(amount, delivery_charge=40):
    return amount + delivery_charge

total = calculate_delivery(amount=500, 60)
print("Final amount:", total)
```

**Test case:** Item amount = 500, Delivery charge = 60

**Expected output**

```text
Final amount: 560
```

**Your task:** Correct the function call using a valid combination of positional and keyword arguments.

### Q30. Multiple Returned Values Assigned Incorrectly

**Given code (contains a mistake)**

```python
def calculate_marks(mark_1, mark_2, mark_3):
    total = mark_1 + mark_2 + mark_3
    average = total / 3
    return total, average

total, average, percentage = calculate_marks(70, 80, 90)

print("Total:", total)
print("Average:", average)
```

**Test input:** Marks = 70, 80, 90

**Expected output**

```text
Total: 240
Average: 80.0
```

**Your task:** The function returns two values, but the caller is trying to receive a different number of values. Correct the assignment statement.

---

# Part C — Statement-Based Programming Questions

**Total: 10 Questions**

Write a complete Python program for each question. Define the required function, call it using the given test cases, and display the result in the requested format.

## Section 1 — Parameters and Return Values

### Q31. Shopping Bill Calculator

**Problem statement**

A shop needs to calculate the total price of purchased items. Create a function named `calculate_bill(price, quantity)` that accepts the price of one item and the purchased quantity.

The function must return the total bill amount.

Display the returned amount outside the function.

**Formula**

```text
Total Bill = Price × Quantity
```

**Test cases**

| Price | Quantity | Expected bill |
|---:|---:|---:|
| 50 | 3 | 150 |
| 120 | 2 | 240 |
| 75 | 4 | 300 |

### Q32. Convert Minutes into Hours and Minutes

**Problem statement**

Create a function named `convert_time(total_minutes)` that converts the given number of minutes into hours and remaining minutes.

The function must return both values.

**Example**

```text
Input: 135 minutes
Expected output:
Hours: 2
Minutes: 15
```

**Test cases**

| Total minutes | Expected hours | Expected remaining minutes |
|---:|---:|---:|
| 135 | 2 | 15 |
| 60 | 1 | 0 |
| 245 | 4 | 5 |
| 48 | 0 | 48 |

### Q33. Calculate Total and Average Marks

**Problem statement**

Create a function named `calculate_marks(mark_1, mark_2, mark_3)`.

The function should calculate:
1. Total marks.
2. Average marks.

Return both values from the function. Store the returned values in two separate variables and display them outside the function.

Assume each subject is out of 100.

**Test cases**

| Mark 1 | Mark 2 | Mark 3 | Expected total | Expected average |
|---:|---:|---:|---:|---:|
| 70 | 80 | 90 | 240 | 80.0 |
| 45 | 55 | 65 | 165 | 55.0 |
| 100 | 90 | 80 | 270 | 90.0 |

### Q34. Find the Final Price After Discount

**Problem statement**

Create a function named `calculate_final_price(price, discount)` that calculates the discount amount and final price.

Return both values from the function.

**Formula**

```text
Discount Amount = Price × Discount / 100
Final Price = Price - Discount Amount
```

**Test cases**

| Price | Discount (%) | Expected discount | Expected final price |
|---:|---:|---:|---:|
| 1000 | 10 | 100 | 900 |
| 2500 | 20 | 500 | 2000 |
| 800 | 5 | 40 | 760 |

---

## Section 2 — Default Arguments

### Q35. Movie Ticket Booking

**Problem statement**

A cinema charges ₹200 for one ticket by default.

Create a function named `calculate_ticket_price(number_of_tickets, price_per_ticket=200)` that returns the total ticket price.

Call the function once using the default ticket price and again using a different ticket price.

**Test cases**

| Number of tickets | Price per ticket | Expected total |
|---:|---:|---:|
| 2 | Default (200) | 400 |
| 4 | Default (200) | 800 |
| 3 | 250 | 750 |
| 5 | 150 | 750 |

### Q36. Employee Salary Calculator

**Problem statement**

Create a function named `calculate_salary(basic_salary, bonus=1500, deduction=500)`.

Calculate and return the final salary.

**Formula**

```text
Final Salary = Basic Salary + Bonus - Deduction
```

Call the function using:
1. Only the basic salary.
2. Basic salary and a custom bonus.
3. All three values.

**Test cases**

| Basic salary | Bonus | Deduction | Expected salary |
|---:|---:|---:|---:|
| 20000 | Default (1500) | Default (500) | 21000 |
| 25000 | 3000 | Default (500) | 27500 |
| 30000 | 4000 | 1000 | 33000 |

---

## Section 3 — Keyword Arguments and Combining Arguments

### Q37. Student Profile

**Problem statement**

Create a function named `display_profile(name, age, city, course)` that displays the student's details in a clean format.

Call the function using keyword arguments. Change the order of the keyword arguments in at least one function call.

**Sample output**

```text
--------- STUDENT PROFILE ---------
Name   : Riya
Age    : 18
City   : Ahmedabad
Course : B.Tech
-----------------------------------
```

**Test cases**

| Name | Age | City | Course |
|---|---:|---|---|
| Riya | 18 | Ahmedabad | B.Tech |
| Aman | 20 | Surat | BCA |
| Neha | 19 | Vadodara | B.Sc |

### Q38. Mobile Recharge Calculator

**Problem statement**

Create a function named `recharge_details(customer_name, amount, validity=28, data_per_day=1.5)`.

The function should display the customer's name, recharge amount, validity, and daily data allowance.

Call the function using:
1. Only the required arguments.
2. Required arguments and a custom validity.
3. A combination of positional and keyword arguments.
4. Keyword arguments in a different order.

**Test cases**

| Customer | Amount | Validity | Data per day |
|---|---:|---:|---:|
| Rohan | 299 | Default (28) | Default (1.5) |
| Priya | 399 | 56 | Default (1.5) |
| Aman | 199 | 28 | 2.0 |
| Neha | 599 | 84 | 3.0 |

### Q39. Online Order Summary

**Problem statement**

Create a function named:

```python
create_order(item_name, quantity, price_per_item=100, delivery_charge=40)
```

The function should:
1. Calculate the item cost.
2. Add the delivery charge.
3. Return both the item cost and final payable amount.

Use a combination of positional arguments, keyword arguments, and default values in your function calls.

**Formula**

```text
Item Cost = Quantity × Price per Item
Final Amount = Item Cost + Delivery Charge
```

**Test cases**

| Item | Quantity | Price per item | Delivery charge | Expected item cost | Expected final amount |
|---|---:|---:|---:|---:|---:|
| Pen | 5 | Default (100) | Default (40) | 500 | 540 |
| Book | 2 | 150 | Default (40) | 300 | 340 |
| Bag | 1 | 800 | 60 | 800 | 860 |
| Bottle | 3 | 120 | 30 | 360 | 390 |

### Q40. Calculate Course Fee

**Problem statement**

An institute calculates course fees based on course name, base fee, discount, and registration charge.

Create a function:

```python
calculate_course_fee(course_name, base_fee, discount=10, registration_charge=500)
```

The function should:
1. Calculate the discount amount.
2. Add the registration charge to the fee after discount.
3. Return both the discount amount and final payable fee.

Use positional arguments for the course name and base fee. For other calls, also use keyword arguments to change the default values.

**Formula**

```text
Discount Amount = Base Fee × Discount / 100
Fee After Discount = Base Fee - Discount Amount
Final Payable Fee = Fee After Discount + Registration Charge
```

**Test cases**

| Course | Base fee | Discount | Registration charge | Expected discount | Expected payable fee |
|---|---:|---:|---:|---:|---:|
| Python | 10000 | Default (10) | Default (500) | 1000 | 9500 |
| Java | 15000 | 20 | Default (500) | 3000 | 12500 |
| Web Development | 20000 | 15 | 1000 | 3000 | 18000 |
| Data Science | 25000 | 25 | 1500 | 6250 | 20250 |

---
