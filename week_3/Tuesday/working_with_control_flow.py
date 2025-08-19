# Control flow in python
# 1. if Statement
age = 20
if age >= 18:
    print("You are eligible to vote")

# Some usecases
#  Checking for eligibility
#  Validating login attempts
#  Ensuring a minimum purchase requirement, etc

# 2. if-else Statement
# Provides two alternative paths
wallet = 400
price = 500

if wallet >= price:
    print("Purchase successful")
else:
    print("Insufficient balance")

# Some usecases
#  Deciding success or failure of a payment
#  Granting or denying access to a system
#  Determining pass/fail in an exam, etc

# 3. if-elif-else Statement
# Used for multiple conditions
score = 85
if score >= 70:
    print("Grade A")
elif score >= 50:
    print("Grade B")
else:
    print("Grade C")

# Some use cases
# Student grading systems
# Assigning ticket categories (VIP, Regular, Student)
# Categorizing temperatures (Hot, Warm, Cold), etc.

# 4. Nested if
# Placing an if inside another if
age = 19
citizen = True

if age >= 18:
    if citizen:
        print("You can vote")
    else:
        print("You must be a citizen to vote")
else:
    print("Too young to vote")

# B. Loops

# 1. for loop
# This is used for iterating over a sequence (strings, list, tuple, dictionary)

# Iterate through each element in a LIST

fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"I like {fruit}")

# Iterate through each element in a TUPLE

coordinates = (0.34654, -0.48585, 0.57477)
for point in coordinates:
    print(F"Point: {point}")

# Iterate through each element in a DICTIONARY

student = {"name": "Tunde", "age": 16, "grade": "A"}
for key, value in student.items():
    print(f"{key}: {value}")

# Iterate through each element in a STRING.
word = "PYTHON"

for char in word:
    print(char)

# 2. while loop
# while condition:
    # code block
    
# using while loop
count = 1
while count <= 5:
    print(count)
    count += 1
    
# Incrementing with 'while'
num = 1
while num <= 10:
    print(num, end=" ")
    num += 1
    
# Decrement with `while`
timer = 10
while timer > 0:
    print("Countdown:", timer)
    timer -= 1
    
# While with user input
# keep asking until the user enters a correct password

password = ""
while password != "python123":
    password = input("Enter the password: ")

print("Access Granted!")