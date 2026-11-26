# Assignment 4 — Conditional Statements, Nested Conditions & Match-Case

**Deadline:** 30 September 2026

## Objective

This assignment builds on the concepts covered in the previous assignments and introduces decision-making in Python.

The assignment focuses mainly on:

- `if` statement
- `if-else` statement
- `if-elif-else` statement
- Nested `if`
- Nested `if-elif-else`
- Logical expressions with conditions
- Comparison operators in decision making
- Combining multiple conditions using `and` and `or`
- `match-case`
- `_` default case in `match`
- Combining conditional statements with previously covered concepts
- Debugging conditional programs
- Real-life problem solving

> **Important:** Use only concepts that have already been covered along with the conditional statements and `match-case` introduced in this assignment. Do not use loops, functions, lists, dictionaries, or other advanced concepts unless specifically mentioned in a question.

---

# Topic-1 — Basic `if` Statements

## Q1. Positive Number

Take an integer as input.

If the number is positive, print:

```text
Positive Number
```

Otherwise, print nothing.

### Test Cases

`8 → Positive Number`  
`-4 → No output`  
`0 → No output`

---

## Q2. Voting Eligibility Check

Take a person's age as input.

If the age is `18` or more, print:

```text
Eligible to Vote
```

### Test Cases

`18 → Eligible to Vote`  
`25 → Eligible to Vote`  
`16 → No output`

---

## Q3. Temperature Warning

Take the temperature in Celsius.

If the temperature is greater than `40`, print:

```text
High Temperature
```

### Test Cases

`42 → High Temperature`  
`40 → No output`  
`25 → No output`

---

## Q4. Divisible by 5

Take an integer.

If it is divisible by `5`, print:

```text
Divisible by 5
```

### Test Cases

`25 → Divisible by 5`  
`42 → No output`  
`100 → Divisible by 5`

---

## Q5. Free Delivery

An online store gives free delivery when the order amount is `1000` or more.

Take the order amount and print:

```text
Free Delivery
```

when the condition is satisfied.

### Test Cases

`1200 → Free Delivery`  
`1000 → Free Delivery`  
`799 → No output`

---

## Q6. Character Check

Take one character as input.

If the character is `"A"`, print:

```text
You entered A
```

### Test Cases

`A → You entered A`  
`B → No output`

---

## Q7. Password Length Check

Take a password as input.

If its length is at least `8`, print:

```text
Strong Length
```

### Test Cases

`python123 → Strong Length`  
`hello → No output`  
`college2026 → Strong Length`

---

## Q8. Number of Digits

Take an integer.

If the number is between `100` and `999`, print:

```text
Three Digit Number
```

### Test Cases

`250 → Three Digit Number`  
`99 → No output`  
`1000 → No output`

---

# Topic-2 — `if-else` Statements

## Q9. Even or Odd

Take an integer and print whether it is even or odd.

### Test Cases

`24 → Even`  
`17 → Odd`  
`0 → Even`

---

## Q10. Pass or Fail

Take marks as input.

If marks are `40` or more, print:

```text
Pass
```

Otherwise print:

```text
Fail
```

### Test Cases

`75 → Pass`  
`40 → Pass`  
`39 → Fail`

---

## Q11. Adult or Minor

Take age as input.

Print:

```text
Adult
```

if age is `18` or more; otherwise print:

```text
Minor
```

### Test Cases

`21 → Adult`  
`18 → Adult`  
`12 → Minor`

---

## Q12. Number Sign

Take an integer and print:

```text
Positive
```

for positive numbers and:

```text
Non-Positive
```

otherwise.

### Test Cases

`15 → Positive`  
`0 → Non-Positive`  
`-7 → Non-Positive`

---

## Q13. Divisible by 3

Take an integer.

Print:

```text
Divisible by 3
```

or:

```text
Not Divisible by 3
```

### Test Cases

`21 → Divisible by 3`  
`22 → Not Divisible by 3`  
`0 → Divisible by 3`

---

## Q14. Login Password

Store the correct password as:

```python
correct_password = "python123"
```

Take a password from the user.

Print:

```text
Login Successful
```

if it matches; otherwise print:

```text
Invalid Password
```

### Test Cases

`python123 → Login Successful`  
`python321 → Invalid Password`

---

## Q15. Username Check

The valid username is:

```text
admin
```

Take a username as input and print:

