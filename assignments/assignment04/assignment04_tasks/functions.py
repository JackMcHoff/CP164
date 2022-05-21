"""
------------------------------------------------------------------------
CP164 Assignment 04, Functions
------------------------------------------------------------------------
Author: Your Full Name
ID:     190401010
Email:  name1010@mylaurier.ca
__updated__ = "2022-02-02"
------------------------------------------------------------------------
"""
from Priority_Queue_array import Priority_Queue
from Queue_array import Queue


def queue_split_alt(source):
    """
    -------------------------------------------------------
    Splits the source queue into separate target queues with values
    alternating into the targets. At finish source queue is empty.
    Order of source values is preserved.
    (iterative algorithm)
    Use: target1, target2 = queue_split_alt(source)
    -------------------------------------------------------
    Parameters:
        source - a queue (Queue)
    Returns:
        target1 - contains alternating values from source (Queue)
        target2 - contains other alternating values from source (Queue)
    -------------------------------------------------------
    """
    target1 = Queue()
    target2 = Queue()
    while len(source) > 0:
        if len(source) > 0:
            target1.insert(source.remove())
        if len(source) > 0:
            target2.insert(source.remove())
    return target1, target2


def pq_split_key(source, key):
    """
    -------------------------------------------------------
    Splits a priority queue into two depending on an external
    priority key. The source priority queue is empty when the method
    ends.
    Use: target1, target2 = pq_split_key(source, key)
    -------------------------------------------------------
    Parameters:
        source - a priority queue (Priority_Queue)
        key - a data object (?)
    Returns:
        target1 - a priority queue that contains all values
            with priority higher than key (Priority_Queue)
        target2 - priority queue that contains all values with
            priority lower than or equal to key (Priority_Queue)
    -------------------------------------------------------
    """
    target1 = Priority_Queue()
    target2 = Priority_Queue()
    while len(source) > 0:
        value = source.remove()
        if value < key:
            target1.insert(value)
        else:
            target2.insert(value)
    return target1, target2
