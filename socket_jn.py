#!/usr/bin/env python3

import socket

# EV3 IP address and port
ev3_ip = "10.42.0.66"  # Replace with your EV3's IP address
ev3_port = 8888  # Choose a port number

try:
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect to the EV3
    client_socket.connect((ev3_ip, ev3_port))
    print("Connected to EV3")
    
    while True:
        # Get user input
        command = input("Enter command (w for forward, s for backward, a for left, d for right, q to quit, x for high speed, z to stop motors): ")
        
        # Send the command to the EV3
        client_socket.send(command.encode())
        
        # Quit if 'q' is entered
        if command == 'q':
            break

except Exception as e:
    print("Error:", str(e))
finally:
    # Close the socket
    client_socket.close()
