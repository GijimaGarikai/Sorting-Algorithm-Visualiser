**Sort Visualizer**

**Description:**

Sort Visualizer is a Python GUI application made with Tkinter that allows users to visualize various sorting algorithms in action. Users can select from a variety of sorting algorithms such as Merge Sort, Bubble Sort, Insertion Sort, Selection Sort, and Quick Sort. They can also adjust parameters like sleep time (delay between each step of the sorting algorithm) and input array size. The application provides a visual representation of the sorting process, making it easier for users to understand and analyze how different sorting algorithms work.

**Features:**

1. **Selection of Sorting Algorithms:** Users can choose from a dropdown menu of sorting algorithms to visualize. Supported algorithms include Merge Sort, Bubble Sort, Insertion Sort, Selection Sort, and Quick Sort.

2. **Adjustable Parameters:** Users can adjust parameters like sleep time to control the speed of the sorting visualization. They can also specify the size of the input array to be sorted.

3. **Real-time Visualization:** The application provides a real-time visual representation of the sorting process. As the sorting algorithm progresses, bars representing elements in the array are updated on the canvas, allowing users to see how the data is being sorted step by step.

4. **Random Data Generation:** Users can generate random data of specified size to be used as input for sorting algorithms. This feature allows users to test and observe the behavior of sorting algorithms with different datasets.

**Usage:**

1. Run the main script `main.py`:
   ```
   python main.py
   ```

2. The Sort Visualizer GUI will appear. Select a sorting algorithm from the dropdown menu, adjust parameters as needed, and click the "Generate Data" button to generate random data.

3. Click the "Visualize Sort" button to start visualizing the selected sorting algorithm with the generated data.

4. Observe the sorting process in real-time on the canvas. You can adjust the speed of visualization and generate new data to explore different scenarios.

**Credits:**

Sort Visualizer uses the following libraries and resources:
- Tkinter: Python's standard GUI (Graphical User Interface) toolkit.
- Random: Python's built-in module for generating random numbers.
- Sorting algorithms implementations: All but [quicksort](https://www.geeksforgeeks.org/quick-sort/) were from memory.
- [Justin Johnson's site](https://cs.stanford.edu/people/jcjohns/sorting.js/) for inspiration.

