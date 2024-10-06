import serial
import time
import numpy as np

# Set up the serial connection (adjust 'COM5' to your actual port)
ser = serial.Serial('COM5', 9600, timeout=1)

# Allow some time for the connection to establish
time.sleep(2)

# Initialize an empty list to store weights
weights = []

try:
    while True:
        # Read a line from the serial port
        line = ser.readline().decode('utf-8', errors='ignore').strip()
        
        if line:
            # Split the line by commas
            values = line.split(',')
            
            # Ensure there are enough values before accessing them
            if len(values) >= 5:
                # Extract the weight
                weight = float(values[1])
                
                # Append the weight to the list
                weights.append(weight)
                
                # Print the extracted values
                print(f"Weight: {weight} {values[2]}")
            else:
                print(f"Unexpected data format: {line}")
        
        # Add a small delay to avoid overwhelming the serial port
        time.sleep(0.1)

except KeyboardInterrupt:
    # Convert the list of weights to a NumPy array
    weights_array = np.array(weights)
    
    # Save the NumPy array to a file
    np.save('weights.npy', weights_array)
    
    # Close the serial connection when the script is interrupted
    ser.close()
    print("Serial connection closed.")
    print(f"Saved weights to 'weights.npy'.")