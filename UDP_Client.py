import socket
# Create the client socket using IPv4 and UDP protocol
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Open the image file in binary read mode
with open("C:/emition/images.jfif", "rb") as f:

    # Read and send the file data in a loop
    while True:

        # Read 1024 bytes from the file
        data = f.read(1024)

        # Check if the end of the file has been reached
        if not data:
            break

        # Send the data to the server at IP address 127.0.0.1
        # using port 9999
        client.sendto(data, ("127.0.0.1", 9999))

# Send a special message to indicate the end of the file
client.sendto(b"EOF", ("127.0.0.1", 9999))
# Close the file
f.close()
# Close the client socket
client.close()
# Display a message indicating that the file transfer is complete
print("File transfer completed")