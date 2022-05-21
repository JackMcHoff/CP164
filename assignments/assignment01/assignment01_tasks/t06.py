"""
------------------------------------------------------------------------
CP164 Assignment 01, Task 06
------------------------------------------------------------------------
Author: Your Full Name
ID:     190401010
Email:  name1010@mylaurier.ca
__updated__ = "2022-01-15"
------------------------------------------------------------------------
"""
from functions import max_diff

string_values = input('Enter values (seperated by a comma): ').split(',')

values = []

for i in string_values:
    values.append(int(i))

diff = max_diff(values)

print(f"Biggest Difference: {diff}")
