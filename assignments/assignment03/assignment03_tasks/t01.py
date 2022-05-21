"""
------------------------------------------------------------------------
CP164 Assignment 03, Task 01
------------------------------------------------------------------------
Author: Your Full Name
ID:     190401010
Email:  name1010@mylaurier.ca
__updated__ = "2022-01-15"
------------------------------------------------------------------------
"""
from Stack_array import Stack
from functions import stack_combine
from utilities import array_to_stack

source1 = Stack()

source2 = Stack()

array_to_stack(source1, [5, 8, 12, 8])

array_to_stack(source2, [3, 6, 1, 7, 9, 14])

target = stack_combine(source1, source2)

while not target.is_empty():
    value = target.pop()
    print(value)
