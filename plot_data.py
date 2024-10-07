import numpy as np
import plotly.graph_objs as go
import plotly.io as pio

# Load the first NumPy array from the file
adc_values_array_1 = np.load('tiptopf.npy')

# Extract timestamps and ADC values for the first dataset
timestamps_1 = adc_values_array_1['timestamp']
adc_values_1 = adc_values_array_1['adc_value']

# Load the second NumPy array from the file
adc_values_array_2 = np.load('belastend_mit_Pfeil_2.npy')

# Extract timestamps and ADC values for the second dataset
timestamps_2 = adc_values_array_2['timestamp']
adc_values_2 = adc_values_array_2['adc_value']

# Define the maximum ADC value for a 24-bit ADC
MAX_ADC_VALUE = 2**24 - 1

# Scale the ADC values to percentages for both datasets
adc_percentages_1 = (adc_values_1 / MAX_ADC_VALUE) * 100
adc_percentages_2 = (adc_values_2 / MAX_ADC_VALUE) * 100

# Create a Plotly figure
fig = go.Figure()

# Add a trace for the first dataset
fig.add_trace(go.Scatter(x=timestamps_1, y=adc_percentages_1, mode='lines', name='ADC Percentage 1'))

# # Add a trace for the second dataset
# fig.add_trace(go.Scatter(x=timestamps_2, y=adc_percentages_2, mode='lines', name='ADC Percentage 2'))

# Set the title and labels
fig.update_layout(
    title='ADC Values as Percentage Over Time',
    xaxis_title='Time',
    yaxis_title='ADC Percentage (%)'
)

# Show the plot
pio.show(fig)