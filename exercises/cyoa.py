"""How many pieces of candy can you get this Halloween?"""

__author__ = "730396639"

PUMPKIN: str = "\U0001F383"

points: int = 0
player: str = ""
outcome: str = (f"You have recieved {points} pieces of candy tonight! ")
gamble: int = 0


def main() -> None:
    """Choosing where you will trick or treat this Halloween!"""
    global points
    global replay
    global outcome
# Adventure points
    if player == "":
        greet()
    print(f"Hey {player}, where do you want to go trick or treating?")
    print("a. college campus")
    print("b. Wanda's lair")
    print("c. I don't want to trick or treat. I am done.")
    location: str = input("Enter the letter answer ")
    if location == "a" or location == "A":
        print("")
        print("Here we go!")
        print("")
        college()
    if location == "b" or location == "B":
        print("")
        print("Here we go!")
        print("")
        wanda_instructions()    
    if location == "c" or location == "C":  
        print(f"You have recieved {points} pieces of candy tonight! ") 
        print("Goodbye!")
        quit()


def greet() -> None:
    """Hey! How are you? Here's a greeting in order to explain the game and ask for a name."""
    global player
    print("Hey you!")
    print(f"We've heard that you are a Halloween {PUMPKIN} expert and we want to learn your ways.")
    print("Play this game to see how many pieces of candy you can get before the end of the night!")
    print("Keep in mind, you have access to a time machine and will be able to try all options before deciding to exit the game. ") 
    player = input("Before we begin, what is your name? ")


def college() -> None:
    """How much candy will you get while trick or treating on a college campus?"""
    global points
    global outcome
    print(f"Welcome to UNC's campus {player}! ")
    print("")
    print("Choose a costume! You will receive candy based on the quality of this costume.")
    print(" a. Minion ")
    print(" b. Gru ")
    print(" c. Perry the Platypus ")
    print(" d. Duke student")
    costume: str = input("Which one? ")
    if costume == "a" or costume == "A":
        points += 10
    if costume == "b" or costume == "B":
        points += 15
    if costume == "c" or costume == "C":
        points += 20
    if costume == "d" or costume == "D":
        print("Wrong choice. Only one pity candy for you!")
        points += 1
    print("")
    print(f"{player}, you have received {points} candies for choosing this costume.")
    print(" Which dorm will you choose to trick or treat in? ")
    print(" a. Morrison ")
    print(" b. Granville ")
    print(" c. Hojo ")
    dorm_choice: str = input("Which one? ")
    if dorm_choice == "a" or dorm_choice == "A":
        points += 30
    if dorm_choice == "b" or dorm_choice == "B":
        points += 10
    if dorm_choice == "c" or dorm_choice == "C":
        points += 25
    print(f"Okay {player}! You have {points} candies")    
    replay: str = input("Do you want to go in the time machine? Type 'Yes' if Yes and 'No' if you want to end the game: ")
    if replay == "Yes" or replay == "yes":
        main()
    else:
        print(f"You have recieved {points} pieces of candy tonight! ")


def wanda_instructions() -> int:
    """The instructions for Wanda's magic! Here, you determine your wager (integer) for Wanda."""
    global player
    global gamble
    print(f"{player}, you have chosen to enter Wanda's lair. ")
    print("Wanda loves multiplying candy. She cannot give you new candy, she can only multiply it.")
    print("Unfortunately, due to a curse, her magic only works 80% of the time on Halloween.")
    print("You can ask Wanda for her magical candy as many times as you'd like and you don't have to gamble all of it, but there is a chance that her magic goes wrong.")
    print("If her magic goes wrong, you can end up with zero candies!")
    print(f"You currently have {points} pieces of candy. ")
    print("Do you dare ask Wanda for candy?")
    play: str = input("Type 'yes' or 'no' ")
    if play == "No" or play == "no" or play == "nO":
        main()
    if play == "Yes" or play == "yes":
        y = int(input("How many of your candies would you like to wager? "))
        gamble = y
        int(gamble)
        magic(gamble)  
    return points


def magic(x: int) -> int:
    """Wanda's magic! Risking candy for a potential multiplier!"""
    global points
    from random import randint
    while int(x) > int(points):
        x = int(input("You don't have that many candies! Try again: "))
    wanda: int = randint(0, 4)
    points += (int(wanda) * int(x)) - x
    print(f"Wanda has multiplied your candy by {wanda}! You now have {points} candies!")
    replay: str = input("Do you want to go in the time machine? Type 'Yes' if Yes and 'No' if you want to end the game: ")
    if replay == "Yes" or replay == "yes":
        main()
    return points


if __name__ == "__main__":
    main()    