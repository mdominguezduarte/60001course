# Decomposition, abstraction and functions
import math


def sqrt_int(i):
    """
    This function return True in case of the sqrt of a given number is an integer

    """
    result = math.sqrt(i) - math.floor(math.sqrt(i))
    print(math.sqrt(i), '-', math.floor(math.sqrt(i)), '=', result)
    return result == 0
