

import socket

# os is a standard module that allows interaction with the operating system
from My_Library import *

server_port = 15555
server_name = 'localhost'

# Create the server socket
# AF_INET specifies the IPv4 address family
# SOCK_STREAM specifies a TCP socket
socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the server IP address and port
socket_server.bind((server_name, server_port))

# Listen for incoming connections
# The server can have up to 5 pending client connections
socket_server.listen(5)

# Clear the screen
clear()

while True:

        # Display a message indicating that the server is waiting for connections
        print("Server listening on port", server_port, "...!")

        # Wait for a client connection
        # accept() returns the client socket and the client's address
        client, address = socket_server.accept()

        # Display the client's address
        print("{} connected".format(address))

        # Display the client's IP address and port number
        print("Client connected with IP address -->:", address[0],
              "on port -->:", address[1])

        # Receive up to 512 bytes of data from the client
        response = client.recv(512)

        # Check whether data has been received
        if response != "":
                print(response.decode())

        # Check whether the client sent 'A' or 'a'
        if (response.decode() == 'A') or (response.decode() == 'a'):

                print("Abort request received")
                print("... Stopping the client connection, see you soon ...")

                # Close the client connection
                client.close()


print("Close")

# Close the client socket
client.close()

# Close the server socket
socket_server.close()

