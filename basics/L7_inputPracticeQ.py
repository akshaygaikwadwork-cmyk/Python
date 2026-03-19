#Q.1
# This program takes two numbers as input from the user, adds them together, and prints the result.
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
sum = float(num1) + float(num2) # Convert the input strings to floats before adding
print("The sum of", num1, "and", num2, "is:", sum)

#Q.2
# This program takes one number as input from the user, squares it, and prints the result.
num3 = input("Enter the number: ")
areaOfSquare = float(num3) * float(num3) # Convert the input strings to floats before multiplying
print("The area of the square with side", num3, "is:", areaOfSquare)

#Q.3
# This program takes two numbers as input from the user, calculates their average, and prints the result.
num4 = input("Enter first number: ")
num5 = input("Enter second number: ")
average = (float(num4) + float(num5)) / 2 # Convert the input strings to floats before adding and dividing
print("The average of", num4, "and", num5, "is:", average)

#Q.4
# This program takes two numbers as input from the user and compares them to determine which one is greater or if they are equal.
num6 = int(input("Enter first number: "))
num7 = int(input("Enter second number: "))
print(num6>=num7)