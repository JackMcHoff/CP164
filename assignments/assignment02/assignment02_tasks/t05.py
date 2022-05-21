"""
------------------------------------------------------------------------
CP164 Assignment 02, Task 05
------------------------------------------------------------------------
Author: Your Full Name
ID:     190401010
Email:  name1010@mylaurier.ca
__updated__ = "2022-01-15"
------------------------------------------------------------------------
"""
from Food_utilities import read_foods, food_table, food_search

file = open('food.txt', "rt")

foods = read_foods(file)

file.close()

result = food_search(foods, 11, 0, False)

food_table(result)
