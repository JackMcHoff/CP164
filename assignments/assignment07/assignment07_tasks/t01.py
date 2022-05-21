"""
------------------------------------------------------------------------
CP164 Assignment 07, Task 01
------------------------------------------------------------------------
Author: Your Full Name
ID:     190401010
Email:  name1010@mylaurier.ca
__updated__ = "2022-03-10"
------------------------------------------------------------------------
"""
from Food_utilities import read_foods
from List_linked import List

file = open("food.txt", "rt")

foods = read_foods(file)

file.close()

lst = List()

for value in foods:
    lst.append(value)

print("Printing the first item: ")
print(lst[0])

lst.prepend(foods[10])

print()
print("Printing first item: ")
print(lst[0])


print()
print("Printing count of each item: ")
print(f"Name                                Count")
print(f"---------------------------------   -----")
for value in lst:
    print(f"{value.name:35} {lst.count(value):>5}")

lst.clean()

print()
print("Printing count of each item: ")
for value in lst:
    print(f"{value.name:35} {lst.count(value):>5}")

lst2 = List()

lst3 = List()

for value in range(10):
    lst2.append(foods[value])

lst3.combine(lst, lst2)

print()
print("Printing count of each item in lst3: ")
print(f"Name                                Count")
print(f"---------------------------------   -----")
for value in lst3:
    print(f"{value.name:35} {lst3.count(value):>5}")


for value in range(20, 26):
    lst.append(foods[value])

lst2.intersection(lst, lst3)

print()
print("Printing count of each item in lst2: ")
print(f"Name                                Count")
print(f"---------------------------------   -----")
for value in lst2:
    print(f"{value.name:35} {lst2.count(value):>5}")


print()
print("lst1 and lst2 are identical?: ")
print(lst.is_identical(lst2))

print()
print("Printing the removed value: ")
print(lst.remove_front())


print()
print("Printing count of each item in lst3: ")
print(f"Name                                Count")
print(f"---------------------------------   -----")
for value in lst3:
    print(f"{value.name:35} {lst3.count(value):>5}")


lst3.remove_many(foods[0])

print()
print("Printing count of each item in lst3: ")
print(f"Name                                Count")
print(f"---------------------------------   -----")
for value in lst3:
    print(f"{value.name:35} {lst3.count(value):>5}")

target1, target2 = lst3.split()

print()
print("Printing count of each item in target1: ")
print(f"Name                                Count")
print(f"---------------------------------   -----")
for value in target1:
    print(f"{value.name:35} {target1.count(value):>5}")

print()
print("Printing count of each item in target2: ")
print(f"Name                                Count")
print(f"---------------------------------   -----")
for value in target2:
    print(f"{value.name:35} {target2.count(value):>5}")

target3, target4 = target1.split_alt()

print()
print("Printing count of each item in target3: ")
print(f"Name                                Count")
print(f"---------------------------------   -----")
for value in target3:
    print(f"{value.name:35} {target3.count(value):>5}")

print()
print("Printing count of each item in target4: ")
print(f"Name                                Count")
print(f"---------------------------------   -----")
for value in target4:
    print(f"{value.name:35} {target4.count(value):>5}")

lst3.union(target3, target4)

print()
print("Printing count of each item in lst3: ")
print(f"Name                                Count")
print(f"---------------------------------   -----")
for value in lst3:
    print(f"{value.name:35} {lst3.count(value):>5}")
