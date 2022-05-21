"""
-------------------------------------------------------
Tests various array-based sorting functions.
-------------------------------------------------------
Author: Your Full Name
ID:     190401010
Email:  name1010@mylaurier.ca
Section: CP164 C
__updated__ = "2019-04-27"
-------------------------------------------------------
"""
# Imports
import random
from Number import Number
from Sorts_array import Sorts


# Constants
SIZE = 100  # Size of array to sort.
XRANGE = 1000  # Range of values in random arrays to sort.
TESTS = 100  # Number of random arrays to generate.

SORTS = (
    ('Bubble Sort', Sorts.bubble_sort),
    ('Insertion Sort', Sorts.insertion_sort),
    ('Merge Sort', Sorts.merge_sort),
    ('Quick Sort', Sorts.quick_sort),
    ('Selection Sort', Sorts.selection_sort),
    ('Bin. Ins. Sort', Sorts.binary_insert_sort),
    ('BST Sort', Sorts.bst_sort),
    ('Cocktail Sort', Sorts.cocktail_sort),
    ('Comb Sort', Sorts.comb_sort),
    ('Heap Sort', Sorts.heap_sort),
    ('Shell Sort', Sorts.shell_sort)
)


def create_sorted():
    """
    -------------------------------------------------------
    Creates a sorted list of SIZE Number objects with values
        from 0 up to SIZE-1.
    Use: values = create_sorted()
    -------------------------------------------------------
    Returns:
        values - a sorted list of SIZE Number objects (list of Number)
    -------------------------------------------------------
    """
    values = []
    for value in range(SIZE):
        values.append(Number(value))
    return values


def create_reversed():
    """
    -------------------------------------------------------
    Create a reversed list of SIZE Number objects with values
        from SIZE-1 down to 0.
    Use: values = create_reversed()
    -------------------------------------------------------
    Returns:
        values - a reversed list of SIZE Number objects (list of Number)
    -------------------------------------------------------
    """
    values = []
    for value in range(SIZE - 1, -1, -1):
        values.append(Number(value))
    return values


def create_randoms():
    """
    -------------------------------------------------------
    Create a 2D list of Number objects with TESTS rows and
    SIZE columns of values between 0 and XRANGE.
    Use: lists = create_randoms()
    -------------------------------------------------------
    Returns:
        arrays - TESTS lists of SIZE Number objects containing
            values between 0 and XRANGE (list of list of Number)
    -------------------------------------------------------
    """
    arrays = []
    for _ in range(SIZE):
        temp_array = []
        for _ in range(TESTS):
            value = random.randint(0, XRANGE)
            temp_array.append(Number(value))
        arrays.append(temp_array)
    return arrays


def test_sort(title, func):
    """
    -------------------------------------------------------
    Test a sort function with Number data and prints the number 
    of comparisons necessary to sort an array:
    in order, in reverse order, and a list of arrays in random order.
    Use: test_sort(title, func)
    -------------------------------------------------------
    Parameters:
        title - name of the sorting function to call (str)
        func - the actual sorting function to call (function)
    Returns:
        None
    -------------------------------------------------------
    """
    Number.comparisons = 0
    Sorts.swaps = 0
    # Run For In Order
    values = create_sorted()
    func(values)
    in_order_total = int(Number.comparisons)
    in_order_swaps = int(Sorts.swaps)
    # Run For Reversed Order
    Number.comparisons = 0
    Sorts.swaps = 0
    values = create_reversed()
    func(values)
    reversed_total = int(Number.comparisons)
    reversed_swaps = int(Sorts.swaps)
    # Run For Random Order
    Number.comparisons = 0
    Sorts.swaps = 0
    arrays = create_randoms()
    for array in arrays:
        func(array)
    random_total = int((Number.comparisons) // TESTS)
    random_swaps = int((Sorts.swaps) // TESTS)
    # Print Data
    print(f"{title:14} {in_order_total:>8} {reversed_total:>8} {random_total:>8} {in_order_swaps:>8} {reversed_swaps:>8} {random_swaps:>8}")
    return
