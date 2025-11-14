"""
List processing routines
"""


def maximum(a: list[int]) -> int | None:
    """
    Returns the maximum value in a list of integers.
    Return None if the list is empty.
    """
    if len(a) == 0:
        return None
    else:
        max = a[0]
        for elem in a:
            if elem > max:
                max = elem
        return max


def count_evens(seq: list[int]) -> int:
    """  
    Returns the number of even numbers in a list
    of integers.
    """
    count = 0
    for elem in seq:
        if elem % 2 == 0:
            count += 1
    return count
