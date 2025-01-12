from machine import UART  # type: ignore
import time # type: ignore
import network  # type: ignore
import socket # type: ignore

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




# IN BOOTLOADER MODE (Press and hold BOOT button plug in USB, release BOOT button)
# esptool --port COM12 erase_flash
# esptool --port COM12 --baud 115200 write_flash -z 0x0 bin\ESP32_GENERIC_C3-20241025-v1.24.0.bin

# IN NORMAL MODE
# mpremote connect COM12 fs cp ESP\main.py :main.py

# now reset the board, and it should run the code in main.py