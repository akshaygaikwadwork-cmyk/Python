# Dictionary
# A dictionary is a collection of key-value pairs, where each key is unique and maps to a specific value. Dictionaries are mutable, meaning you can change their content after creation. They are defined using curly braces {} and consist of key-value pairs separated by colons.
mydict = {"name": "Alice", "age": 30, "city": "New York", "is_student": False, "hobbies": ["reading", "traveling", "coding"], "topic": ("Python", "Data Science")}
print(mydict)
print(type(mydict))  # Output: <class 'dict'>
print(len(mydict))  # Output: 6
# Accessing values in a dictionary
print(mydict["name"])  # Output: Alice
print(mydict.get("age"))  # Output: 30
# Modifying values in a dictionary
mydict["age"] = 31
print(mydict["age"])  # Output: 31
# Adding new key-value pairs to a dictionary
mydict["country"] = "USA"
print(mydict["country"])  # Output: USA
# Removing key-value pairs from a dictionary
del mydict["is_student"]
print(mydict)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York', 'hobbies': ['reading', 'traveling', 'coding'], 'topic': ('Python', 'Data Science'), 'country': 'USA'}
mydict.pop("city")
print(mydict)  # Output: {'name': 'Alice', 'age': 31, 'hobbies': ['reading', 'traveling', 'coding'], 'topic': ('Python', 'Data Science'), 'country': 'USA'}
# Iterating through a dictionary
#1st way
print("Iterating through keys:")
for key in mydict:
    print(key, mydict[key]) # Output: name Alice, age 31, hobbies ['reading', 'traveling', 'coding'], topic ('Python', 'Data Science'), country USA
#2nd way
print("Iterating through key-value pairs:")
for key, value in mydict.items():
    print(key, value) # Output: name Alice, age 31, hobbies ['reading', 'traveling', 'coding'], topic ('Python', 'Data Science'), country USA

#Nested dictionary
nested_dict = {
    "person1": {"name": "Alice", "age": 30}, 
    "person2": {"name": "Bob", "age": 25}
}
print(nested_dict)  # Output: {'person1': {'name': 'Alice', 'age': 30}, 'person2': {'name': 'Bob', 'age': 25}}
print(nested_dict["person1"]["name"])  # Output: Alice
print(nested_dict["person2"]["age"])  # Output: 25

for person, details in nested_dict.items():
    print(f"{person}: {details}") # Output: person1: {'name': 'Alice', 'age': 30}, person2: {'name': 'Bob', 'age': 25}

# Dictionary methods
# Keys, values, and items
# The keys() method returns a view object that displays a list of all the keys in the dictionary. 
# The values() method returns a view object that displays a list of all the values in the dictionary. 
# The items() method returns a view object that displays a list of key-value pairs in the dictionary as tuples.
# The update() method is used to add key-value pairs from another dictionary or an iterable of key-value pairs to the existing dictionary. The clear() method removes all items from the dictionary, leaving it empty.
# The get() method is used to retrieve the value associated with a specified key. If the key is not found in the dictionary, it returns a default value (which can be specified as a second argument) instead of raising a KeyError.


mydict = {"name": "Alice", "age": 30, "city": "New York"}
print(f"Keys: {list(mydict.keys())}")  # Output: Keys: ['name', 'age', 'city']
print(f"Values: {list(mydict.values())}")  # Output: Values: ['Alice', 30, 'New York']
print(f"Items: {list(mydict.items())}")  # Output: Items: [('name', 'Alice'), ('age', 30), ('city', 'New York')]
mydict.update({"country": "USA", "name": "Bob"})  # Updates the dictionary with new key-value pairs and updates the value of 'name' to 'Bob'
print(f"mydict: {mydict}")  # Output: {'name': 'Bob', 'age': 30, 'city': 'New York', 'country': 'USA'}
mydict.clear()
print(f"mydict: {mydict}")  # Output: {}

#length of dictionary
mydict = {"name": "Alice", "age": 30, "city": "New York"}
print(f"Length of mydict: {len(mydict)}")  # Output: Length of mydict: 3

print(f"Keys: {list(mydict.keys())}")  # Output: Keys: ['name', 'age', 'city']
print(f"Values: {list(mydict.values())}")  # Output: Values: ['Alice', 30, 'New York']
print(f"Items: {list(mydict.items())}")  # Output: Items: [('name', 'Alice'), ('age', 30), ('city', 'New York')]

print(f"Length of keys: {len(list(mydict.keys()))}")  # Output: Length of keys: 3
print(f"Length of values: {len(list(mydict.values()))}")  # Output: Length of values: 3

print(mydict.get("name"))  # Output: Alice
print(f"Country: {mydict.get("country", "Not Found")}")  # Output: Country: Not Found



# Difference between dictionary and string:
# 1. Mutability: Dictionaries are mutable, meaning you can change their content after creation, while strings are immutable, meaning once they are created, their content cannot be changed.
# 2. Syntax: Dictionaries are defined using curly braces {} and consist of key-value pairs  , while strings are defined using quotes ('' or "") and consist of a sequence of characters.
# 3. Performance: Dictionaries are generally faster than strings for lookups and storing data in key-value pairs, while strings are better for representing text and allow for various string operations and methods.

# Difference between dictionary and list:
# 1. Mutability: Both dictionaries and lists are mutable, meaning you can change their content after creation, but dictionaries store data in key-value pairs while lists store ordered collections of items.
# 2. Syntax: Dictionaries are defined using curly braces {} and consist of key-value pairs, while lists are defined using square brackets [] and consist of ordered elements.
# 3. Performance: Dictionaries are generally faster than lists for lookups and storing data in key-value pairs, while lists are better for ordered collections and allow duplicate members.

# Difference between dictionary and tuple:
# 1. Mutability: Dictionaries are mutable, meaning you can change their content after creation, while tuples are immutable, meaning once they are created, their content cannot be changed.
# 2. Syntax: Dictionaries are defined using curly braces {} and consist of key-value pairs, while tuples are defined using parentheses () and consist of ordered elements.
# 3. Performance: Dictionaries are generally faster than tuples for lookups and storing data in key-value pairs, while tuples are better for ordered collections and allow duplicate members.

# Difference between dictionary and set:
# 1. Mutability: Both dictionaries and sets are mutable, meaning you can change their content after creation, but dictionaries store data in key-value pairs while sets store only unique values without any particular order.
# 2. Syntax: Dictionaries are defined using curly braces {} and consist of key-value pairs, while sets are defined using curly braces {} and consist of unique values.
# 3. Performance: Dictionaries are generally faster than sets for lookups and storing data in key-value pairs, while sets are better for membership testing and eliminating duplicates.

# Difference between dictionary and array:
# 1. Mutability: Both dictionaries and arrays are mutable, meaning you can change their content after creation.
# 2. Syntax: Dictionaries are defined using curly braces {} and consist of key-value pairs, while arrays are defined using square brackets [] and consist of indexed elements.
# 3. Access: Dictionaries allow access to values using keys, while arrays allow access to elements using indices.