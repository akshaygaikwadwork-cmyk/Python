#Conversion : Python is a dynamically typed language, which means that you don't need to declare the type of a variable when you create it. However, sometimes you may want to convert a variable from one type to another. This is called type conversion or type casting.
#1)
a = 2
b = 3.5
sum = a + b
print("Sum:", sum) #5.5
#2)
num1 = 10
num2 = "20"
# This will raise a TypeError because you cannot add an integer and a string
# sum = num1 + num2
# To fix this, you can convert num2 to an integer before adding


#Casting : You can use built-in functions to convert between types. For example:
#1)
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
result = x + y
print("Result:", result) #3
#2)
num1 = 10
num2 = "20"
sum = num1 + int(num2) # Convert num2 to an integer before adding
print("Sum:", sum) #30

#3) You can also convert a number to a string using the str() function:
num = 10
num_str = str(num) # Convert num to a string
print("num_str:", num_str) # "10"

#4) You can convert a string to a float using the float() function:
num_str = "3.14"
num_float = float(num_str) # Convert num_str to a float
print("num_float:", num_float) # 3.14

#5) You can convert a boolean to an integer using the int() function:
is_adult = True
is_adult_int = int(is_adult) # Convert is_adult to an integer   
print("is_adult_int:", is_adult_int) # 1

#6) You can convert an integer to a boolean using the bool() function:
num = 0
num_bool = bool(num) # Convert num to a boolean
print("num_bool:", num_bool) # False

#7) You can also convert a string to an integer using the int() function, but the string must represent a valid integer. For example:
num_str = "abc"
# This will raise a ValueError because "abc" cannot be converted to an integer
# num_int = int(num_str)
# print("num_int:", num_int) # This line will not be executed because of the error above