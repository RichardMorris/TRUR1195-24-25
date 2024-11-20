# TRUR1195-24-25
Code for the TRUR1195 Security Programming Module at Truro college

## Designing a shapes program

The first task is to develope an ascii program.

### User story:

As a retro-game developer 
I want to generate different shapes
so that I can construct an attractive title screen   

(A high level User Story in the form <role> <action> <motivation>.)

### Functional Requirements:
* The program should allow the selection of different shapes
* The program should allow different sizes to be specified
* The following shapes should be supported:
** a square,
** an empty square

### Non-functional requirements:
* The program should handle invalid inputs without crashing

### Design

The code will be split over a number of files
* shapes.py - contains the core functions
* shapes_main.py - a simple program allowing all the different shapes to be displayed
* shapes_test.py - tests for all the functions 

As many shapes contain strings of repeated symbols we will use a function
`n_copies` to return a string with so many copies of a symbol. 
Returning a string rather than directly printing the output will make it 
more flexible and easier to test. 

Two other functions `print_square` and `print_empty_square` 
will be provided to print a square and an empty-square
directly to the console. Both will take the size of the square as input.

The main program will consist of a read-eval-print loop, it will
first ask for the type of shape to print and then ask for the size of the shape.
It will then print the shape to the console and the loop will repeat.
When the user type "quit" the program will exit.
Allowed names of shapes are "square" and "empty_square" square. 

To enable other developers to use the functions here documentation
using DocStrings in the GoogleDocs format. [realpython](https://realpython.com/documenting-python-code/)

### Testing

The testing of the individual functions are shown in `shapes_test.py`.
For each we test on either side of the boundary, normal value tests, and erronious
tests. For the empty square other low value tests are caried out to ensure 
it works in all cases.

For the main program the following test of the input and output are run

Test 1 - drawing an empty square
Inputs: empty_square, 5
Output: A five by five empty square is displayed, and it asks for a new shape

Test 2 - drawing a square
Inputs: square, 1
Output: A single * is displayed, and it asks for a new shape

Test 3 - quitting the program
Inputs: quit
Output: The program exits

Test 4 - invalid name of a shape reports an error message
Input: qwerty
Output: A message saying invalid input, and it asks again

Test 5 - invalid size reports an error message
Input: square five
Output: A message saying invalid input and it asks for the size again

Test 6
Input: empty_square five
Output: A message saying invalid input and it asks for the size again
