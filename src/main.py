import tkinter as tk
from tkinter import OptionMenu, Scale
from sorting_algos import SortingAlgos
from visualisation import Visualiser
from utility_funcs import generate_data

def visualiser():
    # Create the root window
    root = tk.Tk()
    root.title("Sorting Algo Visualizer")  # Set the title of the window

    # Create a canvas for drawing
    canvas = tk.Canvas(root, width=800, height=400)
    canvas.pack()

    # Create a dropdown menu for selecting sorting algorithms
    algorithm_choice = tk.StringVar(root)
    algorithm_choice.set("Merge Sort")  # Default sorting algorithm
    algorithm_menu = OptionMenu(root, algorithm_choice, "Merge Sort", "Bubble Sort", "Insertion Sort", "Selection Sort", "Quick Sort")
    algorithm_menu.pack()

    # Create a scale for adjusting sleep time
    sleep_time = Scale(root, from_=0.01, to=2, resolution=0.01, orient=tk.HORIZONTAL, label="Sleep Time (s)", length=200)
    sleep_time.set(0.1)  # Default sleep time
    sleep_time.pack()

    # Create an instance of Visualiser for visualization
    visualiser = Visualiser(canvas, root)

    # Create an instance of SortingAlgos for sorting algorithms
    sorting_algos = SortingAlgos(sleep_time.get(), visualiser)

    # Create an entry for specifying the array size
    array_size = tk.Entry(root)
    array_size.insert(0, "100")  # Default array size
    array_size.pack()

    # Define an empty list to store generated data
    data = []

    # Create a button to generate random data
    generate_button = tk.Button(root, text="Generate Data", command=lambda: generate_data(array_size.get(), data, visualiser))
    generate_button.pack()

    # Create a button to visualize the sorting process
    visualize_button = tk.Button(root, text="Visualize Sort", command=lambda: visualiser.visualize_sort(data, algorithm_choice.get(), sorting_algos))
    visualize_button.pack()

    # Start the GUI event loop
    root.mainloop()

# Call the visualiser function to run the GUI
visualiser()
