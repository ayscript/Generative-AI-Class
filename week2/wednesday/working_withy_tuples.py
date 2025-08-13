# A tuple is an ordered, immutable (unchangeable) collection of items in python

# Creating Tuples
# Using parenthesis ()
fruits = ("apple", "banana", "cherry")
print(fruits)

# without parenthesis (tuple packing)
numbers = 1, 2, 3
print(numbers)

# single item tuple (must include a comma)
single_item = ("apple",)
print(single_item)

# using the tuple() constructor
fruits_list = ["apple", "banana", "cherry"]
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)

# Characters of tuples
# 1. Ordered - Items have a fixed position
colors = ("red", "green", "blue")
print(colors[0])

# 2. Immutable - Cannot change after creation
# colors[1] = "yellow"  type error

# 3. Allow duplicates
numbers = (1,2,2,3)
print(numbers)

# 4. Can contain mixed data types
mixed = ("apple", 3, True, 5.6)
print(mixed)

# 5. Can be nested
nested = (("a", "b"), (1,2))
print(nested)


# Tuple Operations
# 1. Indexing
fruits = ("apple", "banana", "cherry")
print(fruits[1])
print(fruits[-1])

# 2. Slicing
print(fruits[0:2])
print(fruits[::-1])

# 3. Concatenation
tuple1 = (1,2)
tuple2 = (3,4)
result = tuple1 + tuple2
print(result)

# 4. Repetition
nums = (1,2)
print(nums * 3)

# 5. Membership
fruits = ("apple", "banana", "cherry")
print("banana" in fruits)
print("grape" not in fruits)

# 6. iteration
for fruit in fruits:
        print(fruit)

# working with tuples
# 1. Unpacking tuples
person = (1, 2, 2, 3, 4)