"""
------------------------------------------------------------------------
CP164 Assignment 01, Task 04
------------------------------------------------------------------------
Author: Your Full Name
ID:     190401010
Email:  name1010@mylaurier.ca
__updated__ = "2022-01-15"
------------------------------------------------------------------------
"""
from functions import is_leap_year

year = int(input("Enter year: "))

leap_year = is_leap_year(year)

if leap_year:
    print(f"{year} is a leap year")
else:
    print(f'{year} is not a leap year')
