# Recursion
# A function that calls itself is called a recursive function. It is a powerful programming technique that allows you to solve problems by breaking them down into smaller, more manageable subproblems. A recursive function typically has two main components: a base case that stops the recursion and a recursive case that continues to call the function until it reaches the base case.
# Syntax of a Recursive Function
# def function_name(parameters):
#     if base_case_condition:
#         return base_case_value
#     else:
#         return function_name(modified_parameters)  # Recursive call with modified parameters

# Example print number from n to 1 using recursion
def print_numbers(n):
    if n <= 0:  # Base case: when n is 0 or negative, stop the recursion
        return
    print(n)  # Print the current number
    print_numbers(n - 1)  # Recursive call with modified parameter (n-1)

print_numbers(5)  # Output: 5 4 3 2 1

# Factorial of a number using recursion
def factorial(n):
    if n == 0 or n == 1:  # Base case: factorial of 0 or 1 is 1
        return 1
    else:
        return n * factorial(n - 1)  # Recursive call with modified parameter (n-1)
print(factorial(5))  # Output: 120