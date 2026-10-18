
import socket

hote = "localhost"
port = 15555

# Create the client socket
# AF_INET specifies the IPv4 address family
# SOCK_STREAM specifies a TCP socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the client to the server
# The server is running on the local machine at port 15555
client.connect((hote, port))

print("Connexion au serveur sur le port {}".format(port))

# Get the local IP address and local port used by the client socket
local_address, local_port = client.getsockname()

print("Utilisation du port local --> :", local_port)
print("Utilisation de l'adresse IP --> :", local_address)

# Ask the user to enter a message to send to the server
msg = input("Entrer un message à envoyer au serveur --> : ")

# Encode the message into bytes and send it to the server
client.send(msg.encode())

print("Fermeture de la connexion")

# Close the client socket and terminate the connection
client.close()

