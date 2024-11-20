"""A program to print ascii art of geometric shapes.

To run the program, run the following command:
    python shapes_main.py

The program will repeatidle ask the user for a shape
and a size until the user enters 'quit'.

Allowed shapes are:
- square
- empty_square
"""

from shapes import *

if __name__ == '__main__':
    while True:
        shape = input("Enter a shape (square, empty_square) or 'quit': ")
        if shape == 'quit':
            break
        size = int(input("Enter the size: "))
        if shape == 'square':
            print_square(size)
        elif shape == 'empty_square':
            print_empty_square(size)
        else:
            print("Unknown shape")
