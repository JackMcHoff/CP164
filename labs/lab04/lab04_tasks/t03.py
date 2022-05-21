"""
------------------------------------------------------------------------
CP164 Lab 04, Task 03
------------------------------------------------------------------------
Author: Your Full Name
ID:     190401010
Email:  name1010@mylaurier.ca
__updated__ = "2022-02-04"
------------------------------------------------------------------------
"""
from List_array import List

list1 = List()

list1.append(100)

print(len(list1))

list1.insert(0, 200)

print(len(list1))

remove = list1.remove(200)

print(remove)
