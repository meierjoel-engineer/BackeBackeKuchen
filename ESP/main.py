from machine import UART
import time

# Configure UART for OpenScale
uart = UART(1, baudrate=9600, tx=5, rx=6)  # TX=1, RX=3 (adjust pins as needed)

def read_openscale():
    while True:
        if uart.any():  # Check if data is available
            line = uart.readline()  # Read a full line
            if line:
                return line.decode('utf-8').strip()


def main():
    while True:
        try:
            data = read_openscale()
            if data is not None:
                parts = data.split(',')
                if len(parts) == 2:
                    print(f"ADC Value: {parts[0]}")
                time.sleep(0.2)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()