#1
age = "25"
age = int(age)
print(age)
print(type(age))

#2
marks = "75.5"
marks = float(marks)
print(marks)
print(type(marks))

#3
number = 50
number = float(number)
print(number)
print(type(number))

#4
marks = 85.9
mark=int(marks)
print(marks)
print(type(mark))

#5
roll_number = 101
number=str(roll_number)
print(roll_number)
print(number)

#6
x="18"
y="92.5"
z=100
q=45.8
a=int(x)
b=float(y)
c=str(z)
d=int(q)
print(a,type(a))
print(b,type(b))
print(c,type(c))
print(d,type(d))

#7
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

#8
age = "19"
new_age = int(age) + 1
print("Age:", new_age)

#9
marks="85"
new_marks=int(marks)+5
print(new_marks)

#10
price = "1499.50"
new_price=float(price)
delivery_charges=99.50
print(new_price+delivery_charges)

#11
a = 20
b = 6
add=a+b
subtract=a-b
multiplication=a*b
division=a/b
floor_division=a//b
reminder=a%b
power=a**b
print(add)
print(subtract)
print(multiplication)
print(division)
print(floor_division)
print(reminder)
print(power)

#12
a = 17
b = 5
print(a / b)
print(a // b)
print(a % b)
#/ gives the regular division result, // gives the floor division result, and % gives the remainder after division.

#13
result = (10 + 5 )* 2
print(result)

#14
result = 20 - (4 * 3) + 2
print(result)

#15
#output= 8,9,100
side = 5
area = side ** 2
print(area)

#16
notebook = 80
pen = 20
pencil = 10
total_amount=notebook+pen+pencil
print(total_amount)

#17
total_notebook=3
price=50
total_price=total_notebook*price
print(total_price)
pen=2
cost=15
total_cost=pen*cost
print(total_cost)
calculator=1
price=500
print(price)
bill=total_price+total_cost+price
print(bill)

#18
students = 47
group_size = 5
complete_groups = students // group_size
students_left = students % group_size
print("Complete Groups:", complete_groups)
print("Students Left:", students_left)

#19
python = 85
mathematics = 78
physics = 92
total=python+mathematics+physics
print("Total Marks:",total)
average_marks=total/3
print("Average Marks:",average_marks)

#20
english = 78
mathematics = 85
python = 92
physics = 81
chemistry = 74
total=english+mathematics+python+physics+chemistry
print(total)
percentage=(total/500)*100
print(percentage)

#21
number = 583
ones_digit = number % 10
print("Ones Digit:", ones_digit)

#22
number=583
tens_digit=(number%100)//10
print("tens Digit:", tens_digit)

#23
number = 583
hundred_digit=number//100
print("hundred Digit:", hundred_digit)

#24
number = 746
ones_digit = number % 10
tens_digit=(number%100)//10
hundred_digit=number//100
print("ones digit:",ones_digit)
print("tens_digit:",tens_digit)
print("hundred_digit:",hundred_digit)

#25
number = 5829
ones_digit=number%10
tens_digit=(number%100)//10
hundred_digit=(number%1000)//100
thousands_digit=number//1000
print("ones digit:",ones_digit)
print("tens digit:",tens_digit)
print("hundreds digit:",hundred_digit)
print("thousand digit:",thousands_digit)

#26
number = 583
ones_digit=number%10
tens_digit=(number%100)//10
hundred_digit=number//100
print(ones_digit+tens_digit+hundred_digit)

#27
number = 4726
ones_digit=number%10
tens_digit=(number%100)//10
hundred_digit=(number%1000)//100
thousands_digit=number//1000
print(ones_digit+tens_digit+hundred_digit+thousands_digit)

#28
number = 234
ones_digit=number%10
tens_digit=(number%100)//10
hundred_digit=number//100
print("product of digit:",ones_digit*tens_digit*hundred_digit)

#29
number = 583
number = 583

ones = number % 10
tens = (number // 10) % 10
hundreds = number // 100
reversed_number = ones * 100 + tens * 10 + hundreds
print("Original Number:", number)
print("Reversed Number:", reversed_number)

#30
number = 4726
ones_digit=number%10
tens_digit=(number%100)//10
hundred_digit=(number%1000)//100
thousands_digit=number//1000
reversed=ones_digit*1000+tens_digit*100+hundred_digit*10+thousands_digit
print("original_number:",number)
print("reversed_number:",reversed)

#31
number = 5834
thousands = (number // 1000) * 1000
hundreds = (number // 100) % 10 * 100
tens = (number // 10) % 10 * 10
ones = number % 10
print("Thousands Place:", thousands)
print("Hundreds Place:", hundreds)
print("Tens Place:", tens)
print("Ones Place:", ones)

#32
number = 583
hundreds_digit = number // 100
ones_digit = number % 10
difference = hundreds_digit - ones_digit
print("Difference:", difference)

#33
number = 583
ones = number % 10
print("Ones Digit:", ones)

#34
number = 9365
thousands = number // 1000
hundreds = (number // 100) % 10
tens = (number // 10) % 10
ones = number % 10
print("Thousands Digit:", thousands)
print("Hundreds Digit:", hundreds)
print("Tens Digit:", tens)
print("Ones Digit:", ones)

#35
hundreds = 5
tens = 8
ones = 3
number = hundreds * 100 + tens * 10 + ones
print("Number:", number)

#36
principal = 10000
rate = 5
time = 2
simple_interest = (principal * rate * time) / 100
print("Simple Interest:", simple_interest)

#37
length = 15
width = 8
area = length * width
perimeter = 2 * (length + width)
print("Area:", area)
print("Perimeter:", perimeter)

#38
radius = 7
pi = 3.14
area = pi * radius ** 2
print("Area:", area)

#39
celsius = 35
fahrenheit = (celsius * 9 / 5) + 32
print("Fahrenheit:", fahrenheit)

#40
total_seconds = 367
minutes = total_seconds // 60
seconds = total_seconds % 60
print("Minutes:", minutes)
print("Seconds:", seconds)

#41
total_seconds = 7384
hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60
print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", seconds)

#42
basic_salary = 25000
hra = 5000
travel_allowance = 2500
tax_deduction = 3000
gross_salary = basic_salary + hra + travel_allowance
net_salary = gross_salary - tax_deduction
print("Gross Salary:", gross_salary)
print("Net Salary:", net_salary)

#43
distance = 120
mileage = 20
fuel_price = 100
fuel_required = distance / mileage
total_cost = fuel_required * fuel_price
print("Fuel Required:", fuel_required, "litres")
print("Total Fuel Cost:", total_cost)

#44
price = "2500"
discount = "10"
price = float(price)
discount = float(discount)
discount_amount = price * discount / 100
final_price = price - discount_amount
print("Discount Amount:", discount_amount)
print("Final Price:", final_price)

#45
price = "1200"
quantity = "4"
price = int(price)
quantity = int(quantity)
total_price = price * quantity
print("Price:", price)
print("Quantity:", quantity)
print("Total Price:", total_price)

#46
python_marks = "85"
math_marks = "78"
physics_marks = "91"
python_marks = int(python_marks)
math_marks = int(math_marks)
physics_marks = int(physics_marks)
total = python_marks + math_marks + physics_marks
average = total / 3
print("Total Marks:", total)
print("Average Marks:", average)

#47
price = "1500"
quantity = "2"
tax_rate = "5"
price = float(price)
quantity = int(quantity)
tax_rate = float(tax_rate)
subtotal = price * quantity
tax_amount = subtotal * tax_rate / 100
final_bill = subtotal + tax_amount
print("Subtotal:", subtotal)
print("Tax Amount:", tax_amount)
print("Final Bill:", final_bill)

#48
price = 2000
discount = 15
gst = 18
discount_amount = price * discount / 100
price_after_discount = price - discount_amount
gst_amount = price_after_discount * gst / 100
final_price = price_after_discount + gst_amount
print("Discount Amount:", discount_amount)
print("Price After Discount:", price_after_discount)
print("GST Amount:", gst_amount)
print("Final Price:", final_price)

#49
price = "500"
quantity = 3
price = int(price)
total = price * quantity
print("Total:", total)

#50
marks1 = "80"
marks2 = "75"
marks3 = "90"
marks1 = int(marks1)
marks2 = int(marks2)
marks3 = int(marks3)
total = marks1 + marks2 + marks3
print("Total Marks:", total)

#51
# 50
# 50
# <class 'str'>
# <class 'int'>

#52
# 99.99
# 99
# The decimal portion .99 is removed when converting the float to an integer. Python does not round 99.99 to 100.

#53
# 17
# 7
# 60
# 2.4
# 2
# 2

#54
# 20
# 30
# 7.0
# 2.5
# Without parentheses, multiplication/division is performed before addition. Parentheses force the expression inside them to be calculated first.

#55
# 4
# 8
# 6
# a = ones digit
# c = tens digit
# d = hundreds digit

#56
student_name = "Ravi"
marks = "85"

total = int(marks) + 5

print("Student:", student_name)
print("Marks:", total)
print("Type:", type(total))

#57
number = 746
ones = number % 10
tens = (number // 10) % 10
hundreds = number // 100
print("Ones:", ones)
print("Tens:", tens)
print("Hundreds:", hundreds)

#58
price = "2000"
discount = "15"
price = float(price)
discount = float(discount)
discount_amount = price * discount / 100
final_price = price - discount_amount
print("Discount:", discount_amount)
print("Final Price:", final_price)

#59
student_name = "Rahul"
marks1 = "85"
marks2 = "90"
marks3 = "78"
marks1 = int(marks1)
marks2 = int(marks2)
marks3 = int(marks3)
total = marks1 + marks2 + marks3
average = total / 3
print("Student:", student_name)
print("Total Marks:", total)
print("Average:", average)
print("Marks Type:", type(total))

#60
number = 5836
ones_digit=number%10
tens_digit=(number%100)//10
hundred_digit=(number%1000)//100
thousands_digit=number//1000
sum=ones_digit+tens_digit+hundred_digit+thousands_digit
reversed=ones_digit*1000+tens_digit*100+hundred_digit*10+thousands_digit
print("Reversed:",reversed)
print("Sum of digit:",sum)

#Part-B
price = "1250"
quantity = "4"
discount = "10"
price = float(price)
quantity = int(quantity)
discount = float(discount)
subtotal = price * quantity
discount_amount = subtotal * discount / 100
final_amount = subtotal - discount_amount
print("Subtotal:", subtotal)
print("Discount Amount:", discount_amount)
print("Final Amount:", final_amount)





