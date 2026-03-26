# Q.1. Write a function to print the length of a list. (list is the parameter of the function)
# Ans:
def print_length(lst):
    print(f"The length of the list is: {len(lst)}")
my_list = [1, 2, 3, 4, 5]
print_length(my_list)  # Output: The length of the list is: 5

# Q.2. Write a function to print the elements of a list in a single line. (list is the parameter of the function)
# Ans:
# 1st way
def print_single_line(elements):
    print(" ".join(str(e) for e in elements))
my_list = [1, 2, 3, 4, 5]
print_single_line(my_list)  # Output: 1 2 3 4

# 2nd way
def print_single_line(elements):
    for e in elements:
        print(e, end=" ")
    print()  # for a new line after printing all elements
my_list = [1, 2, 3, 4, 5]
print_single_line(my_list)  # Output: 1 2 3 4 5

# Q.3. Write a function to find the factorial of a number. (number is the parameter of the function)
# Ans:
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))  # Output: 120

# Q.4. Write a function to convert USD to INR. (amount in USD is the parameter of the function)
# Ans:
def convert_usd_to_inr(usd_amount):
    exchange_rate = 73.5  # Example exchange rate (1 USD = 73.5 INR)
    return usd_amount * exchange_rate
print(convert_usd_to_inr(100))  # Output: 7350.0

# Q.5 Write a function to check if a number is odd or even. (number is the parameter of the function)
# Ans:
def check_odd_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(check_odd_even(5))  # Output: Odd
print(check_odd_even(6))  # Output: Even