```text
Welcome Admin
```

or:

```text
Invalid Username
```

### Test Cases

`admin → Welcome Admin`  
`Admin → Invalid Username`  
`student → Invalid Username`

---

## Q16. Greater Between Two Numbers

Take two integers and print the greater number.

If both numbers are equal, print:

```text
Both are Equal
```

### Test Cases

`15 20 → 20`  
`50 12 → 50`  
`25 25 → Both are Equal`

---

## Q17. Hot or Comfortable

Take temperature in Celsius.

If temperature is greater than `30`, print:

```text
Hot
```

Otherwise print:

```text
Comfortable
```

### Test Cases

`35 → Hot`  
`30 → Comfortable`  
`18 → Comfortable`

---

## Q18. Shopping Discount Eligibility

A customer receives a discount if the shopping amount is at least `5000`.

Print:

```text
Discount Available
```

or:

```text
No Discount
```

### Test Cases

`7000 → Discount Available`  
`5000 → Discount Available`  
`4999 → No Discount`

---

# Topic-3 — `if-elif-else`

## Q19. Grade Calculator

Take marks and print:

```text
A
B
C
D
F
```

using these ranges:

- `90–100` → A
- `80–89` → B
- `70–79` → C
- `60–69` → D
- Below `60` → F

### Test Cases

`95 → A`  
`84 → B`  
`72 → C`  
`65 → D`  
`40 → F`

---

## Q20. Temperature Category

Take temperature in Celsius.

Print:

```text
Very Hot
Hot
Warm
Cold
```

Rules:

- `40+` → Very Hot
- `30–39` → Hot
- `20–29` → Warm
- Below `20` → Cold

### Test Cases

`45 → Very Hot`  
`35 → Hot`  
`25 → Warm`  
`12 → Cold`

---

## Q21. Traffic Signal

Take a traffic signal color.

Print the appropriate instruction:

- `red` → Stop
- `yellow` → Wait
- `green` → Go
- anything else → Invalid Signal

### Test Cases

`red → Stop`  
`yellow → Wait`  
`green → Go`  
`blue → Invalid Signal`

---

## Q22. Electricity Usage Category

Take electricity units.

Print:

- `0–100` → Low Usage
- `101–300` → Medium Usage
- `301–500` → High Usage
- Above `500` → Very High Usage

### Test Cases

`80 → Low Usage`  
`250 → Medium Usage`  
`450 → High Usage`  
`650 → Very High Usage`

---

## Q23. Movie Ticket Category

Take age as input.

Print:

- Below `5` → Free Ticket
- `5–12` → Child Ticket
- `13–59` → Regular Ticket
- `60+` → Senior Ticket

### Test Cases

`3 → Free Ticket`  
`10 → Child Ticket`  
`25 → Regular Ticket`  
`65 → Senior Ticket`

---

## Q24. BMI Category

Take BMI as input.

Print:

- Below `18.5` → Underweight
- `18.5–24.9` → Normal
- `25–29.9` → Overweight
- `30+` → Obese

### Test Cases

`17.8 → Underweight`  
`22.5 → Normal`  
`27.2 → Overweight`  
`31.4 → Obese`

---

## Q25. Month Days

Take a month number.

Print the number of days for:

- `1, 3, 5, 7, 8, 10, 12` → 31 Days
- `4, 6, 9, 11` → 30 Days
- `2` → 28 or 29 Days
- Anything else → Invalid Month

### Test Cases

`1 → 31 Days`  
`4 → 30 Days`  
`2 → 28 or 29 Days`  
`13 → Invalid Month`

---

## Q26. Simple Calculator

Take two numbers and an operator (`+`, `-`, `*`, `/`).

Perform the selected operation using `if-elif-else`.

### Test Cases

`10 5 + → 15`  
`10 5 - → 5`  
`10 5 * → 50`  
`10 5 / → 2.0`  
`10 5 % → Invalid Operator`

---

## Q27. Day Number

Take a number from `1` to `7`.

Print:

```text
1 → Monday
2 → Tuesday
3 → Wednesday
4 → Thursday
5 → Friday
6 → Saturday
7 → Sunday
```

For any other number, print:

```text
Invalid Day
```

### Test Cases

`1 → Monday`  
`5 → Friday`  
`7 → Sunday`  
`9 → Invalid Day`

---

## Q28. Performance Level

Take a score from `0` to `100`.

