# code to count the number of lines in a file

import sys

def count_lines(file_name):
    """Count the number of lines in a file

    Args:
    file_name (str): The name of the file to count

    Returns:
    int: The number of lines in the file
    """

    # open the file
    # ensures the file is closed when the block is exited

    with open(file_name) as file: 
        count =0
        # loop through each line in the file
        for line in file:
            count += 1
        return count
    
if __name__ == '__main__':
    file_name = sys.argv[1]
    print(count_lines(file_name))