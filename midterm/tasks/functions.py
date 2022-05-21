"""
-------------------------------------------------------
Midterm Functions
-------------------------------------------------------
Author: Your Full Name
ID:     190401010
Email:  name1010@mylaurier.ca
__updated__ = "2022-02-12"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack

# Constants
OPERATORS = ('*', '/', '+', '-')


def pq_triage(source, key):
    """
    -------------------------------------------------------
    Removes all values from source that have a priority
    less than key.
    Use: pq_triage(source, key)
    -------------------------------------------------------
    Parameters:
        source - a priority queue (Priority_Queue)
        key - a key value (?)
    Returns‌​‌​‌‌‌​‌:
        None
    -------------------------------------------------------
    """
    temp = []
    while not source.is_empty():
        temp.append(source.remove())
    for value in temp:
        if value < key:
            source.insert(value)
    return


def purge(source, key):
    """
    -------------------------------------------------------
    Finds and removes all values in source that match key.
    Use: purge(source, key)
    -------------------------------------------------------
    Parameters:
        source - a List of values (List)
        key - a data element (?)
    Returns‌​‌​‌‌‌​‌:
        None
    -------------------------------------------------------
    """
    value = source.remove(key)
    while value != None:
        value = source.remove(key)
    return


def eval_expression(string):
    """
    -------------------------------------------------------
    Evaluates a postfix expression.
    Use: answer = eval_expression(string)
    -------------------------------------------------------
    Parameters:
        string - the space-separted postfix string to evaluate (str)
    Returns‌​‌​‌‌‌​‌:
        answer - the result of evaluating string (float)
    -------------------------------------------------------
    """
    stack = Stack()
    lst = string.split(" ")
    for value in lst:
        if value in OPERATORS:
            if not stack.is_empty():
                num2 = stack.pop()
                if not stack.is_empty():
                    num1 = stack.pop()
                if value == OPERATORS[0]:
                    num = num1 * num2
                    stack.push(num)
                elif value == OPERATORS[1]:
                    num = num1 / num2
                    stack.push(num)
                elif value == OPERATORS[2]:
                    num = num1 + num2
                    stack.push(num)
                elif value == OPERATORS[3]:
                    num = num1 - num2
                    stack.push(num)
        else:
            stack.push(float(value))
    if not stack.is_empty():
        answer = stack.pop()
    return answer
