"""
------------------------------------------------------------------------
CP164 Lab 03 Task 05
------------------------------------------------------------------------
Author: Your Full Name
ID:     190401010
Email:  name1010@mylaurier.ca
__updated__ = "2022-01-29"
------------------------------------------------------------------------
"""
from Priority_Queue_array import Priority_Queue

pq = Priority_Queue()

value = int(input("Enter a number: "))

pq.insert(value)

print(pq.remove())
