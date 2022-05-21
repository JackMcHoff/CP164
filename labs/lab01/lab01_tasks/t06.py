"""
------------------------------------------------------------------------
CP164 Lab 01, Task 06
------------------------------------------------------------------------
Author: Your Full Name
ID:     190401010
Email:  name1010@mylaurier.ca
__updated__ = "2022-01-15"
------------------------------------------------------------------------
"""
from Food_utilities import read_food, write_foods

gulab_jamun = read_food('Gulab Jamun|2|True|300')

spanakopita = read_food('Spanakopita|5|True|260')

file = open("new_foods.txt", "wt")

write_foods(file, [gulab_jamun, spanakopita])

file.close()
