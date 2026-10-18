# Python Socket Transfer (UDP & TCP)

A demonstration of network communication and file transfer protocols using Python's standard `socket` module.

## Features
- **UDP Image Transfer**: Streams an image chunk-by-chunk over UDP (`UDP_Client.py` and `UDP_Server.py`).
- **TCP Client-Server**: Text communication and connection handling over TCP (`client_socket_Tcp.py` and `serveur_socket_Tcp.py`).

## How to Run

### UDP Image Transfer
1. Run the server first:
   ```bash
   python UDP_Server.py

2. In a separate terminal, run the client:
   ```bash
   python UDP_Client.py

### TCP Communication

1. Run the server:
   ```bash
   python serveur_socket_Tcp.py

2. Run the client:
   ```bash
   python client_socket_Tcp.py