Print:

- `90+` → Excellent
- `75–89` → Very Good
- `60–74` → Good
- `40–59` → Average
- Below `40` → Needs Improvement

### Test Cases

`95 → Excellent`  
`82 → Very Good`  
`68 → Good`  
`50 → Average`  
`25 → Needs Improvement`

---

# Topic-4 — Logical Conditions

## Q29. College Admission Eligibility

A student is eligible if:

- marks are at least `60`, **and**
- attendance is at least `75`.

Take both values and print:

```text
Eligible
```

or:

```text
Not Eligible
```

### Test Cases

`70 80 → Eligible`  
`70 70 → Not Eligible`  
`55 90 → Not Eligible`

---

## Q30. Scholarship Eligibility

A student gets a scholarship if marks are at least `85` **or** family income is below `300000`.

Take marks and income.

### Test Cases

`90 500000 → Scholarship Available`  
`70 250000 → Scholarship Available`  
`70 500000 → No Scholarship`

---

## Q31. Weekend Check

Take a day name.

If it is `Saturday` or `Sunday`, print:

```text
Weekend
```

Otherwise print:

```text
Weekday
```

### Test Cases

`Saturday → Weekend`  
`Sunday → Weekend`  
`Monday → Weekday`

---

## Q32. Online Exam Access

A student can access an exam if:

- username is `"student"`, and
- password is `"python123"`.

Print:

```text
Access Granted
```

or:

```text
Access Denied
```

### Test Cases

`student python123 → Access Granted`  
`student wrong123 → Access Denied`  
`admin python123 → Access Denied`

---

## Q33. Delivery Availability

A delivery is available if the city is `"Ahmedabad"` or `"Gandhinagar"`.

### Test Cases

`Ahmedabad → Delivery Available`  
`Gandhinagar → Delivery Available`  
`Surat → Delivery Unavailable`

---

## Q34. Number Range Check

Take an integer.

Print `Inside Range` if the number is between `10` and `50`, inclusive. Otherwise print `Outside Range`.

### Test Cases

`10 → Inside Range`  
`35 → Inside Range`  
`50 → Inside Range`  
`55 → Outside Range`

---

## Q35. Secure Transaction

A transaction is allowed only when:

- amount is at most `50000`, and
- OTP entered is `"1234"`.

### Test Cases

`25000 1234 → Transaction Approved`  
`60000 1234 → Transaction Declined`  
`25000 9999 → Transaction Declined`

---

# Topic-5 — Nested `if`

## Q36. Login with Role

Take username and password.

First check whether the username is `"admin"`.

If the username is correct, check the password.

Expected results:

```text
admin + admin123 → Login Successful
admin + wrong → Wrong Password
student + anything → Invalid Username
```

Use nested `if`.

---

## Q37. Driving License Eligibility

Take age and test status.

First check whether age is at least `18`.

If yes, check whether test status is `"pass"`.

Print:

```text
License Approved
```

or the appropriate rejection message.

### Test Cases

`20 pass → License Approved`  
`20 fail → Test Not Passed`  
`16 pass → Age Not Eligible`

---

## Q38. ATM Withdrawal

Take account balance and withdrawal amount.

First check whether the withdrawal amount is within the balance.

If yes, check whether the amount is a multiple of `100`.

Print:

```text
Withdrawal Successful
```

or the appropriate message.

### Test Cases

`5000 1000 → Withdrawal Successful`  
`5000 1050 → Enter Amount in Multiples of 100`  
`500 1000 → Insufficient Balance`

---

## Q39. Exam Result with Attendance

Take marks and attendance.

First check attendance.

If attendance is at least `75`, check marks:

- `40+` → Pass
- below `40` → Fail

If attendance is below `75`, print:

```text
Not Eligible Due to Attendance
```

### Test Cases

`75 80 → Pass`  
`75 35 → Fail`  
`60 90 → Not Eligible Due to Attendance`

---

## Q40. Bank Account Verification

Take account type and balance.

First check whether account type is `"savings"`.

If it is, check whether balance is at least `1000`.

Print:

```text
Minimum Balance Maintained
```

or:

```text
Minimum Balance Not Maintained
```

For another account type, print:

```text
Unsupported Account
```

### Test Cases

`savings 5000 → Minimum Balance Maintained`  
`savings 500 → Minimum Balance Not Maintained`  
`current 5000 → Unsupported Account`

