"""
------------------------------------------------------------------------
CP164 Assignment 05, Task 2
------------------------------------------------------------------------
Author: Your Full Name
ID:     190401010
Email:  name1010@mylaurier.ca
__updated__ = "2022-02-10"
------------------------------------------------------------------------
"""
# Imports
from Sorted_List_array import Sorted_List


# Test the clean method

# Set up a sorted list
lst = Sorted_List()

# Use the insert method to
#  add values to the list
lst.insert(100)

lst.insert(200)

lst.insert(200)

lst.clean()

# Print the values to make sure it works
print()
print("Printing")
for value in lst:
    print(value)


# Test the contains method

# Print to make sure it works
print()
print("Printing")
print(100 in lst)


# Test the count method

# Insert a duplicate value
lst.insert(100)

# Test the count method
print()
print("Printing")
print(lst.count(100))


# Test the find method

# Find 100
print()
print("Printing")
print(lst.find(100))


# Test the __getitem__ method

# Print the 3rd item in the list
print()
print("Printing")
print(lst[2])


# Test the index method

# Print the results
print()
print("Printing")
print(lst.index(100))


# Test the intersection method

# Create an empty list
lst2 = Sorted_List()

# Add values
lst2.insert(100)

lst2.insert(1000)

# Create another empty list
lst3 = Sorted_List()

# Use the intersection method
lst3.intersection(lst, lst2)

# Print the results
print()
print("Printing")
for value in lst3:
    print(value)


# Test the is_identical method

# Print the results
print()
print("Printing")
print(lst.is_identical(lst2))


# Test the max method

# Print the results
print()
print("Printing")
print(lst2.max())


# Test the min method

# Print the results
print()
print("Printing")
print(lst2.min())


# Test the peek method

# Print the results
print()
print("Printing")
print(lst.peek())


# Test the remove method

# Use the remove method
lst2.remove(100)

# Print the results
print()
print("Printing")
for value in lst2:
    print(value)


# Test the remove front method

# Use the remove front method
lst.remove_front()

# Print the results
print()
print("Printing")
for value in lst:
    print(value)


# Test the remove many method method

# Create an empty list
lst4 = Sorted_List()

# Insert values
lst4.insert(11)

lst4.insert(22)

lst4.insert(22)

lst4.remove_many(22)

# Print the results
print()
print("Printing")
for value in lst4:
    print(value)


# Test the split method

# Insert values
lst4.insert(1000)

lst4.insert(100)

# Use the method
target1, target2 = lst4.split()

# Print target1
print()
print("Printing")
for value in target1:
    print(value)

# Print target2
print()
print("Printing")
for value in target2:
    print(value)


# Test the split_alt method

# Insert values
target1.insert(1000)

target1.insert(100000)

# Use the split_alt method
target3, target4 = target1.split_alt()

# Print the target3
print()
print("Printing")
for value in target3:
    print(value)

# Print the target4
print()
print("Printing")
for value in target4:
    print(value)


# Test the split_key method

# Insert values
target3.insert(100)

target3.insert(100000)

# Use the split_key method
target5, target6 = target3.split_key(10000)

# Print the target5
print()
print("Printing")
for value in target5:
    print(value)

# Print the target6
print()
print("Printing")
for value in target6:
    print(value)


# Test the union method

# Use the union method
target3.union(target5, target6)

# Print the target3
print()
print("Printing")
for value in target3:
    print(value)

