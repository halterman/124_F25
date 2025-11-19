"""
List processing routines
"""


def maximum(a: list[int]) -> int | None:
    """
    Returns the maximum value in a list of integers.
    Returns None if the list is empty.
    """
    if a == []:
        return None
    max = a[0]
    for x in a:
        if x > max:
            max = x
    return max


def count_evens(seq: list[int]) -> int:
    """  
    Returns the number of even numbers in a list
    of integers.
    """
    count = 0
    for x in seq:
        if x % 2 == 0:
            count += 1
    return count

