import network
import socket
import time
import random


# Main program
try:
    connect_wifi()
    tcp_client()
except KeyboardInterrupt:
    print("\nProgram interrupted by user.")

