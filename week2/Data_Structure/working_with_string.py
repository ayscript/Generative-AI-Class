# String data type

# Single quotes
name = 'ada'

# Triple quoites (for multi-line strrings)
story = '''Once upon a time
there was a coder named Ada'''

print(story)

# String operation
word = "Python is a programming language"

print(word[0])
print(word[-2])

# Slicing

word = "python"
print(word[0:4])

print(word[2:])

print(word[:3])

print(word[::2]) # Print and skip every second step

print(word[::-1]) # print in reverse

# String concatenation & repitition
# Concatenation
a = "Hello"
b = "World"
print(a + " " + b) # Hello World

# Repeatition
word = "Hi! "
print(word * 3) # Hi! Hi! Hi!

# String searching and checking

# Membership
text = "Python programming"
print("Python" in text)
print("Java" not in text)

# find() / rfind()
text = "Hello World"
print(text.find("world")) # Counts from the front
print(text.rfind("o")) # Counts from the back

# index() / rindex()

text = "Hello World"
print(text.index("World"))   # 6

# startswith() / ends
