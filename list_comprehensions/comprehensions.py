nums = [1,2,3,4,5,6,7,8,9,10]

# I want n for n in nums
my_list = [] 

# for n in nums:
#     my_list.append(n)

my_list = [n for n in nums]

print(my_list)

# I want n*n for n in nums
my_list = []

# for n in nums: 
#     my_list.append(n*n)

my_list = [n*n for n in nums]

print(my_list)

#using map and lamda
my_list = [] 

my_list = map(lambda n: n*n, nums)

print(list(my_list))

# I want n for each n in nums if n is even
my_list = [] 

# for n in nums:
#     if n % 2 == 0: 
#         my_list.append(n)

my_list = [n for n in nums if n%2==0]

print(my_list)


#using filter and lamda
my_list = [] 

my_list = filter(lambda n: n%2==0, nums)

print(list(my_list))

# I want a (letter, num) pair for each letter in abcd and each number in 0123
my_list = [] 

# for letter in 'abcd': 
#     for num in '0123':
#         my_list.append((letter,num))

my_list = [(letter, num) for letter in 'abcd' for num in range(4)]

print(my_list)

#Dictionary Comprehensions 

names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heroes = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

#I want a dict{'name': 'hero'} for each name hero pair in zip(names, heroes)

# for n,h in zip(names, heroes): 
#     my_dict[n] = h

my_dict = {name: hero for name, hero in zip(names, heroes)}
print(my_dict)

#If name not equal to Peter
my_dict = {}
my_dict = {name: hero for name, hero in zip(names, heroes) if name != 'Peter'}
print(my_dict)

# Set comprehensions 

nums = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,3,4,5,6]

my_set = set() 

# for n in nums: 
#     my_set.add(n)

my_set = {n for n in nums}

print(my_set)

# Generator Expressions
# I want to yield 'n*n' for n in nums 

nums = [1,2,3,4,5,6,7,8,9,10]

# def gen_func(nums):
#     for n in nums: 
#         yield n*n

# my_gen = gen_func(nums)

my_gen = (n*n for n in nums)

for i in my_gen: 
    print(i)