---

## Q41. Online Shopping Eligibility

Take order amount and payment method.

First check whether order amount is at least `500`.

If yes, check payment method:

- `card` → Card Payment Accepted
- `upi` → UPI Payment Accepted
- anything else → Unsupported Payment Method

If amount is below `500`, print:

```text
Minimum Order Amount Not Reached
```

### Test Cases

`800 card → Card Payment Accepted`  
`800 upi → UPI Payment Accepted`  
`800 cash → Unsupported Payment Method`  
`300 card → Minimum Order Amount Not Reached`

---

## Q42. Hostel Room Allocation

Take year of study and attendance.

First check whether the student is in year `2`, `3`, or `4`.

If eligible by year, check attendance.

Attendance `75+` →:

```text
Room Eligible
```

Otherwise:

```text
Attendance Too Low
```

For year `1`, print:

```text
Not Eligible by Year
```

### Test Cases

`3 80 → Room Eligible`  
`3 65 → Attendance Too Low`  
`1 90 → Not Eligible by Year`

---

## Q43. Internet Plan Upgrade

Take current plan and monthly usage.

First check whether the current plan is `"basic"`.

If it is basic:

- usage above `100` GB → Recommend Upgrade
- otherwise → Basic Plan Is Sufficient

For any other plan:

```text
Already on Higher Plan
```

### Test Cases

`basic 150 → Recommend Upgrade`  
`basic 80 → Basic Plan Is Sufficient`  
`premium 200 → Already on Higher Plan`

---

# Topic-6 — Nested `if-elif-else`

## Q44. Greatest of Three Numbers

Take three integers.

Use nested conditions to determine the greatest number.

Your program must also handle equality.

Possible outputs include:

```text
A is Greatest
B is Greatest
C is Greatest
A and B are Equal and Greatest
A and C are Equal and Greatest
B and C are Equal and Greatest
All are Equal
```

### Test Cases

`10 20 15 → B is Greatest`  
`30 10 30 → A and C are Equal and Greatest`  
`25 25 25 → All are Equal`  
`50 50 20 → A and B are Equal and Greatest`

---

## Q45. Student Result with Grade

Take marks and attendance.

First check attendance.

If attendance is at least `75`, determine the grade:

- `90+` → A
- `75–89` → B
- `60–74` → C
- `40–59` → D
- Below `40` → F

If attendance is below `75`, print:

```text
Not Eligible
```

### Test Cases

`95 80 → Grade A`  
`82 75 → Grade B`  
`65 90 → Grade C`  
`45 85 → Grade D`  
`30 90 → Grade F`  
`95 60 → Not Eligible`

---

## Q46. Employee Bonus

Take salary and performance rating.

First check whether salary is at least `30000`.

If yes, determine bonus based on rating:

- `5` → 20%
- `4` → 15%
- `3` → 10%
- otherwise → 5%

If salary is below `30000`, print:

```text
Not Eligible for Bonus
```

### Test Cases

`50000 5 → Bonus: 20%`  
`40000 4 → Bonus: 15%`  
`35000 3 → Bonus: 10%`  
`35000 2 → Bonus: 5%`  
`25000 5 → Not Eligible for Bonus`

---

## Q47. Bus Ticket Category

Take age and distance.

First check age category:

- below `5` → Free
- `5–59` → Regular
- `60+` → Senior

For a regular passenger, additionally check distance:

- up to `10 km` → Short Distance
- above `10 km` → Long Distance

### Test Cases

`3 20 → Free`  
`25 8 → Regular - Short Distance`  
`25 20 → Regular - Long Distance`  
`65 20 → Senior`

---

## Q48. Product Purchase Validation

Take product stock and payment status.

First check whether stock is greater than `0`.

If stock exists, check payment status:

- `"paid"` → Order Confirmed
- `"pending"` → Payment Pending
- anything else → Invalid Payment Status

If stock is `0`:

```text
Out of Stock
```

### Test Cases

`5 paid → Order Confirmed`  
`5 pending → Payment Pending`  
`5 failed → Invalid Payment Status`  
`0 paid → Out of Stock`

---

## Q49. Travel Ticket Validation

Take age and ticket type.

First check age:

- below `5` → Free Travel
- `5–59` → Regular Passenger
- `60+` → Senior Passenger

For regular passengers, check ticket type:

