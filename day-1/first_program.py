# My first Python program
# Press F5 to run it. Lines starting with # are notes for humans; Python skips them.

# Ask for the player's name and keep it in a box (a variable) called "name"
name = input("What is your name? ")

# Ask for their age; int() turns the text "14" into the number 14
age = int(input("How old are you? "))

# Say hello; + joins pieces of text together
print("Hello, " + name + "!")

# Do some maths with the age
print("In 10 years, you will be", age + 10)

# Decide: this line only runs if the age is 13 or more
# The spaces before print show that it belongs to the if
if age >= 13:
    print("You're old enough to join JET Club!")
