"""
------------------------------------------------------------------------
CP164 Assignment 03, Functions
------------------------------------------------------------------------
Author: Your Full Name
ID:     190401010
Email:  name1010@mylaurier.ca
__updated__ = "2022-01-15"
------------------------------------------------------------------------
"""
from Stack_array import Stack


# For task 1
def stack_combine(source1, source2):
    """
    -------------------------------------------------------
    Combines two source stacks into a target stack.
    When finished, the contents of source1 and source2 are interlaced
    into target and source1 and source2 are empty.
    Use: target = stack_combine(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a stack (Stack)
        source2 - another stack (Stack)
    Returns:
        target - the contents of the source1 and source2
            are interlaced into target (Stack)
    -------------------------------------------------------
    """
    target = Stack()
    index = 1
    while (not source1.is_empty()) or (not source2.is_empty()):
        if (index % 2 == 0) and (not source2.is_empty()) or source1.is_empty():
            value = source2.pop()
            target.push(value)
        else:
            value = source1.pop()
            target.push(value)
        index += 1
    return target


# For task 3
def stack_reverse(source):
    """
    -------------------------------------------------------
    Reverses the contents of a stack.
    Use: stack_reverse(source)
    -------------------------------------------------------
    Parameters:
        source - a Stack (Stack)
    Returns:
        None
    -------------------------------------------------------
    """
    array = []
    while not source.is_empty():
        value = source.pop()
        array.insert(0, value)

    for index in range(len(array) - 1, -1, -1):
        value = array.pop(index)
        source.push(value)
    return


# For task 5
def is_palindrome_stack(string):
    """
    -------------------------------------------------------
    Determines if string is a palindrome. Ignores case, digits, spaces, and
    punctuation in string.
    Use: palindrome = is_palindrome_stack(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        palindrome - True if string is a palindrome, False otherwise (bool)
    -------------------------------------------------------
    """
    palindrome = True
    stack = Stack()
    reverse_index = len(string) - 1
    index = 0
    add = True
    while index < len(string) and reverse_index > 0 and palindrome:
        if string[index].isalpha() and add:
            stack.push(string[index].lower())
        elif string[reverse_index].isalpha() and add:
            reverse_index += 1
        else:
            add = True
        if reverse_index < len(string):
            if string[reverse_index].isalpha():
                if (not stack.is_empty()):
                    if string[reverse_index].lower() != stack.pop():
                        palindrome = False
            elif string[index].isalpha():
                add = False
                index -= 1
        reverse_index -= 1
        index += 1
    return palindrome


# For task 6
def reroute(opstring, values_in):
    """
    -------------------------------------------------------
    Reroutes values in a list according to a operating string and
    returns a new list of values. values_in is unchanged.
    In opstring, 'S' means push onto stack,
    'X' means pop from stack into values_out.
    Use: values_out = reroute(opstring, values_in)
    -------------------------------------------------------
    Parameters:
        opstring - String containing only 'S' and 'X's (str)
        values_in - A valid list (list of ?)
    Returns:
        values_out - if opstring is valid then values_out contains a
            reordered version of values_in, otherwise returns
            None (list of ?)
    -------------------------------------------------------
    """
    stack = Stack()
    values_out = []
    index = 0
    values_index = 0
    cont = True
    while index < len(opstring) and cont and values_index <= len(values_in):
        if opstring[index] == "S" and values_index < len(values_in):
            stack.push(values_in[values_index])
            values_index += 1
        elif opstring[index] == "X":
            if stack.is_empty():
                cont = False
                values_out = None
            else:
                values_out.append(stack.pop())
        index += 1
    if not stack.is_empty():
        values_out = None
    elif index < len(opstring) - 1:
        values_out = None
    elif values_index < len(values_in) - 1:
        values_out = None
    return values_out
