import random

def generate_data(array_size, data, visualiser):
    # Generate random data for visualization
    data_size = int(array_size)  # Convert array size to integer
    new_data = [random.randint(1, 200) for _ in range(data_size)]  # Generate random data
    data[:] = new_data  # Update the original data list with the new data
    visualiser.draw_bars(data)  # Draw bars representing the new data on the canvas
