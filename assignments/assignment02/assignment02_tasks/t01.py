"""
------------------------------------------------------------------------
CP164 Assignment 02, Task 01
------------------------------------------------------------------------
Author: Your Full Name
ID:     190401010
Email:  name1010@mylaurier.ca
__updated__ = "2022-01-15"
------------------------------------------------------------------------
"""
from Food import Food
from Food_utilities import read_foods, by_origin

file = open('food.txt', "rt")

foods = read_foods(file)

file.close()

origin = int(input(f"Enter a origin as an int\n{Food.origins()}: "))

origins = by_origin(foods, origin)

for food in origins:
    print(food, end="\n\n")
