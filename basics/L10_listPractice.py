#Q.1. Write a program to ask the user to enter name of their 3 favorite movies and stored them in a list and print the list.
# Ans:
# 1st way
favorite_movies = []
for i in range(3):
    movie = input("Enter the name of your favorite movie: ")
    favorite_movies.append(movie)
print("Your favorite movies are: ", favorite_movies)

# 2nd way
favorite_movies = [input("Enter the name of your favorite movie: ") for _ in range(3)]
print("Your favorite movies are: ", favorite_movies)


#Q.2. Write a program to check if a list contains a palindrome of elements.
# Ans:
# 1st way
listCheck = [121, 2, "abc", "def", 23, "bab", "aba"]
for item in listCheck:
    original = str(item)
    check = ""

    for char in original:
        check = char + check

    if check == original:
        print(check, "is a palindrome")

# 2nd way
listCheck = [121, 2, "abc", "def", 23, "bab", "aba"]
for item in listCheck:
    if str(item) == str(item)[::-1]:  # Checking if the item is equal to its reverse
        print(item, "is a palindrome")


#Q.3. Write a program to check if a list of reversed elements is same as original list or not. i.e [1,2,3] and [3,2,1] are same but [1,2,3] and [1,2,3] are not same.
# Palindrome list
# Ans:
#1st way
list1 = [1, 2, 1]
listCopy = list1.copy()  # Creating a copy of list1 to reverse it without modifying the original list
listCopy.reverse()  # Reversing the copy of list1
if list1 == listCopy:
    print("The list is a palindrome.")
else:
    print("The list is not a palindrome.")

#2nd way
list1 = [1, 2, 1]
if list1 == list1[::-1]:  # Checking if the list is equal to its reverse
    print("The list is a palindrome.")
else:
    print("The list is not a palindrome.")


#Q.4. Write a program the number of students with the "A" grade in a list of grades.
# Ans:
#1st way
grades = ["A", "B", "C", "A", "D", "A", "B"]
count_A = grades.count("A")  # Using the count() method to count the number of occurrences of "A" in the grades list
print("Number of students with grade A:", count_A)

#2nd way
grades = ["A", "B", "C", "A", "D", "A", "B"]
count_A = 0
for grade in grades:
    if grade == "A":
        count_A += 1  # Incrementing the count_A variable for each occurrence of "A"
print("Number of students with grade A:", count_A)

#Q.5. Write a program to store the above grades in a list and sort the list in ascending order and print the sorted list.
# Ans:
grades = ["A", "B", "C", "A", "D", "A", "B"]
grades.sort()  # Sorting the list in ascending order
print("Sorted grades:", grades)