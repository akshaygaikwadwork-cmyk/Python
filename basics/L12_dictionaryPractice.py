# Q.1. Store following word meanings in a pythton dictionary and print them:
#table : "a piece of furniture", "list of facts & figures"
#cat : "a small animal"

#Ans:
mydict = {
    "table": ["a piece of furniture", "list of facts & figures"],
    "cat": "a small animal"
}
print(mydict)  # Output: {'table': ['a piece of furniture', 'list of facts & figures'], 'cat': 'a small animal'}


# Q.2. You are given a list of subjects for students. Assume one classroom is reuired for 1 subject. How many classrooms are needed by all students.
# "python", "java", "c++", "python", "javascript", "java", "python", "java", "c++", "c"

#Ans:
subjects = ["python", "java", "c++", "python", "javascript", "java", "python", "java", "c++", "c"]
unique_subjects = set(subjects)  # Using a set to get unique subjects
classrooms_needed = len(unique_subjects)  # Count the unique subjects
print(f"Classrooms needed: {classrooms_needed}")  # Output: Classrooms needed: 5

# Q.3. Write a program to enter marks of 3 subjexts from the user and store them in a dictionary. Start with an empty dictionary & add one by one. User subject name as ket & marks as value.
#Ans:
marks_dict = {}
for i in range(3):  
    subject = input("Enter subject name: ")  # Get subject name from user
    marks = float(input("Enter marks for the subject: "))  # Get marks for the subject from user
    marks_dict[subject] = marks  # Add the subject and marks to the dictionary  
print("Marks dictionary:", marks_dict)  # Output: Marks dictionary: {'subject1': marks1, 'subject2': marks2, 'subject3': marks3}

# Q.4. Figure out a way to store 9 & 9.0 as separate values in the set.
#Ans:
my_set = {9, 9.0}  # Both 9 and 9.0 are considered the same in a set, so only one will be stored
print(my_set)  # Output: {9} - Only one of the values will be stored in the set because 9 and 9.0 are considered equal in Python. To store them as separate values, we can use a list instead of a set:
my_list = [9, 9.0]  # Using a list to store both values separately
print(my_list)  # Output: [9, 9.0] - Both values are stored separately in the list.
my_set = {9, "9.0"}  # Using a set to store both values separately
print(my_set)  # Output: {9, "9.0"} - Both values are stored separately in the set.
my_set = {
    "float_9.0": 9.0,
    "int_9": 9
}
print(my_set)  # Output: {'float_9.0': 9.0, 'int_9': 9} - Both values are stored separately in the set using different keys.
