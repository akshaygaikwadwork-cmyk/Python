#Syntax
"""
if condition:
    # code to execute if condition is True
    pass
elif another_condition:
    # code to execute if another_condition is True
    pass
else:
    # code to execute if condition is False
    pass
"""

#Example
#1. Traffic Light
light_color = input("Enter the traffic light color (red, yellow, green): ").lower()
if light_color == "red":
    print("Stop!")
elif light_color == "yellow":
    print("Get ready to go!")
elif light_color == "green":
    print("Go!")
else:
    print("Invalid traffic light color.")


#Nested if-else
#syntax
"""
if condition1:
    if condition2:
        # code to execute if both condition1 and condition2 are True
        pass
    else:
        # code to execute if condition1 is True but condition2 is False
        pass
else:    
    # code to execute if condition1 is False
    pass
"""

#Example
#2. Driving Eligibility
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to drive.")
    has_license = input("Do you have a driving license? (yes/no): ").lower()
    if has_license == "yes":
        print("You can drive legally.")
    else:
        print("You need to obtain a driving license to drive legally.")
else:
    print("You are not eligible to drive yet. You need to wait until you are 18 years old.")
