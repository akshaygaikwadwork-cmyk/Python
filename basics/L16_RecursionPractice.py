# Q.1. Write a recursive function to calculate the sum of first n natural numbers. (n is the parameter of the function)

# Ans:
def sum_natural(n):
    if n <= 0:  # Base case: when n is 0 or negative, return 0
        return 0
    else:
        return n + sum_natural(n - 1)  # Recursive call with modified parameter (n-1)
print(sum_natural(5))  # Output: 15

# Q.2. Write a recursive function to print all elements in a list.
# Ans:
# 1st way
def print_list(lst, index=0):
    if index >= len(lst):  # Base case: when index is out of bounds, stop the recursion
        return
    print(lst[index])  # Print the current element
    print_list(lst, index + 1)  # Recursive call with modified parameter (index+1)
my_list = [1, 2, 3, 4, 5]
print_list(my_list)  # Output: 1 2 3 4 5

# 2nd way
def print_list(lst):
    if not lst:  # Base case: when the list is empty, stop the recursion
        return
    print(lst[0])  # Print the first element of the list
    print_list(lst[1:])  # Recursive call with modified parameter (the rest of the list)
my_list = [1, 2, 3, 4, 5]
print_list(my_list)  # Output: 1 2 3 4 5