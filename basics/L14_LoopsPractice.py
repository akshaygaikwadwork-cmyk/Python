# Using While loop :
# Q.1. Print numbers from 1 to 100.
i = 1
while i <= 100:
    print(i)
    i += 1  # Increment the value of i by 1 in each iteration to avoid infinite loop

# Q.2. Print numbers from 100 to 1.
i = 100
while i >= 1:
    print(i)
    i -= 1  # Decrement the value of i by 1 in each iteration to avoid infinite loop

# Q.3. Print the multiplication table of a number n entered by the user.
n = int(input("Enter a number to print its multiplication table: "))
i = 1
while i <= 10:
    print(f"{n} x {i} = {n * i}")
    i += 1  # Increment the value of i by 1 in each iteration to print the next line of the multiplication table

# Q.4. Print the elements of the following list using a loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1  # Increment the value of i by 1 in each iteration to access the next element of the list

# Linear search : Method of searching an element in a list or tuple by checking each element one by one until the desired element is found or the end of the list/tuple is reached. It is a simple and straightforward search algorithm that does not require the list/tuple to be sorted.
# Binary search : Method of searching an element in a sorted list or tuple by repeatedly dividing the search interval in half. If the value of the search key is less than the item in the middle of the interval, the search continues in the lower half, or if it is greater, it continues in the upper half. This process continues until the value is found or the interval is empty. 
# Q.5. Search for a number x in this tuple using loop: 
# (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
numbers_tuple = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = int(input("Enter a number to search in the tuple: "))
found = False
i = 0
while i < len(numbers_tuple):
    if numbers_tuple[i] == x:
        found = True
        break  # Exit the loop if the number is found
    i += 1  # Increment the value of i by 1 in each iteration to check the next element of the tuple

if found:
    print(f"Number {x} is found in the tuple.")
else:
    print(f"Number {x} is not found in the tuple.")

# Using For loop :

# Q.1. Print numbers from 1 to 100.
for i in range(1, 101):
    print(i)

# Q.2. Print numbers from 100 to 1.
for i in range(100, 0, -1):
    print(i)

# Q.3. Print the multiplication table of a number n entered by the user.
n = int(input("Enter a number to print its multiplication table: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")


# Q.4. Print the elements of the following list using a loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for num in numbers:
    print(num)


# Q.5. Search for a number x in this tuple using loop: 
# (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
numbers_tuple = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = int(input("Enter a number to search in the tuple: "))
found = False
for num in numbers_tuple:
    if num == x:
        found = True
        break  # Exit the loop if the number is found
if found:
    print(f"Number {x} is found in the tuple.")
else:
    print(f"Number {x} is not found in the tuple.")

# Using for loop with range() function:

# Q.1. Print numbers from 1 to 100.
for i in range(1, 101):
    print(i)

# Q.2. Print numbers from 100 to 1.
for i in range(100, 0, -1):
    print(i)

# Q.3. Print the multiplication table of a number n entered by the user.
n = int(input("Enter a number to print its multiplication table: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

# Practice problems on loops are essential for understanding how to control the flow of your program and perform repetitive tasks efficiently. By working through these problems, you can improve your problem-solving skills and become more proficient in using loops in Python.

# Q.1. Write a program to find the sum of first n natural numbers entered by the user using a while loop.
n = int(input("Enter a number n to find the sum of first n natural numbers: "))
sum_natural = 0
i = 1
while i <= n:
    sum_natural += i  # Add the current value of i to the sum
    i += 1  # Increment the value of i by 1 in each iteration to add the next natural number to the sum
print(f"The sum of first {n} natural numbers is: {sum_natural}")

# Q.2. Write a program to calculate the factorial of a number n entered by the user using a for loop.
n = int(input("Enter a number n to calculate its factorial: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i  # Multiply the current value of i with the factorial to calculate the factorial of n
print(f"The factorial of {n} is: {factorial}")