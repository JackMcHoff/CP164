"""
------------------------------------------------------------------------
CP164 Assignment 01, Task 01
------------------------------------------------------------------------
Author: Your Full Name
ID:     190401010
Email:  name1010@mylaurier.ca
__updated__ = "2022-01-15"
------------------------------------------------------------------------
"""
from functions import clean_list

string_values = input('Enter values (seperated by a comma): ').split(',')

values = []

for i in string_values:
    values.append(int(i))

clean_list(values)

print(f'Cleaned List: {values}')
