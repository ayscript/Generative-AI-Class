# upper()

name = 'ada balogun'
print(name.upper())

# lower()
name = 'ADA BALOGUN'
print(name.lower())

# strip()
word = " Abuja "
print(word.strip())

# replace()
word = "I love java"
print(word.replace('java', 'python'))

# swapcase()
text = "Hello ABEOKUTA"
print(text.swapcase())

# lstrip() Removes whitespace (or specified characters) from the left side only.\
text = " Nigeria"
print(text.lstrip())

# rstrip() Removes whitespace (or specified characters) from the right side only.\
text = " Nigeria"
print(text.rstrip())

# split() Splits a string into a list using a separator (default is space).
fruits = "Mango Orange Banana"
print(fruits.split())

# rsplit() Splits a string into a list from the right side
text = "one,two,three,four"
print(text.rsplit(",", 2))

# splitlines() Splits a string into a list at each newline (\n)
lines = "Line 1\nLine 2\nLine 3"
print(lines.splitlines())

# join() Joins a list of strings into one string with a specified separator
words = ["I", "Love", "Python"]
print(" ".join(words))

# center() Centers a specified width, padding with spaces or characters
text = "Python"
print(text.center(20, "-"))

# ljust() Left align the string within a specified width, padding with spaces or characters.
text = "Python"
print(text.ljust(10, "*"))

# rjust() Left align the string within a specified width, padding with spaces or characters.
print(text.rjust(10, "*"))

# zfill() Pads a numeric string on the left with zeros until it reaches a given length
num = "42"
print(num.zfill(5))

# isalpha() Checks if the string contains only letters
print("Lagos".isalpha())
print("Lagos123".isalpha())

# isdigit() Checks if the string contains only digits
print("12345".isdigit())

# isalnum() Checks if the string contains only letters and digits
print("Python3".isalnum())
print("Python 3".isalnum())
