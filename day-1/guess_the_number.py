# Guess the number
# The computer picks a secret number, and you try to guess it.

# Borrow the "random" tools that other programmers already built
import random

# Pick a secret number from 1 to 20
secret = random.randint(1, 20)
print("I'm thinking of a number between 1 and 20.")

# Start with a guess that can't be right, so the loop runs at least once
guess = 0

# Keep asking until the guess is right (!= means "is not equal to")
while guess != secret:
    guess = int(input("Your guess: "))

    # Give a hint
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")

# The loop has ended, so the guess must be right
print("You got it! The number was", secret)
