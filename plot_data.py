import numpy as np
import plotly.graph_objs as go
import plotly.io as pio

# Load the NumPy array from the file
adc_values_array = np.load('adc_values_with_timestamps.npy')

# Extract timestamps and ADC values
timestamps = adc_values_array['timestamp']
adc_values = adc_values_array['adc_value']

# Create a Plotly figure
fig = go.Figure()

# Add a trace for the ADC values
fig.add_trace(go.Scatter(x=timestamps, y=adc_values, mode='lines', name='ADC Value'))

# Set the title and labels
fig.update_layout(
    title='ADC Values Over Time',
    xaxis_title='Time',
    yaxis_title='ADC Value'
)

# Show the plot
pio.show(fig)