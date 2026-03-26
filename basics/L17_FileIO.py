# File I/O
# File I/O stands for File Input/Output, which refers to the process of reading from and writing to files in a programming language. In Python, you can use built-in functions to perform file I/O operations.
# To work with files in Python, you can use the open() function to open a file, and then use methods like read(), readline(), or write() to read from or write to the file. Finally, you should close the file using the close() method to free up system resources.
# Syntax for opening a file
# file_object = open(file_name, mode)
# - file_name: The name of the file you want to open (including the path if it's not in the current directory).
# - mode: The mode in which you want to open the file. Common modes include:
#   - 'r': Read mode (default) - Opens the file for reading.
#   - 'w': Write mode - Opens the file for writing (creates a new file or truncates an existing file).
#   - 'a': Append mode - Opens the file for writing (creates a new file or appends to an existing file).
#   - 'b': Binary mode - Opens the file in binary mode (used for non-text files).
# Example of writing to a file
file = open('example.txt', 'w')  # Open a file for writing
file.write('Hello, World!\n')  # Write a line to the file
file.write('This is a file I/O example.\n')  # Write another line to the file
file.close()  # Close the file to free up system resources
# Example of reading from a file
file = open('example.txt', 'r')  # Open the file for reading    
content = file.read()  # Read the entire file
print(content)  # Print the content
file.close()  # Close the file to free up system resources
# Example of reading a file line by line
file = open('example.txt', 'r')  # Open the file for reading    
for line in file:
    print(line)  # Print each line
file.close()  # Close the file to free up system resources
# Example of appending to a file
file = open('example.txt', 'a')  # Open the file for appending  
file.write('This is a line appended to the file.\n')  # Append a line to the file
file.close()  # Close the file to free up system resources
# Using with statement for file I/O (automatically closes the file)
with open('example.txt', 'r') as file:  # Open the file for reading
    content = file.read()  # Read the entire file
    print(content)  # Print the content
with open('example.txt', 'a') as file:  # Open the file for appending
    file.write('This is another line appended to the file.\n')  # Append a line to the file

# Types of files
# - Text files: These files contain human-readable characters and are typically used for storing data in a structured format (e.g., .txt, .csv, .json, .docs, .log etc.).
# - Binary files: These files contain data in a format that is not human-readable and are typically used for storing data in a compact format (e.g., .jpg, .png, .pdf, .mp4 etc.).

# Character             Meaning
# 'r'                 Read mode (default) - Opens the file for reading.
# 'w'                 Write mode - Opens the file for writing (creates a new file or truncates an existing file).
# 'a'                 Append mode - Opens the file for writing (creates a new file or appends to an existing file).
# 'b'                 Binary mode - Opens the file in binary mode (used for non-text files).
# 'x'                 Exclusive creation - Opens the file for exclusive creation (fails if the file already exists).
# 't'                 Text mode (default) - Opens the file in text mode (used for text files).
# '+'                 Update mode - Opens the file for updating (reading and writing).

# Methods for file objects
# - read(size): Reads a specified number of bytes from the file. If size is not provided, it reads the entire file.
# - readline(): Reads a single line from the file.
# - readlines(): Reads all lines from the file and returns them as a list.
# - write(string): Writes a string to the file.
# - writelines(list): Writes a list of strings to the file.
# - close(): Closes the file to free up system resources.
