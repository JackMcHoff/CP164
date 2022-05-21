"""
------------------------------------------------------------------------
CP164 Assignment 03, Task 06
------------------------------------------------------------------------
Author: Your Full Name
ID:     190401010
Email:  name1010@mylaurier.ca
__updated__ = "2022-01-15"
------------------------------------------------------------------------
"""
from functions import reroute

opstring = input("Enter opstring: ")

values_in = [1, 2, 3, 4, 5, 6]

values_out = reroute(opstring, values_in)

print(values_out)
