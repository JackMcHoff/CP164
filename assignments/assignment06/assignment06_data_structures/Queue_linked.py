"""
-------------------------------------------------------
Linked version of the Queue ADT.
-------------------------------------------------------
Author: Your Full Name
ID:     190401010
Email:  name1010@mylaurier.ca
Term:    Spring 2021
__updated__ = "2021-06-04"
-------------------------------------------------------
"""
from copy import deepcopy


class _Queue_Node:

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a queue node that contains a copy of value
        and a link to the next node in the queue.
        Use: node = _Queue_Node(value, _next)
        -------------------------------------------------------
        Parameters:
            value - value for node (?)
            next_ - another Queue node (_Queue_Node)
        Returns:
            a new _Queue_Node object (_Queue_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = next_


class Queue:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty queue. Values are stored in a
        linked structure.
        Use: queue = Queue()
        -------------------------------------------------------
        Returns:
            a new Queue object (Queue)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the queue is empty.
        Use: b = queue.is_empty()
        -------------------------------------------------------
        Returns:
            True if queue is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._count == 0

    def is_full(self):
        """
        -------------------------------------------------------
        Determines if the queue is full.
        Use: b = queue.is_full()
        -------------------------------------------------------
        Returns:
            True if queue is full, False otherwise.
        -------------------------------------------------------
        """
        # Queue is never full since there is no capacity
        return False

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the length of the queue.
        Use: n = len(queue)
        -------------------------------------------------------
        Returns:
            the number of values in queue.
        -------------------------------------------------------
        """
        return self._count

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the queue.
        Use: queue.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            a copy of value is added to the rear of queue.
        -------------------------------------------------------
        """
        new_node = _Queue_Node(value, None)
        if self._front == None:
            self._front = new_node
            self._rear = new_node
        else:
            self._rear._next = new_node
            self._rear = new_node
        self._count += 1
        return

    def remove(self):
        """
        -------------------------------------------------------
        Removes and returns value from the queue.
        Use: value = queue.remove()
        -------------------------------------------------------
        Returns:
            value - the value at the front of the queue - the value is
            removed from queue (?)
        -------------------------------------------------------        
        """
        assert self._front is not None, "Cannot remove from an empty queue"

        return_node = self._front._value
        if self._front == self._rear:
            self._front = None
            self._rear = None
        else:
            self._front = self._front._next
        self._count -= 1
        return return_node

    def peek(self):
        """
        -------------------------------------------------------
        Peeks at the front of queue.
        Use: value = queue.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the front of queue -
            the value is not removed from queue (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot peek at an empty queue"

        return deepcopy(self._front._value)

    def _move_front(self, source):
        """
        -------------------------------------------------------
        Moves the front node from the source queue to the rear of the target queue.
        The target queue contains the old front node of the source queue.
        The source queue front is updated.
        Use: target._move_front(source)
        -------------------------------------------------------
        Parameters:
            source - a linked queue (Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        assert source._front is not None, "Cannot move the front of an empty queue"

        if self._front == None:
            self._front = source._front
            self._rear = self._front
        else:
            self._rear._next = source._front
            self._rear = source._front
        if source._front == source._rear:
            source._front = None
            source._rear = None
        else:
            source._front = source._front._next
        self._rear._next = None
        self._count += 1
        source._count -= 1
        return

    def _append_queue(self, source):
        """
        -------------------------------------------------------
        Appends the entire source queue to the rear of the target queue.
        The source queue becomes empty.
        Use: target._append_queue(source)
        -------------------------------------------------------
        Parameters:
            source - an linked-based queue (Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        assert source._front is not None, "Cannot append an empty queue"

        while source._count > 0:
            self._move_front(source)
        return

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source queues into the current target queue. 
        When finished, the contents of source1 and source2 are interlaced 
        into target and source1 and source2 are empty.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an linked queue (Queue)
            source2 - an linked queue (Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        while source1._count > 0 or source2._count > 0:
            if source1._count > 0:
                self._move_front(source1)
            if source2._count > 0:
                self._move_front(source2)
        return

    def split_alt(self):
        """
        -------------------------------------------------------
        Splits the source queue into separate target queues with values 
        alternating into the targets. At finish source queue is empty.
        (iterative algorithm)
        Use: target1, target2 = source.split()
        -------------------------------------------------------
        Returns:
            target1 - contains alternating values from source (Queue)
            target2 - contains other alternating values from source (Queue)
        -------------------------------------------------------
        """
        target1 = Queue()
        target2 = Queue()
        while self._count > 0:
            target1._move_front(self)
            if self._count > 0:
                target2._move_front(self)
        if self._count == 0:
            self._rear = None
        return target1, target2

    def is_identical(self, target):
        """
        -------------------------------------------------------
        Determines whether two queues are identical.
        Values of self and target are compared and if all contents 
        are identical and in the same order, returns True, otherwise 
        returns False. Queues are unchanged.
        (iterative algorithm)
        Use: b = source.is_identical(target)
        -------------------------------------------------------
        Parameters:
            target - a queue (Queue)
        Returns:
            identical - True if self and target are identical, False 
                otherwise. (boolean)
        -------------------------------------------------------
        """
        identical = True
        if self._count != target._count:
            identical = False
        else:
            current = self._front
            current_target = target._front
            index = 0
            while index < self._count and identical:
                if current._value != current_target._value:
                    identical = False
                current = current._next
                current_target = current_target._next
                index += 1
        return identical

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the queue
        from front to rear.
        Use: for v in q:
        -------------------------------------------------------
        Returns:
            value - the next value in the queue (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._next
