# Import socket module
import socket

# Create a socket object
s = socket.socket()

# Define the port on which you want to connect
port = 40674

# connect to the server on local computer
s.connect(('127.0.0.1', port))
name = input("Please type your name ")

print("Sending datas")

s.send(name.encode())

print("Data sent")
# receive data from the server
print(s.recv(1024))

# close the connection
s.close()
