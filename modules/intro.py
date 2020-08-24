# import my_module as mm
# from my_module import * -> not a good aproach
import sys
sys.path.append('/home/iliav/pyhton_tutorial_module')

from my_module import find_index

courses = ['Math', 'History', 'Biology', 'CompSci']

index = find_index(courses, 'History')
print(index)

print(sys.path)

import random 

random_course = random.choice(courses)
print(random_course)

import math 

rads = math.radians(90)
print(rads) 
print(math.sin(rads)) 

import datetime 
import calendar 

today = datetime.date.today() 

print(today) 
print(calendar.isleap(2020))

import os

print(os.getcwd()) 

import antigravity