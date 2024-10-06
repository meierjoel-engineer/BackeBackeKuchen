import numpy as np
import plotly.graph_objs as go
import plotly.io as pio

# Load the NumPy array from the file
weights_array = np.load('weights.npy')

# Create a Plotly figure
fig = go.Figure()

# Add a trace for the weights
fig.add_trace(go.Scatter(y=weights_array, mode='lines', name='Weight'))

# Set the title and labels
fig.update_layout(
    title='Weight Data Over Time',
    xaxis_title='Time',
    yaxis_title='Weight (kg)'
)

# Show the plot
pio.show(fig)
