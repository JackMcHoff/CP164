"""
------------------------------------------------------------------------
CP164 Lab 02, Task 05
------------------------------------------------------------------------
Author: Your Full Name
ID:     190401010
Email:  name1010@mylaurier.ca
__updated__ = "2022-01-21"
------------------------------------------------------------------------
"""
from Food_utilities import read_foods
from utilities import stack_test

file = open('food.txt', "rt")

foods = read_foods(file)

file.close()

stack_test(foods)
