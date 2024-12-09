from machine import UART
import time
import network
import socket
import time
import random
import machine


# Configure UART for OpenScale
uart = UART(1, baudrate=9600, tx=5, rx=6)  # TX=1, RX=3 (adjust pins as needed)

def read_openscale():
    while True:
        if uart.any():  # Check if data is available
            line = uart.readline()  # Read a full line
            if line:
                return line.decode('utf-8').strip()

def senddata(data):
    uart.write(data)


# Wi-Fi credentials
SSID = 'RPi-Wlan'
PASSWORD = '44556677'

# Server IP and Port
SERVER_IP = '192.168.241.218'
SERVER_PORT = 65432

sleep_duration_ms = 20_000 

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
def tcp_client(msg):
    try:
        addr_info = socket.getaddrinfo(SERVER_IP, SERVER_PORT)
        addr = addr_info[0][-1]
        s = socket.socket()
        print(f"Attempting to connect to server at {SERVER_IP}:{SERVER_PORT}")
        s.connect(addr)
        print("Connected to server!")
        s.send(msg.encode('utf-8'))
        print(f"Sent: {msg}")
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        s.close()
        print("Connection closed")

def disconnect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.disconnect()
    wlan.active(False)
    print("Wi-Fi disconnected")

def main():
    while True:
        try:
            senddata('0')
            data = read_openscale()
            if data is not None:
                parts = data.split(',')
                if len(parts) == 6:
                    msg = f"ADC: {parts[3]}, Temperature: {parts[4]}"
                    print(msg)
                    connect_wifi()
                    tcp_client(msg)
                    disconnect_wifi()
                    machine.deepsleep(sleep_duration_ms)
            time.sleep(1)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
    main()