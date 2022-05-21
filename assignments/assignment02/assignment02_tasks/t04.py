"""
------------------------------------------------------------------------
CP164 Assignment 02, Task 04
------------------------------------------------------------------------
Author: Your Full Name
ID:     190401010
Email:  name1010@mylaurier.ca
__updated__ = "2022-01-15"
------------------------------------------------------------------------
"""
from Food_utilities import read_foods, food_table

file = open('food.txt', "rt")

foods = read_foods(file)

file.close()

food_table(foods)