# Import socket module
import socket
import sys

def open_socket():
    global ip_addr,sock
    # Create a socket object
    sock = socket.socket()

    # Define the port on which you want to connect
    port = 40674

    # connect to the server on 
    sock.connect((ip_addr, port))



if __name__ == '__main__':
    ip_addr = sys.argv[1]
    print("Connecting to ",ip_addr)
    open_socket()
    print("Connected")

    name = input("Please type your name ")
    print("Sending:",name)
    sock.send(name.encode())
    print("Data sent")

    # receive data from the server
    while True:
        data = sock.recv(1024)
        print("Received: ",len(data)," bytes")
        if(len(data)==0):
            break
        print("Received: ",data.decode())

    # close the connection
    print("Closing connection")
    sock.close()
    print("closed")
