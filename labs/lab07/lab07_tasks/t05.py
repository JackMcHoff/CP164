"""
------------------------------------------------------------------------
CP164 Lab 07, Task 05
------------------------------------------------------------------------
Author: Your Full Name
ID:     190401010
Email:  name1010@mylaurier.ca
__updated__ = "2022-03-05"
------------------------------------------------------------------------
"""
from List_linked import List

lst1 = List()

lst2 = List()

lst3 = List()

array = [22, 44, 33, 55, 11]

array2 = [22, 44, 10, 55, 11]

for value in array:
    lst1.append(value)

for value in array2:
    lst2.append(value)

lst3.union_r(lst1, lst2)

for value in lst3:
    print(value)
