"""EX02 - One-Shot Wordle!"""

__author__ = "730396639"

# Creating the wordle word
secret_word: str = "python"

# Making sure that the guess has sufficient characters
word_length: int = len(secret_word)
guess: str = input(f"What is your {word_length}-letter guess? ")
while len(guess) != len(secret_word):
    guess = input(f"That was not {word_length} letters! Try again: ")

# Labelling variables for each box color
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

# Labelling my constants
a: str = ""
index: int = 0

# What color is the square?
while index < len(secret_word):
    if guess[index] == secret_word[index]:
        a += GREEN_BOX
    else:
        letter_exists: bool = False
        alternate_index: int = 0
        while letter_exists is False and alternate_index < len(secret_word):
            if secret_word[alternate_index] == guess[index]:
                letter_exists = True
            else: 
                alternate_index += 1
        if letter_exists is True:
            a += YELLOW_BOX
        else: 
            a += WHITE_BOX
    index += 1

# Printing the wordle boxes
print(f"{a}")

# Did you get the secret word right?
if guess == secret_word:
    (print(" Woo! You got it! "))
if guess != secret_word:
    (print(" Not quite. Play again soon! "))
SystemExit