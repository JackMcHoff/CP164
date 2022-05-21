"""
------------------------------------------------------------------------
CP164 Lab 09, Functions
------------------------------------------------------------------------
Author: Your Full Name
ID:     190401010
Email:  name1010@mylaurier.ca
__updated__ = "2022-03-18"
------------------------------------------------------------------------
"""


def hash_table(slots, values):
    """
    -------------------------------------------------------
    Print a hash table of a set of values. The format is:
Hash     Slot Key
-------- ---- --------------------
     695    2 Lasagna, 7
    1355    4 Butter Chicken, 2
    Do not create an actual Hash_Set.
    Use: hash_table(slots, values)
    -------------------------------------------------------
    Parameters:
       slots - the number of slots available (int > 0)
       values - the values to hash (list of ?)
    Returns:
       None
    -------------------------------------------------------
    """
    print("Hash     Slot Key")
    print("-------- ---- --------------------")
    for value in values:
        crypt = hash(value)
        slot = crypt % slots
        print(f"{crypt:>8} {slot:>4} {value.key()}")
    return
