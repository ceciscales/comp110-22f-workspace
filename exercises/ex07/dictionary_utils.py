"""Testing my dictionary functions!!!"""


__author__ = "730396639"


from exercises.ex07.dictionary import favorite_color, invert, count


def test_favorite_color_1() -> None:
    # edge case
    """Testing to see what occurs when there is an empty input."""
    assert favorite_color({}) == {}


def test_favorite_color_2() -> None:
    # use case
    """Does this work?"""
    assert favorite_color({"NCSU": "red", "UNC": "blue", "Duke": "blue"}) == "blue"


def test_favorite_color_3() -> None:
    # use case
    """What does it work with two popular colors?"""
    assert favorite_color({"Rory": "yellow", "Paris": "orange"}) == "yellow"


def test_invert_1() -> None:
    # edge case
    """Testing to see what occurs when there is an empty input."""
    assert invert({}) == {}


def test_invert_2() -> None:
    # use case
    """Testing to make sure that the answers are all inverted."""
    assert invert({"cat": "meow", "dog": "woof", "cow": "moo"}) == {"meow": "cat", "woof": "dog", "moo": "cow"}


def test_invert_3() -> None:
    # use case
    """Testing to make sure that the answers are all inverted."""
    example = {"kris": "jordan", "jordan": "michael"}
    assert invert(example) == {"jordan": "kris", "michael": "jordan"}


def test_count_1() -> None:
    # edge case
    """Testing to see what occurs when there is an empty input."""
    assert count({}) == {}


def test_count_2() -> None:
    # use case
    """Does this work for a list of one word?"""
    assert count["flower", "flower"] == {"flower": 2}


def test_count_3() -> None:
    # use case
    """Does this work for long lists?"""
    assert count["carrot", "carrot", "banana"] == {"carrot": 2, "banana": 1}