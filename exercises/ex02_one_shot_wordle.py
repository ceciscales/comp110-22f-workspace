"""EX02 - One-Shot Wordle!"""

__author__ = "730396639"

#Creating the wordle
secret_word: str= "python"

#Making sure that the guess has sufficient characters
guess: str= input(f"What is your 6-letter guess? ")
while len(guess) != len(secret_word):
    guess: str= input(f"That was not 6 letters! Try again: ")

#Labelling variables for each box color
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

#Letter 1
if guess[0] == (secret_word)[0]:
   a=(GREEN_BOX)
elif guess[0] == (secret_word)[1]:
    a= (YELLOW_BOX)
elif guess[0] == (secret_word)[2]:
    a= (YELLOW_BOX)
elif guess[0] == (secret_word)[3]:
    a= (YELLOW_BOX)
elif guess[0] == (secret_word)[4]:
    a= (YELLOW_BOX)
elif guess[0] == (secret_word)[5]:
    a= (YELLOW_BOX)
else: a= (WHITE_BOX)

#Letter 2
if guess[1] == (secret_word)[1]:
    b=(GREEN_BOX)
elif guess[1] == (secret_word)[0]:
    b= (YELLOW_BOX)
elif guess[1] == (secret_word)[2]:
    b= (YELLOW_BOX)
elif guess[1] == (secret_word)[3]:
    b= (YELLOW_BOX)
elif guess[1] == (secret_word)[4]:
    b= (YELLOW_BOX)
elif guess[1] == (secret_word)[5]:
    b= (YELLOW_BOX)
else: b=(WHITE_BOX)

#Letter 3
if guess[2] == (secret_word)[2]:
    c=(GREEN_BOX)
elif guess[2] == (secret_word)[0]:
    c= (YELLOW_BOX)
elif guess[2] == (secret_word)[1]:
    c= (YELLOW_BOX)
elif guess[2] == (secret_word)[3]:
    c= (YELLOW_BOX)
elif guess[2] == (secret_word)[4]:
    c= (YELLOW_BOX)
elif guess[2] == (secret_word)[5]:
    c= (YELLOW_BOX)
else: c=(WHITE_BOX)

#Letter 4
if guess[3] == (secret_word)[3]:
    d=(GREEN_BOX)
elif guess[3] == (secret_word)[0]:
    d= (YELLOW_BOX)
elif guess[3] == (secret_word)[1]:
    d= (YELLOW_BOX)
elif guess[3] == (secret_word)[2]:
    d= (YELLOW_BOX)
elif guess[3] == (secret_word)[4]:
    d= (YELLOW_BOX)
elif guess[3] == (secret_word)[5]:
    d= (YELLOW_BOX)
else: d=(WHITE_BOX)

#Letter 5
if guess[4] == (secret_word)[4]:
    e=(GREEN_BOX)
elif guess[4] == (secret_word)[0]:
    e= (YELLOW_BOX)
elif guess[4] == (secret_word)[1]:
    e= (YELLOW_BOX)
elif guess[4] == (secret_word)[2]:
    e= (YELLOW_BOX)
elif guess[4] == (secret_word)[3]:
    e= (YELLOW_BOX)
elif guess[4] == (secret_word)[5]:
    e= (YELLOW_BOX)
else: e=(WHITE_BOX)

#Letter 6
if guess[5] == (secret_word)[5]:
    f=(GREEN_BOX)
elif guess[5] == (secret_word)[0]:
    f= (YELLOW_BOX)
elif guess[5] == (secret_word)[1]:
    f= (YELLOW_BOX)
elif guess[5] == (secret_word)[2]:
    f= (YELLOW_BOX)
elif guess[5] == (secret_word)[3]:
    f= (YELLOW_BOX)
elif guess[5] == (secret_word)[4]:
    f= (YELLOW_BOX)
else: f=(WHITE_BOX)

#Printing the wordle boxes
print(f"{a}{b}{c}{d}{e}{f}")


#Did you get the secret word right?
while len(guess) == len(secret_word):
    if guess == secret_word:
        exit(print(f"Woo! You got it! "))
    if guess != secret_word:
        exit(f"Not quite. Play again soon!")

