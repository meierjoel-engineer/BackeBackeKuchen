import serial
import time

# Set up the serial connection (adjust 'COM5' to your actual port)
ser = serial.Serial('COM5', 9600, timeout=1)

# Allow some time for the connection to establish
time.sleep(2)

try:
    while True:
        # Read a line from the serial port
        line = ser.readline().decode('utf-8', errors='ignore').strip()
        
        if line:
            # Split the line by commas
            values = line.split(',')
            
            # Ensure there are enough values before accessing them
            if len(values) >= 5:
                # Extract the values
                timestamp = values[0]
                weight = values[1]
                unit = values[2]
                temperature = values[3]
                unknown = values[4]
                
                # Print the extracted values
                print(f"Timestamp: {timestamp}, Weight: {weight} {unit}, Temperature: {temperature}, Unknown: {unknown}")
            else:
                print(f"Unexpected data format: {line}")
        
        # Add a small delay to avoid overwhelming the serial port
        time.sleep(0.1)

except KeyboardInterrupt:
    # Close the serial connection when the script is interrupted
    ser.close()
    print("Serial connection closed.")