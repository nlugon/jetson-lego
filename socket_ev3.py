#!/usr/bin/env python3

import socket
from ev3dev2.motor import LargeMotor

# Initialize motors
motor_left = LargeMotor('outA')
motor_right = LargeMotor('outB')

# EV3 IP address and port
ev3_ip = "10.42.0.66"  # Replace with your EV3's IP address
ev3_port = 8888  # Choose the same port number used on the Raspberry Pi

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the EV3's IP address and port
server_socket.bind((ev3_ip, ev3_port))

# Listen for incoming connections
server_socket.listen(1)
print("Waiting for connection...")

try:
    # Accept the connection
    client_socket, client_address = server_socket.accept()
    print("Connected to Raspberry Pi")
    
    while True:
        # Receive data from the Raspberry Pi
        data = client_socket.recv(1024).decode()

        # Process the received data
        if data:
            print("Received:", data)
            # Control the EV3 motors based on the received command
            if data == 'w':
                # Start motors
                # Add code here to start the motors
                print("Motors started")
                motor_left.on(50)
                motor_right.on(50)
            elif data == 's':
                # Stop motors
                # Add code here to stop the motors
                print("Motors stopped")
                motor_left.on(-50)
                motor_right.on(-50)
            elif data == 'a':
                # Stop motors
                # Add code here to stop the motors
                print("Motors stopped")
                motor_left.on(-50)
                motor_right.on(50)
            elif data == 'd':
                # Add code here to stop the motors
                print("Turn right")
                motor_left.on(50)
                motor_right.on(-50)
            elif data == 'z':
                # Stop motors
                # Add code here to stop the motors
                print("Motors stopped")
                motor_left.off()
                motor_right.off()
            elif data == 'x':
                # Add code here to stop the motors
                print("High speed mode")
                motor_left.on(100)
                motor_right.on(100)


            else:
                # Add code here to control the motors based on other commands
                pass

        # Break the loop if the received data is 'q' (quit)
        if data == 'q':
            break

except Exception as e:
    print("Error:", str(e))
finally:
    # Close the client socket
    client_socket.close()
    # Close the server socket
    server_socket.close()

