"""
------------------------------------------------------------------------
CP164 Lab 02, Task 03
------------------------------------------------------------------------
Author: Your Full Name
ID:     190401010
Email:  name1010@mylaurier.ca
__updated__ = "2022-01-21"
------------------------------------------------------------------------
"""
from Stack_array import Stack
from utilities import array_to_stack, stack_to_array

stack = Stack()

source = ["top", "bottom"]

array_to_stack(stack, source)

target = []

stack_to_array(stack, target)

print(target)
