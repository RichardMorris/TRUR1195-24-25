"""A program to print ascii art of geometric shapes.

It contains the following functions:
- print_square: prints a square of size size
- print_empty_square: prints an empty square of size size
"""

def n_copies(n, symbol):
    """Returns a string with n copies of the symbol
    
    Args:
    n (int): How many copies
    symbol (str): The symbol to print

    Returns:
    A string with the specified number of characters
    """
    result = ""
    for _ in range(n):
        result += symbol
    return result

def print_square(size):
    """Prints a square of size size

    Args:
    size (int): The lenght/width of the squares
    Returns:
    None
    """
    for _ in range(size):
        print(n_copies(size, '*'))

def print_empty_square(size):
    """Prints an empty square of a give size

    Args:
    size (int): The lenght/width of the squares
    Returns:
    None
    """
    print(n_copies(size, '*'))
    for _ in range(size - 2):
        print('*' + n_copies(size - 2, ' ') + '*')

print_square(5)
print()
print_empty_square(5)
