student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

print(student)

print(student['name'])

print(student['phone']) # -> error

print(student.get('name'))

print(student.get('phone')) # -> None

print(student.get('phone', 'Not found')) # -> second argumet is default return type, in case of a non-existing key

# Updating and adding keys
student['phone'] = '555-5555'

print(student.get('phone'))

student['name'] = 'Jane'

print(student.get('name'))

student.update({'name': 'Jane' , 'age': 28, 'courses': ['Biology', 'CompSci']})

print(student)

# Deleting

name = student.pop('name')

print(name)
student['name'] = 'John'

del student['age']

print(student)

# Looping through 

	#accesing key and values

print(len(student))

print(student.keys())

print(student.values())

print(student.items())

	# looping

for key in student: 
	pass # -> loops only through the key 

for key, value in student.items():
	print(key, value)