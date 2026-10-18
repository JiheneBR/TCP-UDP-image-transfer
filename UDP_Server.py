import socket

# Define the server IP address
hote = "127.0.0.1"

# Define the port number used by the server
port = 9999

# Create a UDP socket using IPv4
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the specified IP address and port
server_socket.bind((hote, port))

# Display a message indicating that the server is waiting for data
print("Waiting for data on port", port)

# Open the destination file in binary write mode
with open("C:/reception/images1.jfif", "wb") as f:

    # Continuously receive data from the client
    while True:

        # Receive a UDP packet of up to 1024 bytes
        # 'data' contains the received data
        # 'adresse' contains the sender's IP address and port
        data, adresse = server_socket.recvfrom(1024)

        # Check if the client has finished sending the file
        if data == b"EOF":
            break

        # Write the received data into the file
        f.write(data)

# Close the server socket
server_socket.close()

# Close the file
f.close()

# Display a success message
print("File successfully saved.")