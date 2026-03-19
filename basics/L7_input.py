#The input() function takes user input from the console and returns it as a string. You can store this input in a variable for further use.
name = input("Enter your name: ")
print("Hello, " + name + "!")

print(type(name), name) # <class 'str'>

age = int(input("Enter your age: "))
print("You are " + str(age) + " years old.")
print(type(age), age) # <class 'int'> 25