"""
------------------------------------------------------------------------
CP164 Lab 06, Task 03
------------------------------------------------------------------------
Author: Your Full Name
ID:     190401010
Email:  name1010@mylaurier.ca
__updated__ = "2022-02-25"
------------------------------------------------------------------------
"""
from Food_utilities import read_foods
from List_linked import List


file_variable = open("food.txt", "rt")

foods = read_foods(file_variable)

file_variable.close()

new_list = List()

for value in foods:
    new_list.append(value)

print(new_list.count(foods[5]))

print()
print(new_list.max())

print()
print(new_list.min())
