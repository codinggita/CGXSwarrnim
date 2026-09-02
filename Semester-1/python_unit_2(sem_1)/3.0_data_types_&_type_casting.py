##23
# Creating variables of five basic Python types

student_name = "Diya"       # String
student_age = 15            # Integer
student_height = 5.4        # Float
is_active = True             # Boolean
student_data = [1, 2, 3]    # List

print(type(student_name))
print(type(student_age))
print(type(student_height))
print(type(is_active))
print(type(student_data))

#D. Practicle Problems
##24
student_name = "Diya"
student_age = 15
student_height = 5.4
is_student = True
student_result = None

# Identifying the type of each variable
print(type(student_name))
print(type(student_age))
print(type(student_height))
print(type(is_student))
print(type(student_result))

##25
a=50
b=50.0
c="50"
print(type(a))
print(type(b))
print(type(c))

##26
a=True
b="True"
print(type(a))
print(type(b))
#they are different because the data type varies in a their is no upper quotation in (a) so it is a str type

##27
a=None
b="None"
print(type(a))
print(type(b))
#it is different because a contain none data type and b is in quotation so it shows str type

##28
# First assign an integer
value = 25
print(type(value))

# Reassign a string
value = "Hello"
print(type(value))
#Explanation:
#Initially, value stores an integer (int). After reassignment, it stores a string (str). The variable name stays the same, but its value and type change. This shows that Python variables can refer to values of different types.

##29
product_name = "Notebook"
product_quantity = 10
product_price = 49.99
product_available = True
product_discount = None

print(type(product_name))
print(type(product_quantity))
print(type(product_price))
print(type(product_available))
print(type(product_discount))

##30
value_1 = 10
value_2 = 10.0
value_3 = "10"
value_4 = True
value_5 = "True"
value_6 = None
value_7 = "None"

print(type(value_1))
print(type(value_2))
print(type(value_3))
print(type(value_4))
print(type(value_5))
print(type(value_6))
print(type(value_7))

#Value	Type
#10	    int
#10.0	float
#"10"	str
#True	bool
#"True"	str
#None	NoneType
#"None"	str

#Key idea: Quotation marks make a value a string, while True and None without quotes are special Python values.