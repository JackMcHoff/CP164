"""
-------------------------------------------------------
Array-based list version of the Hash Set ADT.
-------------------------------------------------------
Author: Your Full Name
ID:     190401010
Email:  name1010@mylaurier.ca
Section: CP164 A
__updated__ = "2021-06-13"
-------------------------------------------------------
"""
# pylint: disable=protected-access

# Imports
# Use any appropriate data structure here.
from List_array import List

# Constants
SEP = '-' * 40


class Hash_Set:
    """
    -------------------------------------------------------
    Constants.
    -------------------------------------------------------
    """
    _LOAD_FACTOR = 20

    def __init__(self, capacity):
        """
        -------------------------------------------------------
        Initializes an empty Hash_Set of size capacity.
        Use: hs = Hash_Set(capacity)
        -------------------------------------------------------
        Parameter:
            capacity - size of initial table in Hash Set  (int > 0)
        Returns:
            A new Hash_Set object (Hash_Set)
        -------------------------------------------------------
        """
        self._capacity = capacity
        self._table = []
        self._count = 0

        # Define the empty table.
        for _ in range(self._capacity):
            self._table.append(List())

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of values in the Hash Set.
        Use: n = len(hs)
        -------------------------------------------------------
        Returns:
            the number of values in the Hash Set.
        -------------------------------------------------------
        """
        return self._count

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the Hash Set is empty.
        Use: b = hs.is_empty()
        -------------------------------------------------------
        Returns:
            True if the Hash Set is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._count == 0

    def _find_slot(self, key):
        """
        -------------------------------------------------------
        Returns the slot for a key value.
        Use: list = hs._find_slot(key)
        -------------------------------------------------------
        Returns:
            slot - list at the position of hash key in self._table
        -------------------------------------------------------
        """

        # your code here

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the Hash Set contains key.
        Use: b = key in hs
        -------------------------------------------------------
        Parameters:
            key - a comparable data element (?)
        Returns:
            True if the Hash Set contains key, False otherwise.
        -------------------------------------------------------
        """

        # your code here

    def insert(self, value):
        """
        ---------------------------------------------------------
        Inserts value into the Hash Set, allows only one copy of value.
        Calls _rehash if the Hash Set _LOAD_FACTOR is exceeded.
        Use: inserted = hs.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a comparable data element (?)
        Returns:
            inserted - True if value is inserted, False otherwise.
        -------------------------------------------------------
        """
        # Make sure rehash is finished before hand
        inserted = False
        crypt = hash(value)
        slot = crypt % self._capacity
        if self._count == 0:
            self._table[slot].append(value)
            inserted = True
        else:
            if self._table[slot].is_empty():
                self._table[slot].append(value)
                inserted = True
            else:
                i = self._table[slot].index(value)
                if i == -1:
                    self._table[slot].append(value)
                    inserted = True
        if inserted:
            self._count += 1
        if self._count > (self._LOAD_FACTOR * self._capacity):
            self._rehash()
        return inserted

    def find(self, key):
        """
        ---------------------------------------------------------
        Returns a copy of the value identified by key.
        Use: value = hs.find(key)
        -------------------------------------------------------
        Parameters:
            key - a comparable data element (?)
        Returns:
            value - if it exists in the Hash Set, None otherwise.
        -------------------------------------------------------
        """

        # your code here

    def remove(self, key):
        """
        ---------------------------------------------------------
        Removes the value matching key from the Hash Set, if it exists.
        Use: value = hs.remove(key)
        -------------------------------------------------------
        Parameters:
            key - a comparable data element (?)
        Returns:
            value - if it exists in the Hash Set, None otherwise.
        -------------------------------------------------------
        """
        crypt = hash(key)
        if self._count == 0:
            value = None
        else:
            slot = crypt % self._capacity
            if self._table[slot].is_empty():
                value = None
            else:
                i = self._table[slot].index(key)
                if i == -1:
                    value = None
                else:
                    value = self._table[slot][i]
                    self._table[slot].pop(i)
        return value

    def _rehash(self):
        """
        ---------------------------------------------------------
        Creates a new larger table in the Hash Set and reallocates the
        existing data within the Hash Set to the new table.
        Use: hs._rehash()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        self._capacity = (2 * self._capacity) + 1
        new_table = []
        for _ in range(self._capacity):
            new_table.append(List())
        for slots in self._table:
            for value in slots:
                crypt = hash(value) % self._capacity
                new_table[crypt].append(value)
        self._table = new_table
        return

    def is_identical(self, target):
        """
        ---------------------------------------------------------
        Determines whether two hash sets are identical.
        Use: b = source.is_identical(target)
        -------------------------------------------------------
        Parameters:
             target - another hash set (Hash_Set)
        Returns:
            identical - True if this hash set contains the same values
                as other in the same order, otherwise returns False.
        -------------------------------------------------------
        """

        # your code here

    def debug(self):
        """
        USE FOR TESTING ONLY
        ---------------------------------------------------------
        Prints the contents of the Hash Set starting at slot 0,
        showing the slot currently being printed. Used for
        debugging purposes.
        Use: hs.debug()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        print(f"{len(self._table)} slots")
        print()
        print("========================================")
        for index in range(len(self._table)):
            print(f"Slot {index}")
            print()
            for value in self._table[index]:
                print(value)
                print()
        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the hash set
        from first to last slot. Assumes slot has own iterator.
        Use: for v in q:
        -------------------------------------------------------
        Returns:
            yields
            value - the next value in the list (?)
        -------------------------------------------------------
        """
        for slot in self._table:
            for item in slot:
                yield item
