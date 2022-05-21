"""
------------------------------------------------------------------------
CP164 Lab 10, Task 04
------------------------------------------------------------------------
Author: Your Full Name
ID:     190401010
Email:  name1010@mylaurier.ca
__updated__ = "2022-03-22"
------------------------------------------------------------------------
"""
from test_Sorts_List_linked import SORTS, test_sort

# IMPORTANT!!!! for this task to work you need to download the assignment 07 solution
# And write the clear method for the linked list
# Thanks to @cgram_00 from discord for the help

print(
    f"n:   100       |      Comparisons       | |         Swaps          |")
print("Algorithm      In Order Reversed   Random In Order Reversed   Random")
print("-------------- -------- -------- -------- -------- -------- --------")

for values in SORTS:
    test_sort(values[0], values[1])
