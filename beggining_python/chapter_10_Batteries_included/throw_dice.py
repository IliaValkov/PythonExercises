from random import randrange 

num = input("How many dice? ")
sides = input("How many sides per dice? ")

s = 0

for i in range(int(num)): s +=randrange(int(sides))+1

print("The result is : " ,s)

