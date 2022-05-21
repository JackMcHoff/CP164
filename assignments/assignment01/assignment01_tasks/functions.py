"""
------------------------------------------------------------------------
CP164 Assignment 01, Functions
------------------------------------------------------------------------
Author: Your Full Name
ID:     190401010
Email:  name1010@mylaurier.ca
__updated__ = "2022-01-15"
------------------------------------------------------------------------
"""
# For tasks
VOWELS = ['a', 'e', 'i', 'o', 'u']


# For task 1
def clean_list(values):
    """
    -------------------------------------------------------
    Removes all duplicate values from a list: values contains
    only one copy of each of its integers. The order of values
    must be preserved.
    Use: clean_list(values)
    -------------------------------------------------------
    Parameters:
        values - a list of integers (list of int)
    Returns:
        None
    -------------------------------------------------------
    """
    temp_list = []
    index = 0
    while index < len(values):
        if values[index] not in temp_list:
            temp_list.append(values[index])
        else:
            values.pop(index)
            index -= 1
        index += 1
    return


# For task 2
def dsmvwl(s):
    """
    -------------------------------------------------------
    Disemvowels a string. out contains all the characters in s
    that are not vowels. ('y' is not considered a vowel.) Case is preserved.
    Use: out = dsmvl(s)
    -------------------------------------------------------
    Parameters:
       s - a string (str)
    Returns:
       out - s with the vowels removed (str)
    -------------------------------------------------------
    """
    out = ""
    for letter in s:
        if letter.lower() not in VOWELS:
            out += letter
    return out


# For task 3
def file_analyze(fv):
    """
    -------------------------------------------------------
    Analyzes the characters in a file.
    The contents of the file must be unchanged.
    Use: u, l, d, w, r = file_analyze(fv)
    -------------------------------------------------------
    Parameters:
        fv - an already open file reference (file variable)
    Returns:
        u - the number of uppercase letters in the file (int)
        l - the number of lowercase letters in the file (int)
        d - the number of digits in the file (int)
        w - the number of whitespace characters in the file (int)
        r - the number of remaining characters in the file (int)
    -------------------------------------------------------
    """
    u, l, d, w, r = 0, 0, 0, 0, 0
    for line in fv:
        for character in line:
            if character.isspace():
                w += 1
            elif character.isupper():
                u += 1
            elif character.islower():
                l += 1
            elif character.isdigit():
                d += 1
            else:
                r += 1
    return u, l, d, w, r


# For task 4
def is_leap_year(year):
    """
    -------------------------------------------------------
    Leap year determination.
    Use: leap_year = is_leap_year(year)
    -------------------------------------------------------
    Parameters:
        year - year to determine if it is a leap year (int > 0)
    Returns:
        leap_year - True if year is a leap year, False otherwise (boolean)
    -------------------------------------------------------
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap_year = True
            else:
                leap_year = False
        else:
            leap_year = True
    else:
        leap_year = False
    return leap_year


# For task 5
def is_palindrome(s):
    """
    -------------------------------------------------------
    Determines if s is a palindrome. Ignores case, spaces, and
    punctuation in s.
    Use: palindrome = is_palindrome(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        palindrome - True if s is a palindrome, False otherwise (boolean)
    -------------------------------------------------------
    """
    palindrome = True
    index = 0
    negative_index = -1
    while index <= range(int(len(s)/2)) and palindrome:
        if not (s[index].isalnum()):
            index += 1
        elif not (s[negative_index].isalnum()):
            negative_index -= 1
        elif s[index].lower() != s[negative_index].lower():
            palindrome = False
            index += 1
            negative_index -= 1
        else:
            index += 1
            negative_index -= 1
    return palindrome

# For task 6
def max_diff(a):
    """
    -------------------------------------------------------
    Returns maximum absolute difference between adjacent values in a list.
    a must be unchanged.
    Use: md = max_diff(a)
    -------------------------------------------------------
    Parameters:
        a - a list of values (list of int)
    Returns:
        md - the largest absolute difference between adjacent
            values in a list (int)
    -------------------------------------------------------
    """
    highest = 0
    for index in range((len(a) - 1)):
        current_val = abs(a[index] - a[index + 1])
        if current_val > highest:
            highest = current_val
    return highest


# For task 7
def matrix_transpose(a):
    """
    -------------------------------------------------------
    Transpose the contents of matrix a.
    Use: b = matrix_transpose(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list (list of lists of ?)
    Returns:
        b - the transposed matrix (list of lists of ?)
    -------------------------------------------------------
    """
    b = []
    for index_list1 in range(len(a[0])):
        temp_list = []
        for index_main_list in range(len(a)):
            temp_list.append(a[index_main_list][index_list1])
        b.append(temp_list)
    return b


# For task 8
def matrix_stats(a):
    """
    -------------------------------------------------------
    Determines the smallest, largest, total, and average of
    the values in the 2D list a. You may assume there is at
    least one value in a.
    a must be unchanged.
    Use: small, large, total, average = matrix_stats(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list of numbers (2D list of float)
    Returns:
        small - the smallest number in a (float)
        large - the largest number in a (float)
        total - the total of all numbers in a (float)
        average - the average of all numbers in a (float)
    -------------------------------------------------------
    """
    small = a[0][0]
    large = a[0][0]
    total = 0
    average = 0
    for lists in a:
        for value in lists:
            if value < small:
                small = value
            elif value > large:
                large = value
            total += value
            average += 1
    average = total / average
    return small, large, total, average


# For task 9
def pig_latin(word):
    """
    -------------------------------------------------------
    Converts a word to Pig Latin. The conversion is:
    - if a word begins with a vowel, add "way" to the end of the word.
    - if the word begins with consonants, move the leading consonants to
    the end of the word and add "ay" to the end of that.
    "y" is treated as a consonant if it is the first character in the word,
    and as a vowel for anywhere else in the word.
    Preserve the case of the word - i.e. if the first character of word
    is upper-case, then the new first character should also be upper case.
    Use: pl = pig_latin(word)
    -------------------------------------------------------
    Parameters:
        word - a string to convert to Pig Latin (str)
    Returns:
        pl - the Pig Latin version of word (str)
    ------------------------------------------------------
    """
    pl = ""
    if word[0].lower() in VOWELS:
        pl = word + 'way'
    else:
        capital = False
        index = 0
        not_done = True
        temp_word = ""
        if word[0].isupper():
            capital = True
        while index < len(word) and not_done:
            if word[index] in VOWELS:
                not_done = False
            else:
                temp_word += word[index].lower()
                index += 1
        pl = word[index:] + temp_word + 'ay'
        if capital:
            pl = pl.capitalize()
    return pl
