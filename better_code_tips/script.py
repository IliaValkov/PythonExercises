# conditionals 

condition = False 

x = 1 if condition else 0

print(x)
print("\n")
# working with large numbers 

num1 = 10_000_000_000
num2 = 100_000_000 

total = num1 + num2 

print(f"{total:,}")
print("\n")
# using context manager wwhen working with resources 
# like files, threads, data bases
# let resource handling to happen automatically

with open("test.txt", "r") as f:
    file_contents = f.read()

words = file_contents.split(" ")
print(len(words))
print("\n")
# using the enumerate function 

names = ['Ilia', 'Python', 'Tutorial']

for index, name in enumerate(names, start=1): 
    print(index, name)

print("\n")

# loop over two lists at once using zip 
# works as well for more than two list
# zip will stop after the the end of the shortest list

names = ['Ilia', 'Python', 'Tutorial', 'Learn']
names_r = ['Tutorial', 'Learn', 'Ilia', 'Python']

for n1, n2 in zip(names, names_r): 
    print(f"n1: {n1} , n2: {n2}" )

for value in zip(names, names_r): 
    print(value)


print("\n")


# unpacking values 
# use underscore if it is a thorwaway variable
a, _ = (1,2)
print(a)

# a,b,c = (1,2) -> error
# a,b,c = (1,2,3,4,5) -> error but possible 

a, b, *c = (1,2,3,4,5)
print(c)

a, b, *_ = (1,2,3,4,5) # also possible 

a, b, *c, d = (1,2,3,4,5,6,7,8)
print(a)
print(b)
print(c)
print(d)


print("\n")

# setting and getting attributes of classes

class Person():

    pass 

person = Person() 

# dynamic aadding like this: person.first= "Ilia" is possible 

first_key = "first" 
frist_value = "Ilia" 

setattr(person, first_key, frist_value)

first = getattr(person, first_key)

print(first)
print(person.first)

person2 = Person()

person_info = {"first": "John", "last": "Snow"}

for key, value in person_info.items(): 
    setattr(person2, key, value)

for key in person_info.keys(): 
    print(getattr(person2, key))

print("\n")

# inputting secret information 

from getpass import getpass 

username = input("Username: ")
password = getpass("Password: ")

print("Logging in...")

# using -m flag in the terminal
# -m specifies for the module name
# this searches sys.path for the module


# use help() and dir() function on objects and imports
# in order to find out more about what you are using


