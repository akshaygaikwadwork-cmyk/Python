# Function
# A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.
# Creating a Function
# Syntax for creating a function in Python is as follows:
# def function_name(parameters):
#     # code to be executed
# Example
def greet(name):
    print(f"Hello, {name}!")

# Calling a Function
greet("Alice")  # Output: Hello, Alice!

# Function with Return Value
def add(a, b):
    return a + b
result = add(5, 3)
print(result)  # Output: 8

# Function with Default Parameters
def greet(name="Guest"):
    print(f"Hello, {name}!")
greet()  # Output: Hello, Guest!
greet("Bob")  # Output: Hello, Bob!

# Function with Variable Number of Arguments
def sum_all(*args):
    return sum(args)
print(sum_all(1, 2, 3))  # Output: 6
print(sum_all(4, 5))     # Output: 9

# Function with Keyword Arguments
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")
greet("Charlie")  # Output: Hello, Charlie!
greet("Dave", greeting="Hi")  # Output: Hi, Dave!

# Function with Docstring : A docstring is a string literal that occurs as the first statement in a function, method, class, or module definition. It is used to document the purpose and usage of the function. You can access the docstring using the __doc__ attribute of the function.
def greet(name):
    """This function greets the person with the given name."""
    print(f"Hello, {name}!")
print(greet.__doc__)  # Output: This function greets the person with the given name.    


# Print in a Single Line
# 1st way
my_list = [1, 2, 3, 4, 5]
def print_single_line(elements):
    print(" ".join(str(e) for e in elements))

# 2nd way
def print_single_line(elements):
    for e in elements:
        print(e, end=" ")
    print()  # for a new line after printing all elements

#Types of Functions
# 1. Built-in Functions: These are functions that are provided by Python and can be used directly without any need for definition. Examples include print(), len(), type(), etc.
# 2. User-defined Functions: These are functions that you create yourself to perform specific tasks. You can define them using the def keyword as shown in the examples above.

# 1. Built-in Functions
# Example of built-in functions:
print("Hello, World!")  # Output: Hello, World!
length = len("Hello")  # Output: 5
print(length)
number = 10
print(type(number))  # Output: <class 'int'>
range(1, 10)  # Output: range(1, 10)
# 2. User-defined Functions
# Example of user-defined functions:
def print_values():
    print("Value 1")
    print("Value 2")
print_values()
def calculate_area(radius):
    import math
    area = math.pi * radius ** 2
    return area
radius = 5
area = calculate_area(radius)
print(area)

