"""
------------------------------------------------------------------------
CP164 Assignment 01, Task 05
------------------------------------------------------------------------
Author: Your Full Name
ID:     190401010
Email:  name1010@mylaurier.ca
__updated__ = "2022-01-15"
------------------------------------------------------------------------
"""
from functions import is_palindrome

s = input("Enter word: ")

palindrome = is_palindrome(s)

if palindrome:
    print(f"{s} is a palindrome")
else:
    print(f'{s} is not a palindrome')
