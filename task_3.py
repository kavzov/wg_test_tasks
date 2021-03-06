#!/usr/bin/env python
import socket


def main():
    VALID_PATH = '/ping'

    # Socket settings
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('', 8080))
    server_socket.listen(1)
    print('Starting HTTP server for task 3\nQuit the server with Ctrl-C')

    while True:
        response_msg = 'HTTP/1.1 200 OK\n\n'

        # Receive data from client socket
        client_socket = server_socket.accept()[0]
        data = client_socket.recv(1024).decode('utf-8')

        # Get request path from the request headers
        try:
            path = data.split(' ')[1]
        except IndexError:
            path = None

        # Set response message. It stay blank if invalid path
        if path == VALID_PATH:
            response_msg += 'Cats service. Version 0.1\n'

        # Send message to client
        client_socket.send(response_msg.encode('utf-8'))

        # Close connection with client
        client_socket.close()


if __name__ == '__main__':
    main()
