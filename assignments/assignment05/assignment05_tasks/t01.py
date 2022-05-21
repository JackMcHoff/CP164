"""
------------------------------------------------------------------------
CP164 Assignment 05, Task 01
------------------------------------------------------------------------
Author: Your Full Name
ID:     190401010
Email:  name1010@mylaurier.ca
__updated__ = "2022-02-10"
------------------------------------------------------------------------
"""
# Imports
from Food import Food
from Food_utilities import read_food, read_foods
from List_array import List
from utilities import array_to_list


# Prepare a List

# Open the food.txt file
file = open("food.txt", "rt")

# Use the read_foods method to get a list of foods
foods = read_foods(file)

# Close the file
file.close()

# Create an empty list
lst = List()

# Add all the food items into the list
array_to_list(lst, foods)


# Test the Append Method

# Create an extra food item
lasgna = Food("Lasagna", 7, False, 135)

# Use the append method
lst.append(lasgna)

# Get the names of all the food objects in the list
#   making sure append was successful
print("Printing...")
for value in lst:
    print(f"{value.name} = {lst.count(value)}")


# Test the clean method

# Use the clean method
lst.clean()

# Make sure it works by printing names and count
print()
print("Printing...")
for value in lst:
    print(f"{value.name} = {lst.count(value)}")


# Test the combine method

# Create an temporary list (Built-In)
temp = [
    read_food("Gulab Jamun|2|True|300"),
    read_food("Burrito|4|False|200")
]

# Create an empty list
lst2 = List()

# Append values to the empty list
lst2.append(temp[0])

lst2.append(temp[1])

# Create another empty list
lst3 = List()

# Combine lst and lst2 in lst3
lst3.combine(lst, lst2)

# Make sure it works by printing names
print()
print("Printing...")
for value in lst3:
    print(f"{value.name}")


# Test the __getitem__ method

# Print the 10th item in lst3
print()
print("Printing...")
print(lst3[10])


# Test the intersection method

# Add the values from temp into
#    the now empty lst2
lst2.append(temp[0])

lst2.append(temp[1])

# Create an empty list
lst4 = List()

# Use the intersection method using lst2 and lst3
lst4.intersection(lst2, lst3)

# Make sure it works by printing the names
print()
print("Printing...")
for value in lst4:
    print(f"{value.name}")


# Test the is_identical method

# Print the results of comparing lst4 to lst2
print()
print("Printing...")
print(lst4.is_identical(lst2))


# Test the prepend method

# Prepend the first food object from
#   temp into lst4
lst4.prepend(temp[0])

# Print the names to make sure it worked
print()
print("Printing...")
for value in lst4:
    print(f"{value.name}")


# Test the remove front method

# remove the first value in lst4
lst4.remove_front()

# Print the names to make sure it worked
print()
print("Printing...")
for value in lst4:
    print(f"{value.name}")


# Test the remove many method

# Append Gulab Jamun to lst4
lst4.append(temp[0])

# remove Gulab Jamun from lst4
lst4.remove_many(temp[0])

# Print the names to make sure it worked
print()
print("Printing...")
for value in lst4:
    print(f"{value.name}")


# Test the split method

# Use the split method
target1, target2 = lst3.split()

# Print the names in target1 to make sure it worked
print()
print("Printing...")
for value in target1:
    print(f"{value.name}")

# Print the names in target2 to make sure it worked
print()
print("Printing...")
for value in target2:
    print(f"{value.name}")


# Test the split alt method

# Use the split alt method
target3, target4 = target1.split_alt()

# Print the names in target3 to make sure it worked
print()
print("Printing...")
for value in target3:
    print(f"{value.name}")

# Print the names in target4 to make sure it worked
print()
print("Printing...")
for value in target4:
    print(f"{value.name}")


# Test the union method

# Use the union method
lst3.union(target3, target4)

# Print the names in lst3 to make sure it worked
print()
print("Printing...")
for value in lst3:
    print(f"{value.name}")
