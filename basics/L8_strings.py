str1 = "This is a string"
str2 = 'This is also a string'
# Both str1 and str2 are valid string literals in Python. You can use either single quotes or double quotes to define a string.
# If you want to include a single quote within a string, you can use double quotes to define the string:
str3 = "It's a nice day!"
# If you want to include a double quote within a string, you can use single quotes to define the string:
str4 = 'She said, "Hello!"'
str5 = "She said, 'Hello'"  # Using double quotes to include a single quote without escaping
str6 = 'It\'s a nice day!'  # Using single quotes and escaping the single quote
# Alternatively, you can use escape characters to include quotes within a string:
str7 = "She said, \"Hello!\""  # Using backslash to escape the double quote

print(str1)
print(str2)
print(str3)
print(str4)
print(str5)
print(str6)
print(str7)

#Escape characters : /n for new line, /t for tab, /' for single quote, /" for double quote, / for backslash

#New line character
print("Escape characters:")
str8 = "Hello\nWorld"
print(str8)

#Concatenation of strings
print("Concatenation of strings:")
str9 = "Hello"
str10 = "World"
str11 = str9 + " " + str10  # Concatenating str9 and str10 with a space in between
print(str11)

#Length of a string
print("Length of a string:")
str12 = "Hello World"
length_of_str12 = len(str12)  # Using the len() function to get the length of str12
print("The length of the string is:", length_of_str12)

#String indexing
print("String indexing:")
str13 = "Hello"
print("The first character of str13 is:", str13[0])  # Accessing the first character of str13
print("The last character of str13 is:", str13[-1])  # Accessing the last character of str13 using negative indexing


#String slicing
print("String slicing:")
str14 = "Hello World"
print("The first 5 characters of str14 are:", str14[0:5])  # Slicing the first 5 characters of str14 (from index 0 to index 4)
print("The last 5 characters of str14 are:", str14[-5:])  # Slicing the last 5 characters of str14 (from index -5 to the end of the string)

#String methods/functions
print("String methods/functions:")
str15 = "hello world"
print("Uppercase version of str15:", str15.upper())  # Using the upper() method to convert str15 to uppercase
print("Lowercase version of str15:", str15.lower())  # Using the lower() method to convert str15 to lowercase
print("Title case version of str15:", str15.title())  # Using the title() method to convert str15 to title case
print("Number of occurrences of 'o' in str15:", str15.count('o'))  # Using the count() method to count the number of occurrences of 'o' in str15
endwith_o = str15.endswith('o')  # Using the endswith() method to check if str15 ends with 'o'
print("Does str15 end with 'o'?", endwith_o)
capitalize_str15 = str15.capitalize()  # Using the capitalize() method to capitalize the first character of str15
print("Capitalized version of str15:", capitalize_str15)
replace_str15 = str15.replace('o', '0')  # Using the replace() method to replace 'o' with '0' in str15
print("str15 after replacing 'o' with '0':", replace_str15)
find_index = str15.find('world')  # Using the find() method to find the index of the substring 'world' in str15
print("Index of 'world' in str15:", find_index)  # Using the find() method to find the index of the substring 'world' in str15

#String immutability - Strings in Python are immutable, which means that once a string is created, it cannot be changed. When you try to modify a string, a new string is created instead.
strCheck =" hey there"
print(id(strCheck))
strCheck = "Youare welcome"
print(id(strCheck))  # The id of strCheck will be different after reassignment, indicating that a new string object has been created.