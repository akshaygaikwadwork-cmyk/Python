#Q.1 Write a program marks of a student and print the grade based on the following criteria:
#Marks >= 90: Grade A
#Marks >= 80 and < 90: Grade B
#Marks >= 70 and < 80: Grade C
#Marks >= 60 and < 70: Grade D
#Marks < 60: Grade F
marks = float(input("Enter the marks of the student: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 80 and marks < 90:
    print("Grade: B")
elif marks >= 70 and marks < 80:
    print("Grade: C")
elif marks >= 60 and marks < 70:
    print("Grade: D")
else:
    print("Grade: F")

#Q.2. Write a program to check entered number is odd or even.
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

#Q.3. Find the largest of three numbers entered by the user.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
if num1 >= num2 and num1 >= num3:
    print("The largest number is: ", num1)
elif num2 >= num1 and num2 >= num3:
    print("The largest number is: ", num2)
else:
    print("The largest number is: ", num3)

#Q.4. Write a program entered number is multiple of 7 or not.
number = int(input("Enter a number: "))
if number % 7 == 0:
    print("The number is a multiple of 7.")
else:
    print("The number is not a multiple of 7.")