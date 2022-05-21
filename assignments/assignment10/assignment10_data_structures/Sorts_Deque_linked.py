"""
-------------------------------------------------------
Linked versions of various sorts. Implemented on linked Deques.
-------------------------------------------------------
Author: Your Full Name
ID:     190401010
Email:  name1010@mylaurier.ca
__updated__ = "2021-04-09"
-------------------------------------------------------
"""


class Sorts:
    """
    -------------------------------------------------------
    Defines a number of linked sort operations.
    Uses class attribute 'swaps' to determine how many times 
    elements are swapped by the class.
    Use: print(Sorts.swaps)
    Use: Sorts.swaps = 0
    -------------------------------------------------------
    """
    swaps = 0  # Tracks swaps performed.

    # The Sorts

    @staticmethod
    def gnome_sort(a):
        """
        -------------------------------------------------------
        Sorts a Deque using the Gnome Sort algorithm.
        Use: gnome_sort(a)
        -------------------------------------------------------
        Parameters:
            a - a linked structure of comparable elements (Deque)
        Returns:
            None
        -------------------------------------------------------
        """
        current = a._front
        while current is not None:
            if a._front == current:
                current = current._next
            else:
                if current is not None:
                    if current._value < current._prev._value:
                        a._swap(current._prev, current)
                    else:
                        current = current._next
        return

    # Sort Utilities

    @staticmethod
    def sort_test(a):
        """
        -------------------------------------------------------
        Determines whether a linked deque is sorted or not.
        Use: sort_test(a)
        -------------------------------------------------------
        Parameters:
            a - a linked deque of comparable elements (?)
        Returns:
            is_sorted - True if contents of a are sorted, False otherwise.
        -------------------------------------------------------
        """
        is_sorted = True
        # Test forward links
        current = a._front

        while is_sorted and current is not None and \
                current._next is not None:

            if current._value <= current._next._value:
                current = current._next
            else:
                is_sorted = False
        # Test reverse links
        current = a._rear

        while is_sorted and current is not None and \
                current._prev is not None:

            if current._value >= current._prev._value:
                current = current._prev
            else:
                is_sorted = False

        return is_sorted
