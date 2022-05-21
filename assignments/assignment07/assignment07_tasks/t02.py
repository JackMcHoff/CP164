"""
------------------------------------------------------------------------
CP164 Assignment 07, Task 02
------------------------------------------------------------------------
Author: Your Full Name
ID:     190401010
Email:  name1010@mylaurier.ca
__updated__ = "2022-03-10"
------------------------------------------------------------------------
"""
from Food_utilities import read_foods
from Sorted_List_linked import Sorted_List


file = open("food.txt", "rt")

foods = read_foods(file)

file.close()

sl = Sorted_List()

for value in foods:
    sl.insert(value)

sl.insert(foods[10])

print("Printing count of each item: ")
print(f"Name                                Count")
print(f"---------------------------------   -----")
for value in sl:
    print(f"{value.name:35} {sl.count(value):>5}")

sl.clean()

print("Printing count of each item: ")
print(f"Name                                Count")
print(f"---------------------------------   -----")
for value in sl:
    print(f"{value.name:35} {sl.count(value):>5}")

print()
print(f"{foods[-4].name} in sl?: ")
print(foods[-4] in sl)

print()
print(f"Index of {foods[-4].name}: ")
print(sl.index(foods[-4]))

print()
print(f"{foods[-4].name} from sl: ")
print(sl.find(foods[-4]))

print()
print(f"Second item in sl: ")
print(sl[1])

print()
print(f"First item in sl: ")
print(sl.peek())

print()
print(f"Min value in sl: ")
print(sl.min())

print()
print(f"Max value in sl: ")
print(sl.max())

print()
print(f"Remove first value in sl: ")
print(sl.remove_front())

print()
print(f"Remove {foods[-4].name} from sl: ")
print(sl.remove(foods[-4]))

sl2 = Sorted_List()

sl3 = Sorted_List()

for value in range(10):
    sl2.insert(foods[value])

sl3.intersection(sl, sl2)

print()
print("Printing count of each item in sl3: ")
print(f"Name                                Count")
print(f"---------------------------------   -----")
for value in sl3:
    print(f"{value.name:35} {sl3.count(value):>5}")

print()
print("sl2 and sl3 are identical?: ")
print(sl2.is_identical(sl3))

sl4 = Sorted_List()

sl4.union(sl2, sl3)

print()
print("Printing count of each item in sl4: ")
print(f"Name                                Count")
print(f"---------------------------------   -----")
for value in sl4:
    print(f"{value.name:35} {sl4.count(value):>5}")
