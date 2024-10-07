import serial
import time
import numpy as np

# Set up the serial connection (adjust 'COM5' to your actual port)
ser = serial.Serial('COM5', 9600, timeout=1)

# Allow some time for the connection to establish
time.sleep(2)

# Initialize an empty list to store ADC values and timestamps
adc_values_with_timestamps = []
timestamp_0 = time.time()
try:
    while True:
        # Read a line from the serial port
        line = ser.readline().decode('utf-8', errors='ignore').strip()
        
        if line:
            # Split the line by commas
            values = line.split(',')
            
            # Ensure there are enough values before accessing them
            if len(values) >= 4:
                # Extract the ADC value
                adc_value = int(values[3])
                
                # Get the current timestamp
                timestamp = time.time() - timestamp_0
                
                # Append the ADC value and timestamp to the list
                adc_values_with_timestamps.append((timestamp, adc_value))
                
                # Print the extracted values
                print(f"Timestamp: {timestamp}, ADC Value: {adc_value}")
            else:
                print(f"Unexpected data format: {line}")
        
        # Add a small delay to avoid overwhelming the serial port
        time.sleep(0.1)

except KeyboardInterrupt:
    # Convert the list of ADC values and timestamps to a NumPy array
    adc_values_array = np.array(adc_values_with_timestamps, dtype=[('timestamp', 'f8'), ('adc_value', 'i4')])
    
    # Save the NumPy array to a file
    np.save('tiptopf.npy', adc_values_array)
    
    # Close the serial connection when the script is interrupted
    ser.close()
    print("Serial connection closed.")
    print(f"Saved ADC values with timestamps to 'adc_values_with_timestamps_2.npy'.")