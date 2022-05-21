"""
------------------------------------------------------------------------
CP164 Lab 02, Task 02
------------------------------------------------------------------------
Author: Your Full Name
ID:     190401010
Email:  name1010@mylaurier.ca
__updated__ = "2022-01-21"
------------------------------------------------------------------------
"""
from Stack_array import Stack
from utilities import array_to_stack

stack = Stack()

source = ["top", "bottom"]

array_to_stack(stack, source)

while not stack.is_empty():
    value = stack.pop()
    print(value)
