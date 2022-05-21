"""
------------------------------------------------------------------------
CP164 Assignment 04, Task 04
------------------------------------------------------------------------
Author: Your Full Name
ID:     190401010
Email:  name1010@mylaurier.ca
__updated__ = "2022-02-02"
------------------------------------------------------------------------
"""
from Priority_Queue_array import Priority_Queue
from functions import pq_split_key

source = Priority_Queue()

source.insert(1)

source.insert(2)

source.insert(3)

key = 2

target1, target2 = pq_split_key(source, key)


print("Printing Target 1...")
while len(target1) > 0:
    print(target1.remove())

print("Printing Target 2...")
while len(target2) > 0:
    print(target2.remove())
