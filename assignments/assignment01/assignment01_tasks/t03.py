"""
------------------------------------------------------------------------
CP164 Assignment 01, Task 03
------------------------------------------------------------------------
Author: Your Full Name
ID:     190401010
Email:  name1010@mylaurier.ca
__updated__ = "2022-01-15"
------------------------------------------------------------------------
"""
from functions import file_analyze

file = open('test_file.txt', 'rt')

u, l, d, w, r = file_analyze(file)

file.close()

print(f"Uppercase Letters:    {u:>2}")
print(f"Lowercase Letters:    {l:>2}")
print(f"Digits:               {d:>2}")
print(f"Whitespace Characters:{w:>2}")
print(f"Remaining Characters: {r:>2}")
