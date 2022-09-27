"""My own, original list utility function!"""


__author__ = "730396639"


def all(given_list: list[int], given: int) -> bool:
    """Function determines whether all the numbers in a given list is the same as the given number!"""
    i: int = 0
    x: int = 0
    if given_list == []:
        return False
    while i < (len(given_list)):
        if given_list[i] != given:
            x += 1
        i += 1
    if x > 0:
        return False
    else: 
        return True


def max(input: list[int]) -> int:
    """Function determines the maximum number from a list!"""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    if len(input) == 1:
        return input[0]
    while len(input) >= 2:
        if input[0] >= input[1]:
            input.pop(1)
        else:
            input.pop(0)
    return input[0]


def is_equal(numbers_1: list[int], numbers_2: list[int]) -> bool:
    """Function determines whether or not two lists are deeply equal."""
    a: int = 0
    b: int = 0
    c: int = 0
    if len(numbers_1) == len(numbers_2):
        while c < len(numbers_1):
            if numbers_1[a] != numbers_2[a]:
                b += 1
            a += 1
            c += 1
    else: 
        return False
    if b == 0:
        return True
    else: 
        return False