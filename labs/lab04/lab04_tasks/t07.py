"""
------------------------------------------------------------------------
CP164 Lab 04, Task 07
------------------------------------------------------------------------
Author: Your Full Name
ID:     190401010
Email:  name1010@mylaurier.ca
__updated__ = "2022-02-04"
------------------------------------------------------------------------
"""
from Food_utilities import read_foods
from utilities import list_test

file = open("food.txt", "rt")

source = read_foods(file)

file.close()

list_test(source)
