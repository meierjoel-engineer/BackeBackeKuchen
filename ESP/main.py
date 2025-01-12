import socket
import time
import network
from machine import UART

# Configure UART for OpenScale
uart = UART(1, baudrate=115200, tx=5, rx=6)

def read_openscale(timeout=1, wait_interval=0.1):
    waited_time = 0
    while waited_time < timeout:
        if uart.any():
            return uart.readline()
        time.sleep(wait_interval)
        waited_time += wait_interval
    return None

# Wi-Fi credentials
SSID = 'RPi-Wlan'
PASSWORD = '44556677'

# Server IP and Port
SERVER_IP = '192.168.80.218'
SERVER_PORT = 42069

def connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    print(f"Connecting to Wi-Fi: {SSID}")
    while not wlan.isconnected():
        print(".", end="")
        time.sleep(1)
    print("\nConnected to Wi-Fi!")
    print(f"IP Address: {wlan.ifconfig()[0]}")
    addr = socket.getaddrinfo(SERVER_IP, SERVER_PORT)[0][-1]
    s = socket.socket()
    s.connect(addr)
    print(f"Connected to server at {SERVER_IP}:{SERVER_PORT}")
    return s

def client(s):
    while True:
        data = read_openscale()
        if data:
            print(f"Data: {data}")
            s.send(data)
        else:
            print("No data received, breaking the loop")
            break
        time.sleep(0.1)

def main():
    s = connect()
    client(s)

if __name__ == "__main__":
    main()




# IN BOOTLOADER MODE (Press and hold BOOT button plug in USB, release BOOT button)
# esptool --port COM12 erase_flash
# esptool --port COM12 --baud 115200 write_flash -z 0x0 bin\ESP32_GENERIC_C3-20241025-v1.24.0.bin

# IN NORMAL MODE
# mpremote connect COM12 fs cp ESP\main.py :main.py

# now reset the board, and it should run the code in main.py