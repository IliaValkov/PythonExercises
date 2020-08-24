
def pass_func():
	pass

def hello_fun():
	print("Hello function!")

def hello_fun1():
	return "Hello function1!"

def custom_hello_fun(greeting, name='you'):
	return f"{greeting}, {name}!"

def student_info(*args, **kwargs): 
	print(args)
	print(kwargs)

print(hello_fun)

hello_fun()

print(hello_fun1())

print(hello_fun1().upper())

print(custom_hello_fun('Hi'))

print(custom_hello_fun('Hi', 'Ilia'))

# args and kwargs

student_info('Math','Art', name='John', age=22)

courses = ['Chemistry','Math']
info = {'name': 'Johnatan', 'age': 24} 

student_info(*courses,**info)
