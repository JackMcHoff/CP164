"""
------------------------------------------------------------------------
CP164 Lab 08, Task 04
------------------------------------------------------------------------
Author: Your Full Name
ID:     190401010
Email:  name1010@mylaurier.ca
__updated__ = "2022-03-12"
------------------------------------------------------------------------
"""
from BST_linked import BST
from morse import DATA1, fill_code_bst


bst = BST()

fill_code_bst(bst, DATA1)

for value in bst:
    print(value.letter, value.code)
