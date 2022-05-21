"""
------------------------------------------------------------------------
CP164 Lab 04, Task 06
------------------------------------------------------------------------
Author: Your Full Name
ID:     190401010
Email:  name1010@mylaurier.ca
__updated__ = "2022-02-04"
------------------------------------------------------------------------
"""
from List_array import List
from utilities import array_to_list, list_to_array

llist = List()

source = [1, 2, 3, 4, 5]

array_to_list(llist, source)

print("Printing LList: ")
for value in llist:
    print(value)

list_to_array(llist, source)

print()
print("Printing List: ")
for value in source:
    print(value)
