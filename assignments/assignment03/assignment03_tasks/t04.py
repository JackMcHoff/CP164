"""
------------------------------------------------------------------------
CP164 Assignment 03, Task 04
------------------------------------------------------------------------
Author: Your Full Name
ID:     190401010
Email:  name1010@mylaurier.ca
__updated__ = "2022-01-15"
------------------------------------------------------------------------
"""
from Stack_array import Stack
from utilities import array_to_stack

source1 = Stack()

array_to_stack(source1, [5, 8, 12, 8])

source1.reverse()

while not source1.is_empty():
    value = source1.pop()
    print(value)
