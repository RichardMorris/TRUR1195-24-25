"""A program to print ascii art of geometric shapes.

It contains the following public functions:
- print_square: prints a square of size size
- print_empty_square: prints an empty square of size size

To see the generated documentation, run the following command:
    python -m pydoc .\shapes.py
To run the program, run the following command:

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
        result += symbol   # this is the same as result = result + symbol
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
    print(n_copies(size, '*'))

# Using this guard will ensure the code is only executed when the file is run
# as a script and not when imported as a module or when using pydoc
if __name__ == '__main__':
    print_square(5)
    print()
    print_empty_square(5)
