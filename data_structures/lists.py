courses = ['History' , 'Math', 'Biology', 'Chemistry']

print("Accessing:")

print(courses)

print(len(courses))

print(courses[0])

print(courses[-1])

print(courses[:2])

print(courses[2:])

print(courses[1:3]) #second index is exclusive

#adding , removing
print("Adding / Removing:")
courses.append('Art')

print(courses)
popped = courses.pop()
print(popped)

courses.insert(0, 'Art')
courses.remove('Art')

print(courses)

courses_2 = ['Physics', 'Music']

courses.insert(0, courses_2)

print(courses)

del courses[0]

courses.extend(courses_2)

print(courses)

#methods 
print("Methods:")

courses.reverse()
print(courses)
courses.reverse()

numbers = [1,5,3,4,2]

# sort sorts the list in-place
courses.sort()
numbers.sort(reverse = True)

print(courses)
print(numbers)

# sorted returns a new list	

sorted_numbers = sorted(numbers)

print(sorted_numbers)

print(min(numbers))
print(max(numbers))
print(sum(numbers))

print(courses.index('Biology'))
print('Art' in courses)

for index, course in enumerate(courses, start=1): 
	print(index, course)

course_str = ', '.join(courses)

print(course_str)

new_list = course_str.split(', ')
print(new_list)





















