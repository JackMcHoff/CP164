"""
------------------------------------------------------------------------
CP164 Assignment 02, Task 03
------------------------------------------------------------------------
Author: Your Full Name
ID:     190401010
Email:  name1010@mylaurier.ca
__updated__ = "2022-01-15"
------------------------------------------------------------------------
"""
from Food_utilities import read_foods, calories_by_origin

file = open('food.txt', "rt")

foods = read_foods(file)

file.close()

avg = calories_by_origin(foods, 2)

print(f"Average Calories: {avg}")
