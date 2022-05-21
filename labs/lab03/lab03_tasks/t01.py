"""
------------------------------------------------------------------------
CP164 Lab 03, Task 01
------------------------------------------------------------------------
Author: Your Full Name
ID:     190401010
Email:  name1010@mylaurier.ca
__updated__ = "2022-01-29"
------------------------------------------------------------------------
"""
from Queue_array import Queue

queue = Queue()

value = input("Enter a value: ")

queue.insert(value)

print(len(queue))
