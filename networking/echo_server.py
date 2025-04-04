# first of all import the socket library
import socket
import sys

def open_socket():
    global s, port
    # next create a socket object
    s = socket.socket()
    print ("Socket successfully created")

    # reserve a port on your computer in our
    # case it is 40674 but it can be anything
    port = 40674

    # Next bind to the port
    # we have not typed any ip in the ip field
    # instead we have inputted an empty string
    # this makes the server listen to requests
    # coming from other computers on the network
    s.bind(('', port))
    print ("socket binded to %s" %(port))

    # put the socket into listening mode
    s.listen(5)    
    print ("socket is listening")

def wait_for_requests():
    global host_title
    # a forever loop until we interrupt it or
    # an error occurs
    while True:

        # Establish connection with client.
        con, addr = s.accept()
        print ('Got connection from', addr )
        con.send(host_title.encode())

        words = con.recv(1024)
        print('Received:',words.decode())
        # send a thank you message to the client.
        con.send(('Hello '+words.decode()).encode())

        # Close the connection with the client
        con.close()

if __name__ == '__main__':
    if len(sys.argv) < 2:
    # if len(sys.argv < 2):
        print("Please privide a welcome messages as the first argument")
        sys.exit()
    ip_addr = sys.argv[1]
    host_title = sys.argv[1]
    print(host_title)
    open_socket()
    wait_for_requests()
