"""EX02 - One-Shot Wordle!"""

__author__ = "730396639"

    # Creating the wordle
SECRET_WORD: str= "python"

    # Making sure that the guess has sufficient characters
GUESS: str= input(f"What is your 6-letter guess? ")
while len(GUESS) != len(SECRET_WORD):
    GUESS = input(f"That was not 6 letters! Try again: ")

    # Labelling variables for each box color
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

    # Letter 1
if GUESS[0] == (SECRET_WORD)[0]:
   a=(GREEN_BOX)
elif GUESS[0] == (SECRET_WORD)[1]:
    a= (YELLOW_BOX)
elif GUESS[0] == (SECRET_WORD)[2]:
    a= (YELLOW_BOX)
elif GUESS[0] == (SECRET_WORD)[3]:
    a= (YELLOW_BOX)
elif GUESS[0] == (SECRET_WORD)[4]:
    a= (YELLOW_BOX)
elif GUESS[0] == (SECRET_WORD)[5]:
    a= (YELLOW_BOX)
else: a= (WHITE_BOX)

    # Letter 2
if GUESS[1] == (SECRET_WORD)[1]:
    b=(GREEN_BOX)
elif GUESS[1] == (SECRET_WORD)[0]:
    b= (YELLOW_BOX)
elif GUESS[1] == (SECRET_WORD)[2]:
    b= (YELLOW_BOX)
elif GUESS[1] == (SECRET_WORD)[3]:
    b= (YELLOW_BOX)
elif GUESS[1] == (SECRET_WORD)[4]:
    b= (YELLOW_BOX)
elif GUESS[1] == (SECRET_WORD)[5]:
    b= (YELLOW_BOX)
else: b=(WHITE_BOX)

    # Letter 3
if GUESS[2] == (SECRET_WORD)[2]:
    c=(GREEN_BOX)
elif GUESS[2] == (SECRET_WORD)[0]:
    c= (YELLOW_BOX)
elif GUESS[2] == (SECRET_WORD)[1]:
    c= (YELLOW_BOX)
elif GUESS[2] == (SECRET_WORD)[3]:
    c= (YELLOW_BOX)
elif GUESS[2] == (SECRET_WORD)[4]:
    c= (YELLOW_BOX)
elif GUESS[2] == (SECRET_WORD)[5]:
    c= (YELLOW_BOX)
else: c=(WHITE_BOX)

    # Letter 4
if GUESS[3] == (SECRET_WORD)[3]:
    d=(GREEN_BOX)
elif GUESS[3] == (SECRET_WORD)[0]:
    d= (YELLOW_BOX)
elif GUESS[3] == (SECRET_WORD)[1]:
    d= (YELLOW_BOX)
elif GUESS[3] == (SECRET_WORD)[2]:
    d= (YELLOW_BOX)
elif GUESS[3] == (SECRET_WORD)[4]:
    d= (YELLOW_BOX)
elif GUESS[3] == (SECRET_WORD)[5]:
    d= (YELLOW_BOX)
else: d=(WHITE_BOX)

    # Letter 5
if GUESS[4] == (SECRET_WORD)[4]:
    e=(GREEN_BOX)
elif GUESS[4] == (SECRET_WORD)[0]:
    e= (YELLOW_BOX)
elif GUESS[4] == (SECRET_WORD)[1]:
    e= (YELLOW_BOX)
elif GUESS[4] == (SECRET_WORD)[2]:
    e= (YELLOW_BOX)
elif GUESS[4] == (SECRET_WORD)[3]:
    e= (YELLOW_BOX)
elif GUESS[4] == (SECRET_WORD)[5]:
    e= (YELLOW_BOX)
else: e=(WHITE_BOX)

    # Letter 6
if GUESS[5] == (SECRET_WORD)[5]:
    f=(GREEN_BOX)
elif GUESS[5] == (SECRET_WORD)[0]:
    f= (YELLOW_BOX)
elif GUESS[5] == (SECRET_WORD)[1]:
    f= (YELLOW_BOX)
elif GUESS[5] == (SECRET_WORD)[2]:
    f= (YELLOW_BOX)
elif GUESS[5] == (SECRET_WORD)[3]:
    f= (YELLOW_BOX)
elif GUESS[5] == (SECRET_WORD)[4]:
    f= (YELLOW_BOX)
else: f=(WHITE_BOX)

    # Printing the wordle boxes
print(f"{a}{b}{c}{d}{e}{f}")


    # Did you get the secret word right?
while len(GUESS) == len(SECRET_WORD):
    if GUESS == SECRET_WORD:
        exit(print(f"Woo! You got it! "))
    if GUESS != SECRET_WORD:
        exit(f"Not quite. Play again soon! ")