- `"AC"` → AC Ticket
- `"Sleeper"` → Sleeper Ticket
- anything else → Invalid Ticket Type

### Test Cases

`3 AC → Free Travel`  
`25 AC → AC Ticket`  
`25 Sleeper → Sleeper Ticket`  
`25 General → Invalid Ticket Type`  
`65 AC → Senior Passenger`

---

# Topic-7 — `match-case`

## Q50. Basic Menu

Take a menu number:

```text
1 → Add
2 → View
3 → Update
4 → Delete
```

Use `match-case`.

For any other number:

```text
Invalid Choice
```

### Test Cases

`1 → Add`  
`3 → Update`  
`4 → Delete`  
`8 → Invalid Choice`

---

## Q51. Day Name Using `match-case`

Take a number from `1` to `7`.

Use `match-case` to print the corresponding day.

### Test Cases

`1 → Monday`  
`4 → Thursday`  
`7 → Sunday`  
`9 → Invalid Day`

---

## Q52. Calculator Using `match-case`

Take two numbers and an operator.

Use `match-case` for:

```text
+  -  *  /
```

For any other operator:

```text
Invalid Operator
```

### Test Cases

`20 5 + → 25`  
`20 5 - → 15`  
`20 5 * → 100`  
`20 5 / → 4.0`  
`20 5 % → Invalid Operator`

---

## Q53. Traffic Signal Using `match-case`

Take a traffic signal color.

Use `match-case`:

```text
red → Stop
yellow → Wait
green → Go
```

Default:

```text
Invalid Signal
```

### Test Cases

`red → Stop`  
`yellow → Wait`  
`green → Go`  
`purple → Invalid Signal`

---

## Q54. Grade Message Using `match-case`

Take a grade:

```text
A → Excellent Performance
B → Very Good Performance
C → Good Performance
D → Needs Improvement
F → Failed
```

Use `match-case`.

### Test Cases

`A → Excellent Performance`  
`C → Good Performance`  
`F → Failed`  
`X → Invalid Grade`

---

## Q55. Mobile Service Menu

Take a service code:

```text
1 → Check Balance
2 → Recharge
3 → Data Usage
4 → Customer Support
```

Use `match-case`.

### Test Cases

`1 → Check Balance`  
`2 → Recharge`  
`4 → Customer Support`  
`9 → Invalid Service`

---

## Q56. Month Name Using `match-case`

Take a month number from `1` to `12`.

Use `match-case` to print the month name.

### Test Cases

`1 → January`  
`6 → June`  
`12 → December`  
`15 → Invalid Month`

---

## Q57. File Type Detector

Take a file extension:

```text
py → Python File
txt → Text File
pdf → PDF File
jpg → Image File
```

Use `match-case`.

For other extensions:

```text
Unknown File Type
```

### Test Cases

`py → Python File`  
`pdf → PDF File`  
`jpg → Image File`  
`exe → Unknown File Type`

---

# Topic-8 — Conditional Statements + Previous Concepts

## Q58. Student ID Validation

A student enters an ID in the format:

```text
BTECH-2026-CSE-105
```

Use `.split("-")` to extract:

- Degree
- Batch
- Branch
- Roll Number

Then use a conditional statement to check whether the branch is `"CSE"`.

Print:

```text
CSE Student
```

or:

```text
Non-CSE Student
```

### Test Cases

`BTECH-2026-CSE-105 → CSE Student`  
`BTECH-2026-ECE-105 → Non-CSE Student`

---

## Q59. Email Domain Checker

Take an email address.

Use `.split("@")` to extract the domain.

If the domain is `"gmail.com"`, print:

```text
Gmail User
```

Otherwise print:

```text
Other Email Provider
```

### Test Cases

`rahul@gmail.com → Gmail User`  
`student@yahoo.com → Other Email Provider`

---

## Q60. Username Generator Validation

Take a full name containing three words.

Create a username using the first and last name.

Then check whether the generated username contains `"."`.

Print:

```text
Valid Username Format
```

or:

```text
Invalid Username Format
```

### Test Cases

`Rahul Kumar Sharma → Valid Username Format`  
`Amit Singh Patel → Valid Username Format`

---

## Q61. Number Digit Analyzer

Take a positive integer.

First determine whether it is:

- 1 digit
- 2 digits
- 3 digits
- 4 or more digits

Then print the corresponding category.

### Test Cases

