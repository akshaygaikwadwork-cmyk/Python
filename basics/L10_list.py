# List
# [] - List is a collection which is ordered and mutable i.e. changeable. Allows duplicate members.
mylist = ["apple", "banana", "cherry"]
print(mylist)
print(type(mylist))  # Output: <class 'list'>
print(len(mylist))  # Output: 3
# Accessing items
print("Accessing items: ")
print(mylist[0])  # Output: apple
print(mylist[1])  # Output: banana
print(mylist[2])  # Output: cherry
# Changing item value
print("Changing item value: ")
mylist[1] = "blueberry"
print(mylist)  # Output: ['apple', 'blueberry', 'cherry']
# Looping through a list
print("Looping through a list: ")
for item in mylist:
    print(item)
# Adding items
print("Adding items: ")
mylist.append("orange")  # Adds 'orange' to the end of the list
print(mylist)  # Output: ['apple', 'blueberry', 'cherry', 'orange']
mylist.insert(1, "grape")  # Inserts 'grape' at index 1
print(mylist)  # Output: ['apple', 'grape', 'blueberry', 'cherry', 'orange']
# Removing items
print("Removing items: ")
mylist.remove("grape")  # Removes 'grape' from the list and first occurrence of 'grape' will be removed if there are multiple 'grape' in the list
print(mylist)  # Output: ['apple', 'blueberry', 'cherry', 'orange']
mylist.pop(2)  # Removes the item at index 2 (blueberry)
print(mylist)  # Output: ['apple', 'blueberry', 'orange']
mylist.clear()  # Removes all items from the list
print(mylist)  # Output: []
#Sublist
print("Sublist: ")
mylist = ["apple", "banana", "cherry", "orange", "grape"]
sublist = mylist[1:4]  # Creates a sublist from index 1 to 3 (not including index 4)
print(sublist)  # Output: ['banana', 'cherry', 'orange']
# List methods
print("List methods: ")
mylist.sort()  # Sorts the list in ascending order
print(mylist)  # Output: ['apple', 'banana', 'cherry', 'grape', 'orange']
mylist.sort(reverse=True)  # Sorts the list in descending order
print(mylist)  # Output: ['orange', 'grape', 'cherry', 'banana', 'apple']
mylist.reverse()  # Reverses the order of the list
print(mylist)  # Output: ['apple', 'banana', 'cherry', 'grape', 'orange']
mylist2 = ["kiwi", "melon"]
mylist.extend(mylist2)  # Extends mylist by adding elements from mylist
print(mylist)  # Output: ['apple', 'banana', 'cherry', 'grape', 'orange', 'kiwi', 'melon']
mylist3 = mylist.copy()  # Creates a copy of mylist
print(mylist3)  # Output: ['apple', 'banana', 'cherry', 'grape', 'orange', 'kiwi', 'melon']

# Difference between list and string:
# 1. Mutability: Lists are mutable, meaning you can change their content after creation, while strings are immutable, meaning once they are created, their content cannot be changed.
# 2. Syntax: Lists are defined using square brackets [], while strings are defined using quotes ('' or "").
# 3. Performance: Strings are generally faster than lists because of their immutability, which allows for certain optimizations in memory and performance.

# Difference between list and tuple:
# 1. Mutability: Lists are mutable, meaning you can change their content after creation, while tuples are immutable, meaning once they are created, their content cannot be changed.
# 2. Syntax: Lists are defined using square brackets [], while tuples are defined using parentheses ().
# 3. Performance: Tuples are generally faster than lists because of their immutability, which allows for certain optimizations in memory and performance.

# Difference between list and set:
# 1. Mutability: Lists are mutable, meaning you can change their content after creation, while sets are also mutable, but they do not allow duplicate members and are unordered.
# 2. Syntax: Lists are defined using square brackets [], while sets are defined using curly braces {}.
# 3. Performance: Sets are generally faster than lists for membership testing and removing duplicates because of their underlying hash table implementation, while lists are better for ordered collections and allow duplicate members.

# Difference between list and dictionary:
# 1. Mutability: Lists are mutable, meaning you can change their content after creation, while dictionaries are also mutable, but they store data in key-value pairs and are unordered.
# 2. Syntax: Lists are defined using square brackets [], while dictionaries are defined using curly braces {} with key-value pairs separated by colons.
# 3. Performance: Dictionaries are generally faster than lists for lookups and inserting new key-value pairs because of their underlying hash table implementation, while lists are better for ordered collections and allow duplicate members.

# Difference between list and array:
# 1. Mutability: Lists are mutable, meaning you can change their content after creation, while arrays are also mutable, but they are more efficient for storing and manipulating large amounts of numerical data because they are implemented in C and have a fixed size.
# 2. Syntax: Lists are defined using square brackets [], while arrays are typically defined using the array module or NumPy library in Python.
# 3. Performance: Arrays are generally faster than lists for numerical operations and memory usage because of their fixed size and efficient memory management, while lists are more flexible and can store different types of data but may have higher overhead for numerical operations.