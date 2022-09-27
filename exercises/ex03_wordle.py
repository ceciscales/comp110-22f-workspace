"""Structured Wordle!"""

__author__ = "730396639"


def contains_char(wordle: str, single_character: str) -> bool:
    """Given the single character is in the given string, the function returns a boolean statement."""
    assert len(single_character) == 1
    index: int = 0
    result: bool = False
    while index < len(wordle):   
        if single_character == wordle[index]:
            result = True
        index += 1
    return result


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess: str, secret: str) -> str:
    """Given a guess, colors corresponding to the correctness of the guess will appear."""
    assert len(guess) == len(secret)
    z: str = ""
    a: int = 0
    while a < len(secret):
        if contains_char(secret, guess[a]) is True:
            if guess[a] == secret[a]:
                z += GREEN_BOX
            else: 
                z += YELLOW_BOX
        else: 
            z += WHITE_BOX
        a += 1
    return z


def input_guess(expected_length: int) -> str:
    """The inputted guess should not exceed an expected length."""
    user_guess: str = input(f"Enter a {expected_length} character word: ")
    while expected_length != len(user_guess):
        user_guess = input(f"That wasn't {expected_length} chars! Try again: ")
    if expected_length == len(user_guess):
        return (user_guess)
    else:
        return ""


def main() -> None:
    """The entrypoint of the program and main game loop."""
    turns: int = 1
    secret_word: str = "codes"
    win: bool = False
    while turns <= 6 and win is False:
        print(f"=== Turn {turns}/6 ===")
        guess: str = input_guess(len(secret_word))
        boxes: str = emojified(guess, secret_word)
        print(boxes)
        if guess == secret_word:
            win = True
            print(f"You won in {turns}/6 turns!")
        if win is False:       
            turns += 1
    if turns == 7:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()