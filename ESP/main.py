import network
import socket
import time
import random

# Wi-Fi credentials
SSID = 'RPi-Wlan'
PASSWORD = '44556677'

# Server IP and Port
SERVER_IP = '192.168.241.218'
SERVER_PORT = 65432

# Connect to Wi-Fi
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    print(f"Connecting to Wi-Fi: {SSID}")
    while not wlan.isconnected():
        print(".", end="")  # Show progress
        time.sleep(1)
    print("\nConnected to Wi-Fi!")
    print(f"IP Address: {wlan.ifconfig()[0]}")

# Connect to server and send random numbers
def tcp_client():
    try:
        addr_info = socket.getaddrinfo(SERVER_IP, SERVER_PORT)
        addr = addr_info[0][-1]
        s = socket.socket()
        print(f"Attempting to connect to server at {SERVER_IP}:{SERVER_PORT}")
        s.connect(addr)
        print("Connected to server!")
        
        while True:
            number = random.randint(0, 100)
            message = f"Random number: {number}"
            s.send(message.encode('utf-8'))
            print(f"Sent: {message}")
            time.sleep(1)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        s.close()
        print("Connection closed")

# Main program
try:
    connect_wifi()
    tcp_client()
except KeyboardInterrupt:
    print("\nProgram interrupted by user.")