`7 → One Digit`  
`45 → Two Digits`  
`789 → Three Digits`  
`2026 → Four or More Digits`

---

## Q62. Shopping Bill Category

Take product price and quantity.

Calculate:

```text
Subtotal = price × quantity
```

Then apply:

- subtotal `5000+` → 20% discount
- subtotal `2000–4999` → 10% discount
- subtotal below `2000` → No discount

Display subtotal, discount percentage, and final amount.

### Test Cases

`1000 5 → Subtotal: 5000, Discount: 20%, Final: 4000.00`  
`500 5 → Subtotal: 2500, Discount: 10%, Final: 2250.00`  
`200 5 → Subtotal: 1000, Discount: 0%, Final: 1000.00`

---

## Q63. Electricity Bill Category

Take units consumed.

Calculate the bill using:

- up to `100` units → ₹5 per unit
- `101–300` units → ₹7 per unit
- above `300` units → ₹10 per unit

Use conditional statements to select the rate.

Display:

```text
Units: ...
Rate: ...
Bill: ...
```

### Test Cases

`80 → Rate: ₹5, Bill: ₹400`  
`200 → Rate: ₹7, Bill: ₹1400`  
`400 → Rate: ₹10, Bill: ₹4000`

---

## Q64. ATM Menu

Display a menu:

```text
1. Check Balance
2. Deposit
3. Withdraw
4. Exit
```

Take the choice using `match-case`.

For withdrawal, use a nested `if` to check whether the requested amount is available.

Assume initial balance is `10000`.

### Test Cases

`1 → Balance: 10000`  
`2 2000 → Deposit Successful, Balance: 12000`  
`3 3000 → Withdrawal Successful, Balance: 7000`  
`3 15000 → Insufficient Balance`  
`5 → Invalid Choice`

---

## Q65. Restaurant Ordering System

Use `match-case` for:

```text
1 → Pizza → ₹250
2 → Burger → ₹150
3 → Pasta → ₹200
4 → Sandwich → ₹120
```

Take quantity and calculate the total.

If total is `500` or more, apply a `10%` discount.

### Test Cases

`1 2 → Total: 500, Discount: 50.00, Final: 450.00`  
`2 2 → Total: 300, Discount: 0.00, Final: 300.00`  
`3 3 → Total: 600, Discount: 60.00, Final: 540.00`

---

## Q66. Exam Result Analyzer

Take:

- three subject marks
- attendance

Calculate total and average.

First check attendance.

If attendance is at least `75`, check the average:

- `90+` → Outstanding
- `75–89` → Very Good
- `60–74` → Good
- `40–59` → Pass
- below `40` → Fail

If attendance is below `75`:

```text
Not Eligible
```

### Test Cases

`90 92 95 85 → Outstanding`  
`80 78 82 80 → Very Good`  
`65 70 68 90 → Good`  
`45 50 48 80 → Pass`  
`30 35 25 90 → Fail`  
`90 90 90 60 → Not Eligible`

---

## Q67. Cab Fare Calculator

Take:

- distance in km
- ride type: `normal` or `premium`

Rules:

- Normal ride: ₹15 per km
- Premium ride: ₹25 per km

Use `match-case` to select the ride type.

Then use a conditional statement:

- distance above `20 km` → 10% extra surcharge
- otherwise → no surcharge

Calculate and display the final fare.

### Test Cases

`10 normal → Fare: 150.00`  
`10 premium → Fare: 250.00`  
`25 normal → Fare: 412.50`  
`25 premium → Fare: 687.50`

---

## Q68. College Admission System

Take:

- entrance score
- 12th percentage
- category: `general`, `obc`, or `sc`

Use `match-case` for the category and nested conditions for eligibility.

Rules:

- General: score `80+` and percentage `75+`
- OBC: score `70+` and percentage `70+`
- SC: score `60+` and percentage `60+`

Print:

```text
Admission Eligible
```

or:

```text
Admission Not Eligible
```

### Test Cases

`85 80 general → Admission Eligible`  
`75 68 obc → Admission Not Eligible`  
`65 65 sc → Admission Eligible`  
`70 80 general → Admission Not Eligible`

---

# Topic-9 — Debugging Conditional Programs

## Q69. Debug the Condition

Find and correct the error:

```python
age = input("Enter age: ")

if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")
```

The program should correctly compare the entered age as a number.

### Test Cases

