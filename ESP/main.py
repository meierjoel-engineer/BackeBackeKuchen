from machine import UART
import time
import network
import socket

# Configure UART for OpenScale
uart = UART(1, baudrate=250_000, tx=5, rx=6)  # TX=1, RX=3 (adjust pins as needed)

def read_openscale():
    timeout = 1  # Total wait time in seconds
    wait_interval = 0.1  # Wait interval in seconds
    waited_time = 0  # Time waited so far

    while waited_time < timeout:
        if uart.any():  # Check if data is available
            line = uart.readline()  # Read a full line
            if line:
                return line.decode('utf-8').strip()
        time.sleep(wait_interval)
        waited_time += wait_interval

    return None

# Wi-Fi credentials
SSID = 'RPi-Wlan'
PASSWORD = '44556677'

# Server IP and Port
SERVER_IP = '192.168.226.218'
SERVER_PORT = 65432

def connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    print(f"Connecting to Wi-Fi: {SSID}")
    while not wlan.isconnected():
        print(".", end="")  # Show progress
        time.sleep(1)
    print("\nConnected to Wi-Fi!")
    print(f"IP Address: {wlan.ifconfig()[0]}")
    addr_info = socket.getaddrinfo(SERVER_IP, SERVER_PORT)
    addr = addr_info[0][-1]
    s = socket.socket()
    print(f"Attempting to connect to server at {SERVER_IP}:{SERVER_PORT}")
    s.connect(addr)
    print("Connected to server!")
    return s


# Connect to server and send data
def client(s):
    while True:
        print("in loop")
        uart.write('0')
        data = read_openscale()
        print(f"Data: {data}")
        s.send(data.encode('utf-8'))
        time.sleep(0.1)
            
            

def main():
    s = connect()
    client(s)

if __name__ == "__main__":
    main()

# ampy --port COM12 put ESP\main.py