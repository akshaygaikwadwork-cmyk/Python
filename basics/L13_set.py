# Set
# A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
myset = {"apple", "banana", "cherry"}
print(myset)
print(type(myset))  # Output: <class 'set'>
print(len(myset))  # Output: 3
#Empty set
empty_set = set()
print(empty_set)  # Output: set()
print(type(empty_set))  # Output: <class 'set'>

# Accessing items in a set
# Note: You cannot access items in a set by index, as sets are unordered.
# Looping through a set
print("Looping through a set: ")
for item in myset:
    print(item)


# Note -
# set is mutable but it's elements must be immutable. This means that you can add or remove elements from a set, but the elements themselves cannot be changed once they are added to the set. For example, you can add a string or a tuple to a set, but you cannot add a list or a dictionary because they are mutable and unhashable.
# We can also use tuple in set but we cannot use list and dictionary in set because they are mutable and unhashable.
# Duplicate values will be ignored in a set, and the order of items is not guaranteed to be the same as the order in which they were added.

myset = {"apple", "banana", "cherry", ("grape", "melon")}
print(myset)  # Output: {'apple', 'banana', 'cherry', ('grape', 'melon')}


# Set methods
# add, remove, discard, pop, clear, update, union, intersection, difference
# The add() method is used to add an element to a set. If the element already
# exists in the set, it will not be added again (sets do not allow duplicate members).
# The remove() method is used to remove an element from a set. If the element is not found in the set, it raises a KeyError.
# The discard() method is used to remove an element from a set. If the element is not found in the set, it does not raise an error.
# The pop() method removes and returns an arbitrary element from the set. If the set is empty, it raises a KeyError.
# The clear() method removes all items from the set, leaving it empty.
# The update() method is used to add multiple elements to a set. It can take an iterable (like a list, tuple, or another set) as an argument and adds all the elements from that iterable to the set.
# The union() method returns a new set that contains all the elements from both sets. It can also be used with the | operator.
# The intersection() method returns a new set that contains only the elements that are common to both sets. It can also be used with the & operator.
# The difference() method returns a new set that contains the elements that are in the first set but not in the second set. It can also be used with the - operator.

# Adding items to a set
print("Adding items to a set: ")
myset.add("orange")
print(myset)  # Output: {'apple', 'banana', 'cherry', 'orange'}
# Removing items from a set
print("Removing items from a set: ")
myset.remove("banana")
print(myset)  # Output: {'apple', 'cherry', 'orange'}
myset.discard("cherry")
print(myset)  # Output: {'apple', 'orange'}
myset.pop()  # Removes and returns an arbitrary element from the set
print(myset)  # Output: {'orange'} (the output may vary since sets are unordered)
# Clearing a set
myset.clear()
print(myset)  # Output: set()
# Updating a set with multiple items
myset.update(["grape", "melon", "kiwi"])
print(myset)  # Output: {'grape', 'melon', 'kiwi'}
# Set operations
set1 = {"apple", "banana", "cherry"}
set2 = {"banana", "cherry", "orange"}
print(f"Union: {set1.union(set2)}")  # Output: Union: {'apple', 'banana', 'cherry', 'orange'}
print(f"Intersection: {set1.intersection(set2)}")  # Output: Intersection: {'banana', 'cherry'}
print(f"Difference: {set1.difference(set2)}")  # Output: Difference: {'apple'}

# Difference between set and string:
# 1. Mutability: Sets are mutable, meaning you can change their content after creation, while strings are immutable, meaning once they are created, their content cannot be changed.
# 2. Syntax: Sets are defined using curly braces {}, while strings are defined using quotes ('' or "").
# 3. Performance: Sets are generally faster than strings for membership testing and eliminating duplicates, while strings are better for representing text and allow for various string operations and methods.

# Difference between set and list:
# 1. Mutability: Both sets and lists are mutable, meaning you can change their content after creation. However, sets do not allow duplicate members and are unordered, while lists allow duplicate members and are ordered.
# 2. Syntax: Sets are defined using curly braces {}, while lists are defined using square brackets [].
# 3. Performance: Sets are generally faster than lists for membership testing and eliminating duplicates, while lists are better for ordered collections and allow duplicate members.

# Difference between set and tuple:
# 1. Mutability: Sets are mutable, meaning you can change their content after creation, while tuples are immutable, meaning once they are created, their content cannot be changed.
# 2. Syntax: Sets are defined using curly braces {}, while tuples are defined using parentheses ().
# 3. Performance: Sets are generally faster than tuples for membership testing and eliminating duplicates, while tuples are better for ordered collections and allow duplicate members. 

# Difference between set and dictionary:
# 1. Mutability: Both sets and dictionaries are mutable, meaning you can change their content after creation, but sets store only unique values without any particular order, while dictionaries store data in key-value pairs and are ordered (as of Python 3.7).
# 2. Syntax: Sets are defined using curly braces {} and consist of unique values, while dictionaries are defined using curly braces {} and consist of key-value pairs.
# 3. Performance: Sets are generally faster than dictionaries for membership testing and eliminating duplicates, while dictionaries are better for lookups and storing data in key-value pairs.

# Difference between set and array:
# 1. Mutability: Both sets and arrays are mutable, meaning you can change their content after creation, but sets do not allow duplicate members and are unordered, while arrays are ordered collections of items that can contain duplicates.
# 2. Syntax: Sets are defined using curly braces {}, while arrays are defined using the array module and require importing the array module.
# 3. Performance: Sets are generally faster than arrays for membership testing and eliminating duplicates, while arrays are more efficient than sets for numerical operations and storing large amounts of data because they are implemented in C and have a fixed size, while sets are more flexible and can store different types of data but may be less efficient for numerical operations.
