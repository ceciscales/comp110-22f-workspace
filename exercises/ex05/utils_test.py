"""Testing EX05: utils.py."""


__author__ = "730396639"


from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens() -> None:
    """Use case that makes sure that the result is even."""
    assert only_evens([2, 4, 6]) == [2, 4, 6]
    

def test_only_evens_1() -> None:
    """Use case that makes sure of an even outcome."""
    assert only_evens([1, 2, 3, 4, 6, 12]) == [2, 4, 6, 12]


def test_only_evens_2() -> None:
    """Edge case that tests the outcome of an empty list."""
    assert only_evens([]) == []


def test_concat() -> None:
    """Use case that makes sure that the lists are added together."""
    assert concat([1, 2], [3, 4]) == [1, 2, 3, 4]
   
   
def test_concat_1() -> None:   
    """Use case that makes sure that the lists are added together."""
    assert concat([4, 7, 6], [3, 4]) == [4, 7, 6, 3, 4]
   
   
def test_concat_2() -> None:   
    """Edge case that tests the outcome of an empty list."""
    assert concat([], []) == []


def test_sub() -> None:
    """Use case that makes sure that the list is between the indices."""
    assert sub([1, 2, 3], 0, 3) == [1, 2, 3]
    
    
def test_sub_1() -> None:
    """Use case that makes sure that the list is between the indices."""
    assert sub([6, 5, 4, 7], 0, 3) == [6, 5, 4]
    
    
def test_sub_2() -> None:    
    """Edge case that tests the outcome of an empty list."""
    assert sub([], (), ()) == []