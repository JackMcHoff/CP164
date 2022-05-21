"""
------------------------------------------------------------------------
CP164 Lab 07, Task 01
------------------------------------------------------------------------
Author: Your Full Name
ID:     190401010
Email:  name1010@mylaurier.ca
__updated__ = "2022-03-05"
------------------------------------------------------------------------
"""
from List_linked import List

lst = List()

array = [22, 44, 33, 55, 11]

for value in array:
    lst.append(value)

p, c, i = lst._linear_search_r(33)

print(p._value)
print(c._value)
print(i)
