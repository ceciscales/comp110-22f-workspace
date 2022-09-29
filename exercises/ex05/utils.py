"""My List Utility Function!"""


__author__ = "730396639"


def only_evens(input: list[int]) -> list[int]:
    """Given a list of numbers, function will return the even numbers."""
    even_list: list[int] = []
    a = 0
    while a < len(input):
        if input[a] % 2 == 0:
            even_list.append(input[a])
        a += 1
    return even_list


def concat(input_1: list[int], input_2: list[int]) -> list[int]:
    """Given two lists of numbers, the function will combine them into one."""
    result: list[int] = input_1 + input_2
    return result


def sub(given: list[int], start_index: int, end_index: int) -> list[int]:
    """Given a list and two indices, the function will return the list of numbers between the indices."""
    answer: list[int] = []
    if start_index < 0:
        start_index = 0
    if end_index > len(given):
        end_index = len(given)
    if len(given) == 0:
        return []
    if start_index > len(given):
        return []
    if end_index <= 0:
        return []

    z = start_index
    while z < (end_index):
        answer.append(given[z])
        z += 1
    return answer