# Comparisons
# == 
# != 
# >
# <
# >=
# <=
# is -> Object identity
# 
if True: 
	print('Conditional was true.')

if False: 
	print('Conditional was true.')
else: 
	print('Conditional was false.')

language = 'Java'

if language == 'Python':
	print('Language is Python')
elif: 
	print('Language is Java')
else: 
	print('No match')	

# there is not switch statement in Python 

# Boolean operations - and / or / not

user = 'Admin' 
logged_in = False

if user == 'Admin' and logged_in: 
	print('Admin Page')
else: 
	print('Bad Creds')

if user == 'Admin' or logged_in: 
	print('Admin Page')
else: 
	print('Bad Creds')

if not logged_in: 
	print('Please log in')
else: 
	print('Welcomell')

a = [1,2,3]
b = [1,2,3]
c = a

print(a==b)

print(id(a))
print(id(b))
print(id(c))

print(a is b)
print(a is c)

# False Value: 
	# False 
	# None
	# Zero of any numeric type 
	# An empty sequence. For example, '' ,() , []
	# An empty mapping. For example, {}

















