# A programmer's view of networking

This week we will look at low level network programming using sockets, the fundamentals of how you might write a program like a web server, with a server program that listens for traffic on a particular port, and handles requests from a client. 
This will work TCP connections at the transport layer in the OSI model, the data transmitted is a raw stream of bytes, without any meta-data indicating the format of the data. 
connections are not guaranteed to last, so you may need to frequently reconnect and don't have session level information.  

Higher level programs might communicate at the Application layer, say using the Hypertext Transfer Protocol, where details of the fields in a web request or response are specified. 

The key abstraction is a socket. Server programs can listen to a server-socket which is bound to a particular port on a machine. Client programs will use a client-socket that attempts to connect to a server specified by an IP address and port number. 

Code for this week can be found in the networking folder on github.

 https://github.com/RichardMorris/TRUR1195-24-25/blob/main/networking/echo_client.py

https://github.com/RichardMorris/TRUR1195-24-25/blob/main/networking/echo_server.py

There is a client-server echo program, with an `echo_server.py` file and an `echo_client.py` file. 
We will use the VM's for this, and each of you will run echo_server.py, you classmate will be able to connect to your servers using the local IP's in the 10.0.0.1-10.0.0.16 range. 

## Python code for Sockets
The key bits of code for setting up the server are

```
# Create a socket object
sock = socket.socket() 
# Next bind to the port
port = 40674
sock.bind(('', port))
# put the socket into listening mode
sock.listen(5)
# Now busily wait for connection
while True:
    # Establish connection with client.
    con, addr = s.accept()
```

To set up the client use
```
# Create a socket object
sock = socket.socket()
# Define the port on which you want to connect
port = 40674
# construct address as a tuple (ip address, port number)
address = (ip_addr, port)
# connect to the server on 
sock.connect(address)
```
Once a connection is established bytes of data can be sent and received using, the client might send some data
```
name = input("Please type your name ")
# send data encoded in binary
sock.send(name.encode())
```
And the server might receive the data
```
# Receive upto 1024 bytes of data and decode binary data into characters
words = con.recv(1024).decode()
print('Received:',words)
# send a thank you message to the client.
con.send(('Hello '+words.decode()).encode())
```

Finally, the connection should be closed
```
# Close the connection with the client
con.close()
```
The client could then receive the rest of the response from the server
```
# receive data from the server
while True:
        data = sock.recv(1024)
        print("Received: ",len(data)," bytes")
        # a length of zero means the server has closed the connection
        # or the connection died for some other reason
        if(len(data)==0):
            break
        print("Received: ",data.decode())
```
This is only a very simple example, a better example is found on  Socket Programming HOWTO

The commands here are mostly system calls to the underlying socket library, which was first implemented in BSD Unix.  

## Application layer network programming

The socket library has no knowledge about the format of the data being sent, this is normally specified by application level protocols like HTTP, specified in the in the 
[http 1.1 rfc](https://datatracker.ietf.org/doc/html/rfc9112)


In HTTP the client will send a request header:
```
GET / HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-GB,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
 ```

The server would then respond with a request header
```
HTTP/1.1 200 OK
Date: Mon, 23 May 2005 22:38:34 GMT
Content-Type: text/html; charset=UTF-8
Content-Length: 155
Last-Modified: Wed, 08 Jan 2003 23:11:55 GMT
Server: Apache/1.3.3.7 (Unix) (Red-Hat/Linux)
ETag: "3f80f-1b6-3e1cb03b"
Accept-Ranges: bytes
Connection: close

<html>
  <head>
    <title>An Example Page</title>
  </head>
  <body>
    <p>Hello World, this is a very simple HTML document.</p>
  </body>
</html>
``` 

It is the job of the client and server code to parse and interpret these headers. In practice, you would use higher level libraries to handle specific protocols.

## Bluetooth connection 

There are many options on the socket library, you can have buffered or unbuffered streams, you can set them up for UDP packets, or use different forms of addresses. For my thermal camera which uses Bluetooth for connections it uses 
specalised versions of the socket library. See https://github.com/RichardMorris/mlx90640-bluetooth
```
server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
```
The client uses
```
sock = bluetooth.BluetoothSocket()
# mac address for server
piMac = ‘B8:27:EB:B1:D2:E5’
channel = 1
sock.connect((piMac, channel))
```
For each frame, the client send one line of text and the server responds with a fixed block of data representing the pixels.

There is a problem with the connection dying after about 10 minutes.  

## Useful links

* [Socket programming HOWTO](https://docs.python.org/3/howto/sockets.html) a better example that handles closing of connections etc.
* [Python socket library documentation](https://docs.python.org/3/library/socket.html). The gory details.
* [Python socket guide](https://realpython.com/python-sockets/)
* [Socket programming in python quiz](https://realpython.com/quizzes/socket-programming-in-python/) Covers most of the above, but there are some advanced questions, so don't expect to get 100% 
