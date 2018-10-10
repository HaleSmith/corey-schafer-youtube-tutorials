# References https://www.youtube.com/watch?v=CqvZ3vGoGs0
# Importing runs all the code in the imported file

import my_module  # In same directory as importing module

courses = ['History', 'Math', 'Physics', 'CompSci']

index = my_module.find_index(courses, 'Physics')
print(index)
print(my_module.find_index(courses, 'Art'))


import my_module as mm  # Can use shorter name for brevity
print(mm.find_index(courses, 'Physics'))

# Can import just a function
# Can import multiple functions
from my_module import find_index as f_i, test
print(f_i(courses, 'Physics'))
print(test)

# Could import everything, but then hard to track
# If use import my_module, then use my_module.find_index
from my_module import *

import sys
print(sys.path)  # Where python looks for code to import


# Adds a folder in which to search for a module
# PyCharm path variables may need to be set differently
# sys.path is a list and can be appended
sys.path.append("C:/Users/kahna/PycharmProjects/"
                "corey-schafer-youtube-tutorials/beginner_intro/my-modules")
import my_module_new_dir as mmnd
print(mmnd.find_index(courses, 'Physics'))

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
print(os.getcwd())  # Like print working directory
# Shows where in the hard drive os.py is located
print(os.__file__)  # "dunder" = double underscore

import antigravity

