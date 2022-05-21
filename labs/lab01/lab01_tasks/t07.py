"""
------------------------------------------------------------------------
CP164 Lab 01, Task 07
------------------------------------------------------------------------
Author: Your Full Name
ID:     190401010
Email:  name1010@mylaurier.ca
__updated__ = "2022-01-15"
------------------------------------------------------------------------
"""
from Food_utilities import read_foods, get_vegetarian

file = open('food.txt', "rt")

foods = read_foods(file)

file.close()

veggies = get_vegetarian(foods)

for food in veggies:
    print(food, end="\n\n")
