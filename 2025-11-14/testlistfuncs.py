
#-----------------------------------------------------
# maximum tests
#-----------------------------------------------------

def test_maximum() -> None:
    """
    >>> from listfuncs import maximum
    >>> a = [20, 34, 10, 4, 18, 11]
    >>> maximum(a)
    34

    >>> a = []
    >>> maximum(a) == None
    True

    >>> a = [4]
    >>> maximum(a)
    4
    """


#-----------------------------------------------------
# equivalence tests
#-----------------------------------------------------

def test_count_evens() -> None:
    """
    >>> from listfuncs import count_evens
    >>> a = [4, 0, 7, 3, 10, 17]
    >>> count_evens(a)
    3

    >>> a = [5, 1, 7, 3, 11, 17]
    >>> count_evens(a)
    0

    >>> a = []
    >>> count_evens(a)
    0
    """


if __name__ == '__main__':
    import doctest
    doctest.testmod()
