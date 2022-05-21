"""
------------------------------------------------------------------------
CP164 Lab 03 Task 02
------------------------------------------------------------------------
Author: Your Full Name
ID:     190401010
Email:  name1010@mylaurier.ca
__updated__ = "2022-01-29"
------------------------------------------------------------------------
"""
from Queue_array import Queue

queue = Queue()

insert_value = input("Enter a value: ")

queue.insert(insert_value)

print(queue.peek())

value = queue.remove()

print(value)
