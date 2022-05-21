"""
-------------------------------------------------------
Array versions of various sorts.
-------------------------------------------------------
Author: Your Full Name
ID:     190401010
Email:  name1010@mylaurier.ca
__updated__ = "2022-04-06"
-------------------------------------------------------
"""


class Sorts:
    """
    -------------------------------------------------------
    Defines a number of array-based sort operations.
    -------------------------------------------------------
    """
    # The Sorts

    @staticmethod
    def radix_string_sort(strings):
        """
        -------------------------------------------------------
        Performs a string radix sort.
        Use: Sorts.radix_string_sort(strings)
        -------------------------------------------------------
        Parameters:
            strings - an array of strings (list of str)
        Returns‌​​‌​‌‌‌‌:
            None
        -------------------------------------------------------
        """
        if strings != []:
            max_char = len(strings[0])
            for value in strings:
                if len(value) >= max_char:
                    max_char = len(value)
                    bucket = []
                    for _ in range(26):
                        bucket.append([])
                    for char_index in range(max_char - 1, -1, -1):
                        for value in strings:
                            temp = value.lower()
                            if len(value) >= char_index + 1:
                                bucket[
                                    ord(temp[char_index]) % 97
                                ].append(value)
                        index = 0
                        for b in bucket:
                            while len(b) > 0:
                                strings[index] = b.pop(0)
                                index += 1
        return

# DO NOT CHANGE CODE BELOW THIS LINE
# =======================================================================

    @staticmethod
    def is_sorted_alpha(strings):
        """
        -------------------------------------------------------
        Determines whether an array is sorted or not.
        Use: srtd = Sorts.is_sorted(strings)
        -------------------------------------------------------
        Parameters:
            strings - an array of strings (list of str)
        Returns‌​​‌​‌‌‌‌:
            srtd - True if contents of strings are sorted,
                False otherwise (boolean)
       -------------------------------------------------------
        """
        srtd = True
        n = len(strings)
        i = 0

        while srtd and i < n - 1:

            if strings[i].lower() <= strings[i + 1].lower():
                i += 1
            else:
                srtd = False
        return srtd
