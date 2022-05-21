"""
------------------------------------------------------------------------
CP164 Lab 02, Task 01
------------------------------------------------------------------------
Author: Your Full Name
ID:     190401010
Email:  name1010@mylaurier.ca
__updated__ = "2022-01-21"
------------------------------------------------------------------------
"""
from Stack_array import Stack

stack = Stack()

if stack.is_empty():
    print("Stack is empty")
else:
    print("Stack is not empty")

stack.push(1)

value = stack.pop()

print(f"{value} is no longer in the stack")

stack.push("bottom")

stack.push("top")

print(stack.peek())
