# Question 1
userName = input("Enter your name: ")
print(userName.upper())

# Question 2
print("python"[0],"python"[-1])

# Question 3
name = input("Enter your name: ")
print(f"Hello, {name}!")

# Question 4
character = input("Enter a character: ")
characterLength = character.find(character[-1]) + 1
print(characterLength)

# Question 5
word = "Hello World"
word = word.replace("World", "Python")
print(word)