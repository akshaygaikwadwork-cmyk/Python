# Tuples
# A tuple is a collection which is ordered and immutable i.e. unchangeable. In Python tuples are written with round brackets. 
mytuple = ("apple", "banana", "cherry")
print(mytuple)
print(type(mytuple))  # Output: <class 'tuple'>
print(len(mytuple))  # Output: 3
# Accessing items
print("Accessing items: ")
print(mytuple[0])  # Output: apple
print(mytuple[1])  # Output: banana
print(mytuple[2])  # Output: cherry
# Note: You cannot change values in a tuple.
# Looping through a tuple
print("Looping through a tuple: ")
for item in mytuple:
    print(item)
#slicing a tuple
print("Slicing a tuple: ")
print(mytuple[0:2])  # Output: ('apple', 'banana') - Slicing the first two items of the tuple (from index 0 to index 1)
print(mytuple[1:])  # Output: ('banana', 'cherry') - Slicing from index 1 to the end of the tuple
# Creating a tuple with one item (note the comma)
mytuple = ("apple",)
print(mytuple)
print(type(mytuple))  # Output: <class 'tuple'>
# Creating a tuple without parentheses
mytuple = "apple", "banana", "cherry", "apple"
print(mytuple)
print(type(mytuple))  # Output: <class 'tuple'>
# Tuple methods
print("Tuple methods: ")
print(mytuple.count("apple"))  # Output: 2
print(mytuple.index("banana"))  # Output: 1

# Difference between list and string:
# 1. Mutability: Lists are mutable, meaning you can change their content after creation, while strings are immutable, meaning once they are created, their content cannot be changed.
# 2. Syntax: Lists are defined using square brackets [], while strings are defined using quotes
# 3. Performance: Strings are generally faster than lists because of their immutability, which allows for certain optimizations in memory and performance.

# Difference between list and tuple:
# 1. Mutability: Lists are mutable, meaning you can change their content after creation, while tuples are immutable, meaning once they are created, their content cannot be changed.
# 2. Syntax: Lists are defined using square brackets [], while tuples are defined using parentheses
# 3. Performance: Tuples are generally faster than lists because of their immutability, which allows for certain optimizations in memory and performance.

# Difference between list and set:
# 1. Mutability: Lists are mutable, meaning you can change their content after creation, while sets are also mutable but they do not allow duplicate members and are unordered.
# 2. Syntax: Lists are defined using square brackets [], while sets are defined using curly braces {}
# 3. Performance: Sets are generally faster than lists for membership testing and eliminating duplicates.

# Difference between list and dictionary:
# 1. Mutability: Both lists and dictionaries are mutable, meaning you can change their content after creation.
# 2. Syntax: Lists are defined using square brackets [], while dictionaries are defined using curly braces {} and consist of key-value pairs.
# 3. Performance: Dictionaries are generally faster than lists for lookups and storing data in key-value pairs, while lists are better for ordered collections and allow duplicate members.

# Difference between list and array:
# 1. Mutability: Both lists and arrays are mutable, meaning you can change their content after creation.
# 2. Syntax: Lists are defined using square brackets [], while arrays are defined using the array module and require importing the array module.
# 3. Performance: Arrays are generally more efficient than lists for numerical operations and storing large amounts of data because they are implemented in C and have a fixed size, while lists are more flexible and can store different types of data but may be less efficient for numerical operations.