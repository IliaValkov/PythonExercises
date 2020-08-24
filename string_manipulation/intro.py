message = "Hello world!"

print(message)

print(len(message))

#slicing
print(message[0])

print(message[0:5]) #second index is exclusive

print(message[:5])

print(message[6:])

#methods

print(message.lower())

print(message.upper())

print(message.count('Hello'))

print(message.count('l'))

print(message.find('world'))

new_message = message.replace('world' , 'universe') #returns a new string
print(new_message)

greeting = "Hello" 

name = "Ilia"

greeting_message = greeting + ", " + name + ". Welcome!" 

formated_message = '{}, {}. Welcome!'.format(greeting, name)

f_string_message = f'{greeting}, {name}. Welcome!'

print(greeting_message)

print(formated_message)

print(f_string_message) 

#using the dir function -> shows available  methods
print(dir(name))

#using help function -> gives method description
print(help(str.lower))