num = 10
num2 = 5

#Arithmetic Operators : + (Addition), - (Subtraction), * (Multiplication), / (Division), % (Modulus), ** (Exponentiation)
print("Arithmetic Operators:")
sum = num + num2
difference = num - num2
product = num * num2
quotient = num / num2
remainder = num % num2
power = num ** num2

print("Sum:", sum) #15
print("Difference:", difference) #5
print("Product:", product) #50
print("Quotient:", quotient) #2.0
print("Remainder:", remainder) #0
print("Power:", power) #100000

#Relational Operators/Comparison Operators : > (Greater than), < (Less than), == (Equal to), != (Not equal to), >= (Greater than or equal to), <= (Less than or equal to)
print("Relational Operators:")
print("num > num2:", num > num2) #True
print("num < num2:", num < num2) #False
print("num == num2:", num == num2) #False
print("num != num2:", num != num2) #True
print("num >= num2:", num >= num2) #True
print("num <= num2:", num <= num2) #False

#Assignment Operators : = (Assignment), += (Add and assign), -= (Subtract and assign), *= (Multiply and assign), /= (Divide and assign), %= (Modulus and assign), **= (Exponentiation and assign)
print("Assignment Operators:")
num += num2 # num = num + num2
print("num:", num) #15
num -= num2 # num = num - num2
print("num:", num) #10
num *= num2 # num = num * num2
print("num:", num) #50
num /= num2 # num = num / num2
print("num:", num) #10.0
num %= num2 # num = num % num2
print("num:", num) #0
num **= num2 # num = num ** num2
print("num:", num) #0


#Logical Operators : and, or, not
print("Logical Operators:")
is_adult = True
has_id = False
print("is_adult and has_id:", is_adult and has_id) #False
print("is_adult or has_id:", is_adult or has_id) #True
print("not is_adult:", not is_adult) #False

print("Now num is:", num) #0
print("Now num2 is:", num2) #5

print("not(num > num2 and is_adult):", not(num > num2 and is_adult)) #True

print("And operator:", num > num2 and is_adult) #False
print("Or operator:", num > num2 or is_adult) #True