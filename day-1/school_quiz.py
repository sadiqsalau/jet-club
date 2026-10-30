# =====================================================
#  ACES SCHOOL QUIZ
#  Change the parts marked ✏️, then press F5 to play.
# =====================================================


# ✏️ 1. The name of your quiz
QUIZ_NAME = "ACES School Quiz"


# ✏️ 2. Your questions
#    Each line is: ["question", "answer"]
#    Replace each ANSWER with the right answer.
#    Add more accepted answers after the first one:
#    ["question", "answer", "another answer"]
QUESTIONS = [
    ["What is our school's motto?", "ANSWER"],
    ["What is the name of our principal?", "ANSWER"],
    ["What sport can we play on our mini pitch?", "ANSWER"],
]


# ✏️ 3. Your messages
PERFECT_MESSAGE = "Perfect score! You're a genius!"
GOOD_MESSAGE = "Well done! Play again to get them all."
TRY_AGAIN_MESSAGE = "Keep learning, and try again!"


# ✏️ 4. Mix up the question order? (True or False)
SHUFFLE = True


# -----------------------------------------------------
#  THE GAME
#  You don't need to change anything below this line,
#  but you can read it to see how it works.
# -----------------------------------------------------

# Borrow the "random" tools, used to mix up the questions
import random


# A function is a named set of steps we can use again and again
def ask(question):
    """Asks one question and returns True if the answer is right."""
    # The question is the first item in the line (Python counts from 0)
    text = question[0]

    # Every item after it is an accepted answer, in small letters
    accepted = [answer.lower() for answer in question[1:]]

    # Ask, then tidy the reply: remove extra spaces and use small letters
    reply = input(text + " ").strip().lower()

    # Is the reply one of the accepted answers?
    if reply in accepted:
        print("✅ Correct!")
        return True

    # Wrong: show the first answer
    print("❌ Not quite. The answer is " + question[1] + ".")
    return False


def play(name):
    """Plays one round and returns the score."""
    # Make a copy of the questions, and mix it up if SHUFFLE is True
    questions = list(QUESTIONS)
    if SHUFFLE:
        random.shuffle(questions)

    # Start with no points
    score = 0

    # Repeat for every question, numbering them from 1
    for number, question in enumerate(questions, start=1):
        print()
        print("Question " + str(number) + " of " + str(len(questions)))

        # One point for each right answer
        if ask(question):
            score = score + 1

    # Show the final score; str() turns a number into text
    total = len(questions)
    print()
    print(name + ", you scored " + str(score) + " out of " + str(total) + "!")

    # Pick a message: all right, at least half right, or less
    if score == total:
        print(PERFECT_MESSAGE)
    elif score >= total / 2:
        print(GOOD_MESSAGE)
    else:
        print(TRY_AGAIN_MESSAGE)

    return score


# The game starts here
print("Welcome to the " + QUIZ_NAME + "!")
player = input("What is your name? ").strip()

# Keep playing rounds until the player says no
while True:
    play(player)
    again = input("\nPlay again? (yes/no) ").strip().lower()

    # break stops the loop
    if again not in ["yes", "y"]:
        break

print("Thanks for playing, " + player + "! 👋")
