"""Dictionary Functions!!!"""

__author__ = "730396639"


def invert(given: dict[str, str]) -> dict[str, str]:
    """Given two strings, function will return the inverted keys and values."""
    inverted: dict[str, str] = {}
    
    values: dict[str, int] = {}
    for key in given:
        if key in values:
            values[key] += 1

    if values[key] > 1:
        inverted == KeyError("invert[] results in repeating keys ")
    
    for key in given:
        new_key: str = given[key]
        inverted[new_key] = key
    return inverted
    
        
def favorite_color(a: dict[str, str]) -> str:
    """Given two a dictionary of names and associated favorite color, function will return the most popular favorite color."""
    counter_1: int = 0
    counter_2: int = 0 
    best_color: str = ""
    for key in a:
        for key2 in a:
            if a[key] == a[key2]:
                counter_1 += 1
        if counter_1 > counter_2:
            best_color = a[key]
            counter_2 = counter_1
            counter_1 = 0
    return best_color


def count(a: list[str]) -> dict[str, int]:
    """Given a list of strings, the function will count how many times the str is in the list."""
    values: dict[str, int] = {}
    for key in a:
        if key in values:
            values[key] += 1
        else:
            values[key] = 1
    return values