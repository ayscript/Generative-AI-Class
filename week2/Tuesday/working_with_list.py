# Creating a list
# With Square brackets
empty_list = []
print(empty_list)

# Using the list() constructor
empty_list2 = list()
print(empty_list2)

# Creating a list with initial elements
# List of Integers
numbers = [1,2,3,4,5,6]
print(numbers)

# List of strings
fruits = ["apple", "banana", "cherry"]
print(fruits)

# Mixed data types
mixed_list = ["Alice", 25, 5.8, True]
print(mixed_list)

# Creating a list from another sequence. You can convert strings, tuples, or other iteratables into a list.

# From a string
char = list("Hello")
print(char)

# from a tuple
my_tuple = (10, 20, 30)
list_from_tuple = list(my_tuple)
print(list_from_tuple)

# from a range
numbers_range = list(range(5))
print(numbers_range)

# Creating a list using list comprehension
# Squares of numbers 0-4
squares = [x**2 for x in range(5)]
print(squares)

# Even numbers between 0 and 10
evens = [x for x in range(11) if x % 2 == 0]
print(evens)

# Nested list
# Matrix-like list
matrix = [[1,2], [3,4], [5,6]]
print(matrix)

# Accessing elements in a nested list
print(matrix[0])
print(matrix[0][1])

# List operation in Python
# Pytho list support a variety of operations for creating, modifying, and working with data.
# Concatenation (+)
# Joins two lists into new list
list1 = [1,2,3,4]
list2 = [5,6]
result = list1 + list2
print(result)

# Repetition
# Repeats elements in a list a given number of times
nums = [1,2]
repeated = nums * 3
print(repeated)

# Indexing
# Accessing element using their position
fruits = ["apple", "Banana", "Cherry"]
print(fruits[0])
print(fruits[-1])

# Slicing: Extract a portion of the list
numbers = [0,1,2,3,4,5]
print(numbers[1:4])
print(numbers[:3])

# Membership (in/not in) - Checks if an element exists in a list
colors = ["red", "green", "blue"]
print("green" in colors)
print("yellow" not in colors)

# Length (len()) - counts the number of elements in a list
items = ["pen", "book", "laptop"]
print(len(items))


# min and max (min() / max()) - returns the smallest or largest element

nums = [5,2,9,1]
print(min(nums))
print(max(nums))

# Sum (sum()) Adds all numerical elements in a list
numbers = [1,2,3,4]
print(sum(numbers))


