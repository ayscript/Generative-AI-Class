# Python dictionaries
# A dictionary is a collection of key value pairs
# Keys are unique and used to store and retrieve values.
# Values can be any data type (string, integer, list, tuple, even other dictionaries)

# Syntax
# dictionary_name = {key1: "value1", key2: "value2"}

# Creating Dictionaries
#    1. Using curly braces
student = {
    "name": "Ada",
    "age": 20,
    "course": "Computer Science"
}
print(student)

#    2. using dict() constructor
student_info = dict(name="john", age=25, course="Maths")
print(student_info)

#    3. Empty dictionary
empty_dict = {}
print(empty_dict)

# 4. Dictionary Comperehension
# syntax: {key_expression: value-expression for item in iteratable if conditioon}
# Example: Create a dictionary of numbers and their sequence
squares = {x: x**2 for x in range(1,6)}
print(squares)

# With conditions
# Dictionaries of even numbers and their cubes
even_cubes = {x: x**3 for x in range(1,10) if x % 2 == 0}
print(even_cubes)