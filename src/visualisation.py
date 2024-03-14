class Visualiser:
    def __init__(self, canvas, root):
        # Initialize the Visualiser object with canvas and root attributes
        self.canvas = canvas  # Canvas widget for drawing bars
        self.root = root  # Root window for updating display

    def visualize_sort(self, data, choice, algos):
        # Visualize the sorting process based on the selected algorithm
        selected_sort = choice
        if selected_sort == "Merge Sort":
            algos.merge_sort(data, 0, len(data) - 1)  # Call merge sort algorithm
        elif selected_sort == "Bubble Sort":
            algos.bubble_sort(data)  # Call bubble sort algorithm
        elif selected_sort == "Insertion Sort":
            algos.insertion_sort(data)  # Call insertion sort algorithm
        elif selected_sort == "Selection Sort":
            algos.selection_sort(data)  # Call selection sort algorithm
        elif selected_sort == "Quick Sort":
            algos.quick_sort(data, 0, len(data) - 1)  # Call quick sort algorithm

    def draw_bars(self, data):
        # Draw bars representing data on the canvas
        self.canvas.delete("all")  # Clear the canvas
        canvas_width = 800  # Canvas width
        canvas_height = 400  # Canvas height
        bar_width = canvas_width / len(data)  # Width of each bar
        for i, height in enumerate(data):
            x0 = i * bar_width  # Left x-coordinate of the bar
            y0 = canvas_height  # Bottom y-coordinate of the bar
            x1 = (i + 1) * bar_width  # Right x-coordinate of the bar
            y1 = canvas_height - height * 2  # Top y-coordinate of the bar (scaled based on data)
            # Draw a rectangle representing the bar
            self.canvas.create_rectangle(x0, y0, x1, y1, fill="blue")
        self.root.update()  # Update the display to show the drawn bars
