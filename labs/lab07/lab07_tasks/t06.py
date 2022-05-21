"""
------------------------------------------------------------------------
CP164 Lab 07, Task 06
------------------------------------------------------------------------
Author: Your Full Name
ID:     190401010
Email:  name1010@mylaurier.ca
__updated__ = "2022-03-05"
------------------------------------------------------------------------
"""
from List_linked import List

lst = List()

array = [22, 44, 55, 55, 11]

for value in array:
    lst.append(value)

lst.reverse_r()

for value in lst:
    print(value)
