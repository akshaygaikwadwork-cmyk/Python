# Loops
# Loops are used to repeat a block of code multiple times. In Python, there are two main types of loops: for loops and while loops.
# 1. For Loop
# A for loop is used to iterate over a sequence (like a list, tuple, or string) or other iterable objects. It executes a block of code for each item in the sequence.
# Syntax:
# for variable in sequence:
#     # block of code to be executed    
# Example:
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)  # Output: apple, banana, cherry

# else clause can be used with loops to execute a block of code when the loop has completed all iterations without encountering a break statement.
# Example:
for i in range(5):
    print(i)  # Output: 0, 1, 2, 3, 4
else:
    print("Loop completed successfully!")  # This will be printed after the loop finishes iterating through all numbers from 0 to 4.

# 2. While Loop
# A while loop is used to execute a block of code as long as a specified condition is true. It is useful when the number of iterations is not known beforehand.
# Syntax:
# while condition:
#     # block of code to be executed
# Example:
count = 0
while count < 5:
    print(count)  # Output: 0, 1, 2, 3, 4
    count += 1  # Increment the count to avoid infinite loop
# Loops can also be nested, meaning you can have a loop inside another loop. This is useful for working with multi-dimensional data structures like lists of lists.

# Example of nested loops:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for element in row:
        print(element)  # Output: 1, 2, 3, 4, 5, 6, 7, 8, 9 - Each element of the matrix is printed on a new line.


# Note: Be careful with while loops, as they can lead to infinite loops if the condition never becomes false. Always make sure to include a way to break out of the loop or ensure that the condition will eventually become false.

# break and continue statements can be used to control the flow of loops. 
# The break statement is used to exit a loop prematurely.
# The continue statement is used to skip the current iteration and move to the next one.

# Example of break and continue:
for i in range(10):
    if i == 5:
        break  # Exit the loop when i is 5
    if i % 2 == 0:
        continue  # Skip the rest of the loop for even numbers
    print(i)  # Output: 1, 3 (only odd numbers less than 5 are printed)


# You can also use the range() function to generate a sequence of numbers for the loop to iterate over.
# default start is 0, default step is 1, and stop is required. The range() function generates a sequence of numbers from the start (inclusive) to the stop (exclusive) with a specified step can be positive or negative ex -1 or 1.
# The range() function can take one, two, or three arguments:
# Example:
# range(stop) - Generates numbers from 0 to stop-1
for i in range(5):
    print(i)  # Output: 0, 1, 2, 3, 4

# range(start, stop) - Generates numbers from start to stop-1
for i in range(1, 6):
    print(i)  # Output: 1, 2, 3, 4, 5

# range(start, stop, step) - Generates numbers from start to stop-1 with a step of step
for i in range(0, 10, 2):
    print(i)  # Output: 0, 2, 4, 6, 8 (step of 2)


# Pass Statement
# The pass statement is a null operation; it does nothing when executed. It is used as a placeholder in situations where a statement is syntactically required but no action is needed or when you want to create an empty block of code.
# Example of pass statement:
for i in range(5):
    if i % 2 == 0:
        pass  # Do nothing for even numbers
    else:
        print(i)  # Output: 1, 3 (only odd numbers are printed)