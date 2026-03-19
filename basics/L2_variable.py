name = "Akshay"
name += ' Gaikwad'
name += """ Senior Software Engineer"""
name += ''' at Microsoft'''
print("my name is", name)
age = 25
age += -1
print("my age is", age)
gender = "Male"
print("my gender is", gender)
price = 20.43
print("the price is",price)
is_adult = True
print("is adult?", is_adult)
newType = None
print("new type is", newType)


print(type(name))
print(type(age))
print(type(gender))
print(type(price))
print(type(is_adult))
print(type(newType))

#Case sensitivity
# variable name is case sensitive
name1 = "Akshay"
Name1 = "Akshay Gaikwad"
print(name1)
print(Name1)


#Reserved keywords
# you cannot use these keywords as variable names.

# False      await      else       import     pass
# None       break      except     in         raise
# True       class      finally    is         return
# and        continue   for        lambda     try
# as         def        from       nonlocal   while
# assert     del        global     not        with
# async       elif       if         or         yield