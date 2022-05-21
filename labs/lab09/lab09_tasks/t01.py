"""
------------------------------------------------------------------------
CP164 Lab 09, Task 01
------------------------------------------------------------------------
Author: Your Full Name
ID:     190401010
Email:  name1010@mylaurier.ca
__updated__ = "2022-03-18"
------------------------------------------------------------------------
"""
from Food_utilities import get_food
from functions import hash_table


food1 = get_food()

print()
food2 = get_food()

print()
hash_table(4, [food1, food2])