`20 → Eligible`  
`15 → Not Eligible`

---

## Q70. Debug the Nested Condition

Find and correct the error:

```python
marks = int(input("Enter marks: "))

if marks >= 40:
    if marks >= 90:
        print("A")
    elif marks >= 75:
        print("B")
else:
    print("Fail")
```

Test the program for marks `95`, `80`, `50`, and `30`.

Explain why the current program does not give the correct result for every passing range, then correct it.

### Test Cases

`95 → A`  
`80 → B`  
`50 → Pass`  
`30 → Fail`

---

# Submission Guidelines

1. Write clean and readable Python code.
2. Use meaningful variable names.
3. Do not hard-code the values from the test cases.
4. Test every program with all provided test cases.
5. Use `if`, `if-else`, `if-elif-else`, nested conditions, or `match-case` exactly as requested.
6. Use `and` / `or` only where they are required by the problem.
7. Keep the indentation correct.
8. For `match-case`, include a default `_` case where the question requires handling invalid input.
9. Do not use loops, functions, lists, dictionaries, or other advanced concepts that have not been covered.
10. For debugging questions, first identify the reason for the error and then correct the program.
11. Do not manually print the expected answers for the given test cases; the program must calculate the result.
12. Test boundary values carefully, such as `18`, `40`, `75`, `90`, `100`, and range limits.
13. Make sure the program handles equality and invalid input cases wherever the question requires them.
14. Keep output clear, meaningful, and easy to verify.

---

# Final Challenge

After completing all questions, choose **any 3 problems** from Q58–Q68 and improve them by adding:

- Clear user prompts
- Well-formatted output using f-strings
- At least 3 additional test cases
- Proper handling of boundary values
- Short comments explaining the main decision-making logic

This challenge is optional but recommended for practice.


---

# Topic-10 — Output Prediction & Execution Flow

> **Important:** For the following questions, do not run the code first. Predict the output by carefully tracing which condition becomes true.

## Q71. Condition Order

Predict the output:

```python
marks = 85

if marks >= 40:
    print("Pass")
elif marks >= 75:
    print("Very Good")
else:
    print("Fail")
```

### Test Case

`85 → ?`

Then explain why the program does not print `Very Good`.

---

## Q72. Correct the Condition Order

The following program is intended to classify marks:

```python
marks = 85

if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 40:
    print("Pass")
else:
    print("Fail")
```

Predict the output.

Then explain why changing the order of the conditions can change the result.

### Test Cases

`95 → ?`  
`85 → ?`  
`50 → ?`  
`30 → ?`

---

## Q73. Nested `if` Execution Flow

Predict the output:

```python
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry Allowed")
    else:
        print("ID Required")
else:
    print("Underage")
```

### Test Case

`age = 20, has_id = True → ?`

Now predict the output if:

```text
age = 20
has_id = False
```

and:

```text
age = 16
has_id = True
```

---

## Q74. `match-case` and Default Case

Predict the output:

```python
choice = 5

match choice:
    case 1:
        print("Add")
    case 2:
        print("View")
    case 3:
        print("Delete")
    case _:
        print("Invalid Choice")
```

### Test Cases

`1 → ?`  
`3 → ?`  
`5 → ?`

Explain the purpose of `case _`.

---

## Q75. Final Execution Challenge

Predict the output without running the program:

```python
marks = 82
attendance = 80

if attendance >= 75:
    if marks >= 90:
        print("Grade A")
    elif marks >= 75:
        print("Grade B")
    elif marks >= 40:
        print("Pass")
    else:
        print("Fail")
else:
    print("Not Eligible")
```

### Test Cases

`82 80 → ?`  
`92 80 → ?`  
`55 80 → ?`  
`92 60 → ?`

After predicting the output, write in one sentence which condition is checked first and why.

---

# Updated Assignment Structure

The assignment now contains **75 questions**.

The final progression is:

- **Q1–Q8:** Basic `if`
- **Q9–Q18:** `if-else`
- **Q19–Q28:** `if-elif-else`
- **Q29–Q35:** Logical conditions
- **Q36–Q43:** Nested `if`
- **Q44–Q49:** Nested `if-elif-else`
- **Q50–Q57:** `match-case`
- **Q58–Q68:** Integrated real-life problems
- **Q69–Q70:** Debugging
- **Q71–Q75:** Output prediction & execution flow
