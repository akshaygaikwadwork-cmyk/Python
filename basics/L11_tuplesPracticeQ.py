#Q.1. Write a program to ask the user to enter name of their 3 favorite movies and stored them in a tuple and print the tuple.
# Ans:

# 1st way
favorite_movies = ()  # Initializing an empty tuple to store the favorite movies
for i in range(3):
    movie = input("Enter the name of your favorite movie: ")
    favorite_movies += (movie,)  # Adding the movie to the tuple

print("Your favorite movies are: ", favorite_movies)


# 2nd way
favorite_movies = tuple(input("Enter the name of your favorite movie: ") for _ in range(3))
print("Your favorite movies are: ", favorite_movies)


#Q.2. Write a program to check if a tuple contains a palindrome of elements.
# Ans:

# 1st way
tupleCheck = (121, 2, "abc", "def", 23, "bab", "aba")
for item in tupleCheck:
    original = str(item)
    check = ""

    for char in original:
        check = char + check

    if check == original:
        print(check, "is a palindrome")


# 2nd way
tupleCheck = (121, 2, "abc", "def", 23, "bab", "aba")
for item in tupleCheck:
    if str(item) == str(item)[::-1]:
        print(item, "is a palindrome")


#Q.3. Write a program to check if a tuple of reversed elements is same as original tuple or not.
# Ans:

# 1st way
tuple1 = (1, 2, 1)
tupleCopy = tuple1[::-1]

if tuple1 == tupleCopy:
    print("The tuple is a palindrome.")
else:
    print("The tuple is not a palindrome.")


# 2nd way
tuple1 = (1, 2, 1)
if tuple1 == tuple1[::-1]:
    print("The tuple is a palindrome.")
else:
    print("The tuple is not a palindrome.")


#Q.4. Write a program the number of students with the "A" grade in a tuple of grades.
# Ans:

# 1st way
grades = ("A", "B", "C", "A", "D", "A", "B")
count_A = grades.count("A")
print("Number of students with grade A:", count_A)


# 2nd way
grades = ("A", "B", "C", "A", "D", "A", "B")
count_A = 0
for grade in grades:
    if grade == "A":
        count_A += 1
print("Number of students with grade A:", count_A)


#Q.5. Write a program to store the above grades in a tuple and sort them in ascending order.
# Ans:

grades = ("A", "B", "C", "A", "D", "A", "B")
sorted_grades = tuple(sorted(grades))
print("Sorted grades:", sorted_grades)