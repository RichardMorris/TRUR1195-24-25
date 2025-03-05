# code to count the number of lines in a file

import sys
import re
from datetime import datetime

def get_referer(line: str):
    # Match the last quoted string in the line
    # Search for:
    #    A quote: \"
    #    A group inside: ( ) 
    #      Any character other than a quote: [^\"]
    #      Repeated any number of times: * 
    #    Then a quote: \"
    #    End of line marker: $
    res = re.search(r'\"([^\"]*)\"$', line)
    # return 1st group matched
    return res.group(1) if res else None

def get_referers(file_name):
    data = []
    with open(file_name) as file:
        for line in file:
            referer = get_referer(line)
            if referer:
                data.append(referer)
    return data

def n_parts(file_name):
    """Number of parts in each line
    Args:
    file_name (str): The name of the file to count
    Returns:
    data: A list with number of parts per line
    """

    data = [] 
    # open the file
    # ensures the file is closed when the block is exited
    with open(file_name) as file: 
        count =0
        # loop through each line in the file
        for line in file:
            parts = line.split(' ')
            #print(len(parts))
            data.append(len(parts))
    return data



def splitn(file_name,part):
    """Split the lines returning the first field
    Args:
    file_name (str): The name of the file to count
    part (int): The part of the line to return, 0 for the first
    Returns:
    data: A list with the first field in the file
    """

    data = [] 
    # open the file
    # ensures the file is closed when the block is exited
    with open(file_name) as file: 
        count =0
        # loop through each line in the file
        for line in file:
            parts = line.split(' ')
            ip = parts[part]
            data.append(ip)
    return data

def split_struct(file_name):
    """Split the lines returning a structure
    Args:
    file_name (str): The name of the file to count
    Returns:
    data: A list with each part a dictionary
    """

    data = [] 
    # open the file
    # ensures the file is closed when the block is exited
    with open(file_name) as file: 
        count =0
        # loop through each line in the file
        for line in file:
            parts = line.split(' ')
            ip = parts[0]
            date = parts[3]
            method = parts[5]
            url = parts[6]
            refer = parts[10]
            status = parts[8]
            size = parts[9]
            user_agent = parts[11]
            data.append({'ip':ip,'date':date,'method':method,'url':url,'refer':refer,
                         'status':status,'size':size,'user_agent':user_agent}) 
    return data

def statemachine(line):
    """Split the line using a state machine.
    Double quotes are  string deliminators as are square brackets [, ].
    Spaces outside of strings are field seperators.
    Args:
    line (str): The line to split
    Returns:
    items: A list of the fields in the line
    """

    part = 0
    items = [] 
    str = ""
    state = 0 # 0: start, 1: a string "...", 2: a list [...]

    for c in line:
        if state == 0:
            if c == ' ': # a space indicates the end of a part
                items.append(str)   # store the part
                str = ""            # reset the string
                part += 1           # move to the next part
            elif c == '\"': # a quote indicates the start of a string
                state = 1
            elif c == '[': # a square bracket indicates the start of list 
                state = 2
            else:
                str += c # add the character to the string
        elif state == 1:
            if c == '\"':
                state = 0
            else:
                str += c # add the character to the string
        elif state == 2:
            if c == ']':
                state = 0
            else:
                str += c # add the character to the string

    # end of line
    items.append(str) # store the last part
    return items

def parse_datestr(datestr):
    """Parse the date string in the format: 18/Dec/2015:14:45:08 +0000
    Args:
    datestr (str): The date string to parse
    Returns:
    datetime: The date and time
    """
    months = {'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,
             'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}

    # datestr = '[18/Dec/2015:14:45:08 +0000]'

    m = re.match(r'(\d\d)/(\w\w\w)/(\d\d\d\d):(\d\d):(\d\d):(\d\d) (.*)', datestr)
    #print(m.group(1),months[m.group(2)],m.group(3))
    d = datetime(int(m.group(3)),months[m.group(2)],int(m.group(1)),
                    int(m.group(4)),int(m.group(5)),int(m.group(6)))
    return d

def split_statemachine(file_name):
    """Split the lines using a state machine
    Args:
    file_name (str): The name of the file to count
    Returns:
    data: A list with each part a dictionary
    """

    data = [] 
    # open the file
    # ensures the file is closed when the block is exited
    with open(file_name) as file: 
        count =0
        # loop through each line in the file
        for line in file:
            items = statemachine(line.strip())
            print(items)
            datetime = parse_datestr(items[3])
            data.append({'ip':items[0],'date':datetime,
                         'request':items[4],
                         'status':items[5],'size':items[6],
                         'refer':items[7],
                         'user_agent':items[8]})
    return data

if __name__ == '__main__':
    file_name = sys.argv[1]
    #print(splitn(file_name,int(part_no)))
    #print(n_parts(file_name))
    #print(get_referers(file_name))
    #print(split_struct(file_name))
    print(split_statemachine(file_name))
    