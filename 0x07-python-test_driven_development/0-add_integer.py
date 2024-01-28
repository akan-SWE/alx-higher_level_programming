
"""Defines the add_integer function

add_integer: adds two integers, number must be an integer or a float, raises a TypeError
for floats it type cast to integer
"""
def add_integer(a, b=98):
    """Adds two integers
    returns: the addition of the two integer
    """
    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')
    elif type(b) not in [int, float]:
        raise TypeError('b must be an integer')

    return int(a) + int(b)
