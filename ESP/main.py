
from machine import UART, Pin
import time

# Configure UART on GPIO pins
uart = UART(1, baudrate=9600, tx=Pin(4), rx=Pin(3))

print("Waiting for data from USB device...")

while True:
    print(".", end="")  # Show progress
    if uart.any():  # Check if data is available
        data = uart.read()  # Read available data
        if data:
            print(f"Received: {data.decode('utf-8')}")
    time.sleep(0.1)