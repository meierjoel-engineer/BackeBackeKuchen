# from machine import UART
# import time

# # Configure UART for OpenScale
# uart = UART(1, baudrate=9600, tx=5, rx=6)  # TX=1, RX=3 (adjust pins as needed)

# def read_openscale():
#     while True:
#         if uart.any():  # Check if data is available
#             line = uart.readline()  # Read a full line
#             if line:
#                 return line.decode('utf-8').strip()

# def senddata(data):
#     uart.write(data)


# def main():
#     while True:
#         try:
#             senddata('0')
#             data = read_openscale()
#             if data is not None:
#                 parts = data.split(',')
#                 if len(parts) == 6:
#                     print(f"ADC: {parts[3]}, Temperature: {parts[4]}")
#             time.sleep(1)
#         except Exception as e:
#             print(f"Error: {e}")

# if __name__ == "__main__":
#     main()