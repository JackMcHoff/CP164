"""
------------------------------------------------------------------------
CP164 Assignment 05, Task 01
------------------------------------------------------------------------
Author: Your Full Name
ID:     190401010
Email:  name1010@mylaurier.ca
__updated__ = "2022-03-02"
------------------------------------------------------------------------
"""
from Queue_linked import Queue

queue = Queue()

print("Queue is empty: ")
print(queue.is_empty())

print()
print("Queue is Full: ")
print(queue.is_full())

print()
print("Length of queue: ")
print(len(queue))

queue.insert(11)

print()
print("Length of queue: ")
print(len(queue))

queue.insert(22)

print()
print("Removed Node: ")
print(queue.remove())

print()
print("First item in queue: ")
print(queue.peek())

queue1 = Queue()

queue1.insert(44)

queue2 = Queue()

queue2.combine(queue, queue1)

print()
print("Printing queue2: ")
for value in queue2:
    print(value)

target1, target2 = queue2.split_alt()

print()
print("Printing target1: ")
for value in target1:
    print(value)

print()
print("Printing target2: ")
for value in target2:
    print(value)
