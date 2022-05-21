"""
------------------------------------------------------------------------
CP164 Lab 08, Task 05
------------------------------------------------------------------------
Author: Your Full Name
ID:     190401010
Email:  name1010@mylaurier.ca
__updated__ = "2022-03-12"
------------------------------------------------------------------------
"""
from BST_linked import BST
from morse import DATA1, fill_letter_bst, encode_morse


bst = BST()

fill_letter_bst(bst, DATA1)

text = input("Enter a String: ")

print(encode_morse(bst, text))
