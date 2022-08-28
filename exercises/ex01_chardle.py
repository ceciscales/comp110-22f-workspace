"""EX01 - Chardle - A cute step toward Wordle!"""


__author__ = "730396639"


wordle_word: str = input("Enter a 5-character word: ")

if len(wordle_word) != 5:
    exit(print("Error: Word must contain 5 characters "))  

single_character: str = input("Enter a single character: ")

if len(single_character) != 1:
    exit(print("Error: Character must be a single character. "))  

print("Searching for " + single_character + " in " + wordle_word)  

if single_character == (wordle_word)[0]:
    print(single_character + " found at index 0 ")

if single_character == (wordle_word)[1]:
    print(single_character + " found at index 1 ")

if single_character == (wordle_word)[2]:
    print(single_character + " found at index 2 ")

if single_character == (wordle_word)[3]:
    print(single_character + " found at index 3 ")   

if single_character == (wordle_word)[4]:
    print(single_character + " found at index 4 ") 


total_count: int = 0
if single_character == (wordle_word)[0]:
    total_count = total_count + 1

if single_character == (wordle_word)[1]:
    total_count = total_count + 1

if single_character == (wordle_word)[2]:
    total_count = total_count + 1

if single_character == (wordle_word)[3]:
    total_count = total_count + 1

if single_character == (wordle_word)[4]:
    total_count = total_count + 1 

if int(total_count) == int(0):
    print(("No instances of " + single_character + " found in " + wordle_word))

if int(total_count) == int(1):
    print(("1 instance of " + single_character + " found in " + wordle_word))

if int(total_count) >= int(2):
    print((str(total_count)) + " instances of " + single_character + " found in " + wordle_word)