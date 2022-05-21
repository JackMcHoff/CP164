"""
-------------------------------------------------------
Linked version of the Deque Set ADT.
-------------------------------------------------------
Author: Your Full Name
ID:     190401010
Email:  name1010@mylaurier.ca
__updated__ = "2022-04-06"
-------------------------------------------------------
"""
# pylint: disable=protected-access

# Imports
from copy import deepcopy


class _Deque_Set_Node:

    def __init__(self, value, _prev, _next):
        """
        -------------------------------------------------------
        Initializes a Deque_Set node.
        Use: node = _Deque_Set_Node(value, _prev, _next)
        -------------------------------------------------------
        Parameters:
            value - value value for node (?)
            _prev - another Deque_Set node (_Deque_Set_Node)
            _next - another Deque_Set node (_Deque_Set_Node)
        Returns‌​​‌​‌‌‌‌:
            a new _Deque_Set_Node object (_Deque_Set_Node)

        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._prev = _prev
        self._next = _next


class Deque_Set:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty Deque_Set.
        Use: d = Deque_Set()
        -------------------------------------------------------
        Returns‌​​‌​‌‌‌‌:
            a new Deque_Set object (Deque_Set)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def _linear_search(self, key):
        """
        -------------------------------------------------------
        Private helper method.
        Searches for key in a Deque_Set.
        Use: curr = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (*)
        Returns‌​​‌​‌‌‌‌:
            curr - pointer to node containing key, None if not found (_Deque_Set_Node)
        -------------------------------------------------------
        """
        curr = self._front
        while curr is not None and curr._value != key:
            curr = curr._next
        return curr

    def _move_front_to_rear(self, source):
        """
        -------------------------------------------------------
        Private helper method.
        Moves the front node from source to the rear of self.
        Does *not* validate that self is still a set.
        Use: self._move_front_to_rear(source)
        -------------------------------------------------------
        Parameters:
            source - a non-empty Deque_Set (Deque_Set)
        Returns‌​​‌​‌‌‌‌:
            self contains the old front of source as its rear.
            source front is updated. The counts of self and source are updated.
        -------------------------------------------------------
        """
        assert source._front is not None, \
            "Cannot move the front of an empty Deque_Set"

        if self._rear is not None:
            self._rear._next = source._front
        else:
            self._rear = source._front
        source._front._prev = self._rear
        self._rear = source._front
        if self._front is None:
            self._front = self._rear
        self._count += 1

        if source._front._next == source._rear:
            source._front = source._rear
            source._front._prev = None
        elif source._front._next is None:
            source._front = None
            source._rear = None
        else:
            source._front = source._front._next
            source._front._prev = None
        self._rear._next = None
        source._count -= 1
        return

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if a Deque_Set is empty.
        Use: b = source.is_empty()
        -------------------------------------------------------
        Returns‌​​‌​‌‌‌‌:
            True if source is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._count == 0

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the size of a Deque_Set.
        Use: n = len(source)
        -------------------------------------------------------
        Returns‌​​‌​‌‌‌‌:
            the number of values in source (int)
        -------------------------------------------------------
        """
        return self._count

    def insert_front(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the front of a Deque_Set.
        value cannot already be in the Deque_Set.
        Updates _count appropriately.
        Use: source.insert_front(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (*)
        Returns‌​​‌​‌‌‌‌:
            inserted - True if value is added to front of source, False otherwise.
        -------------------------------------------------------
        """
        inserted = False
        curr = self._linear_search(value)
        if curr is None:
            self._count += 1
            self._front = _Deque_Set_Node(value, None, self._front)
            if self._rear is None:
                self._rear = self._front
            else:
                self._front._next._prev = self._front
        return inserted

    def insert_rear(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the front of a Deque_Set.
        value cannot already be in the Deque_Set.
        Updates _count appropriately.
        Use: source.insert_rear(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (*)
        Returns‌​​‌​‌‌‌‌:
            inserted - True if value is added to rear of source, False otherwise.
        -------------------------------------------------------
        """
        inserted = False
        curr = self._linear_search(value)
        if curr is None:
            self._count += 1
            self._rear = _Deque_Set_Node(value, self._rear, None)
            if self._front is None:
                self._front = self._rear
            else:
                self._rear._prev._next = self._front
        return inserted

    def remove_front(self):
        """
        -------------------------------------------------------
        Removes and returns value from the front of a Deque_Set.
        Updates _count appropriately.
        Use: v = source.remove_front()
        -------------------------------------------------------
        Returns‌​​‌​‌‌‌‌:
            value - the value at the front of source (*)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot remove from an empty Deque_Set"

        self._count -= 1
        value = self._front._value
        self._front = self._front._next
        self._front._prev = None
        return value

    def remove_rear(self):
        """
        -------------------------------------------------------
        Removes and returns value from the rear of a Deque_Set.
        Updates _count appropriately.
        Use: v = source.remove_rear()
        -------------------------------------------------------
        Returns‌​​‌​‌‌‌‌:
            value - the value at the rear of source (*)
        -------------------------------------------------------
        """
        assert self._rear is not None, "Cannot remove from an empty Deque_Set"

        self._count -= 1
        value = self._rear._value
        self._rear = self._rear._prev
        self._rear._next = None
        return value

    def remove(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in source that matches key.
        Updates _count appropriately.
        Use: value = source.remove(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (*)
        Returns‌​​‌​‌‌‌‌:
            value - the full value matching key, otherwise None (*)
        -------------------------------------------------------
        """
        curr = self._linear_search(key)
        if curr is not None:
            self._count -= 1
            curr._prev._next = curr._next
            curr._next._prev = curr._prev
            if self._front == curr:
                self._front = curr._next
            if self._rear == curr:
                self._rear = curr._prev
        return curr._value

    def max(self):
        """
        -------------------------------------------------------
        Finds the maximum value in a Deque_Set.
        Use: value = source.max()
        -------------------------------------------------------
        Returns‌​​‌​‌‌‌‌:
            a copy of the maximum value in source (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find maximum of an empty Deque_Set"

        curr = self._front
        value = self._front
        while curr is not None:
            if value < curr._value:
                value = curr._value
            curr = curr._next
        return value

    def split_key(self, key):
        """
        -------------------------------------------------------
        Splits source so that target1 contains all values < key,
        and target2 contains all values >= key. source is empty
        when finished.
        Nodes are moved, values are not copied.
        Updates _count appropriately.
        Use: target1, target2 = source.split_key(key)
        -------------------------------------------------------
        Parameters:
            key - a key value to split source upon (?)
        Returns‌​​‌​‌‌‌‌:
            target1 - a new Deque_Set of values < key (Deque_Set)
            target2 - a new Deque_Set of values >= key (Deque_Set)
        -------------------------------------------------------
        """
        target1 = Deque_Set()
        target2 = Deque_Set()
        while self._front is not None:
            if self._front._value < key:
                target1._move_front_to_rear(self)
            if self._front is not None and self._front._value >= key:
                target2._move_front_to_rear(self)
        return target1, target2

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines source1 and source2 into target.
        When finished, the contents of source1 and source2 are interlaced
        into target and source1 and source2 are empty.
        Order of source values is preserved.
        Values may appear only once in target.
        Nodes are moved, values are not copied.
        Updates _count appropriately.
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a Deque_Set (Deque_Set)
            source2 - a Deque_Set (Deque_Set)
        Returns‌​​‌​‌‌‌‌:
            None
        -------------------------------------------------------
        """
        assert self._front is None, "target must be empty"
        while source1._front is not None or source2._front is not None:
            if source1._front is not None:
                curr = self._linear_search(source1._front._value)
                if curr is None:
                    self._move_front_to_rear(source1)
            if source2._front is not None:
                curr = self._linear_search(source2._front._value)
                if curr is None:
                    self._move_front_to_rear(source2)
        return

# DO NOT CHANGE CODE BELOW THIS LINE
# =======================================================================

    def peek_front(self):
        """
        -------------------------------------------------------
        Peeks at the front of a Deque_Set.
        Use: v = source.peek_front()
        -------------------------------------------------------
        Returns‌​​‌​‌‌‌‌:
            a copy of the value at the front of source (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot peek at an empty Deque_Set"

        return deepcopy(self._front._value)

    def peek_rear(self):
        """
        -------------------------------------------------------
        Peeks at the rear of a Deque_Set.
        Use: v = source.peek_rear()
        -------------------------------------------------------
        Returns‌​​‌​‌‌‌‌:
            a copy of the value at the rear of source (?)
        -------------------------------------------------------
        """
        assert self._rear is not None, "Cannot peek at an empty Deque_Set"

        return deepcopy(self._rear._value)

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the deque
        from front to rear.
        Use: for v in d:
        -------------------------------------------------------
        Returns‌​​‌​‌‌‌‌:
            yields
            value - the next value in the deque (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._next
