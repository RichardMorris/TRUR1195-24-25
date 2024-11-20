"""Testing package for shapes.py

To run the tests, run the following command:
    python -m unittest shapes_test.py
"""

from shapes import *     # import all functions from shapes.py

import unittest
import io
import contextlib

class TestShapes(unittest.TestCase):
    """ Test cases for the shapes module."""

    def test_n_copies(self):
        """Test the n_copies function."""
        self.assertEqual(n_copies(1, '*'), '*')      # boundary test
        self.assertEqual(n_copies(5, 'a'), 'aaaaa')  # normal test
        self.assertEqual(n_copies(0, 'b'), '')       # boundary/error test
        self.assertEqual(n_copies(-1, 'c'), '')      # error test

    def test_print_square(self):
        """Test the print_square function."""

        # to test print we need to send output to a string
        f = io.StringIO()   
        with contextlib.redirect_stdout(f):
            print_square(5)
        self.assertEqual(f.getvalue(), '*****\n*****\n*****\n*****\n*****\n')

        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            print_square(1)
        self.assertEqual(f.getvalue(), '*\n')

        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            print_square(0)
        self.assertEqual(f.getvalue(), '')

    def test_print_5_by_5_empty_square(self):
        """Test the print_empty_square function with a 5x5 square."""

        # to test print we need to send output to a string
        f = io.StringIO()   
        with contextlib.redirect_stdout(f):
            print_empty_square(5)
        self.assertEqual(f.getvalue(), '*****\n*   *\n*   *\n*   *\n*****\n')

    def test_print_2_by_2_empty_square(self):
        """Test the print_empty_square function with a 2x2 square."""
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            print_empty_square(2)
        self.assertEqual(f.getvalue(), '**\n**\n')

    def test_print_1_by_1_empty_square(self):
        """Test the print_empty_square function with a 1x1 square."""
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            print_empty_square(1)
        self.assertEqual(f.getvalue(), '*\n')

    def test_print_0_by_0_empty_square(self):
        """Test the print_empty_square function with a 0x0 square."""

        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            print_square(0)
        self.assertEqual(f.getvalue(), '')

    def test_print_neg_by_neg_empty_square(self):
        """Test the print_empty_square function with a 0x0 square."""

        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            print_square(-1)
        self.assertEqual(f.getvalue(), '')    