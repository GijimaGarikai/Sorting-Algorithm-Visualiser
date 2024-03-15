import time

class SortingAlgos:
    def __init__(self, sleep_time, visualiser):
        # Constructor to initialize SortingAlgos object
        self.sleep_time = float(sleep_time)  # Convert sleep time to float
        self.visualiser = visualiser  # Reference to Visualiser object

    def merge_sort(self, arr, start, end):
        # Merge sort algorithm
        if end <= start:
            return
        mid = (start + end) // 2
        self.merge_sort(arr, start, mid)  # Recursively sort left half
        self.merge_sort(arr, mid + 1, end)  # Recursively sort right half
        self.merge(arr, start, mid, end)  # Merge sorted halves
        self.visualiser.draw_bars(arr)  # Draw bars after each step
        time.sleep(self.sleep_time)  # Delay visualization by sleep time

    def merge(self, arr, start, mid, end):
        # Merge two sorted subarrays
        temp = [0] * (end - start + 1)
        i = start
        j = mid + 1
        k = 0
        while i <= mid and j <= end:
            if arr[i] < arr[j]:
                temp[k] = arr[i]
                i += 1
            else:
                temp[k] = arr[j]
                j += 1
            k += 1
        while i <= mid:
            temp[k] = arr[i]
            i += 1
            k += 1
        while j <= end:
            temp[k] = arr[j]
            j += 1
            k += 1
        for i in range(len(temp)):
            arr[start + i] = temp[i]

    def bubble_sort(self, arr):
        # Bubble sort algorithm
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    self.visualiser.draw_bars(arr)  # Draw bars after each step
                    time.sleep(self.sleep_time)  # Delay visualization by sleep time

    def insertion_sort(self, arr):
        # Insertion sort algorithm
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
            self.visualiser.draw_bars(arr)  # Draw bars after each step
            time.sleep(self.sleep_time)  # Delay visualization by sleep time

    def selection_sort(self, arr):
        # Selection sort algorithm
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            self.visualiser.draw_bars(arr)  # Draw bars after each step
            time.sleep(self.sleep_time)  # Delay visualization by sleep time

    def partition(self, arr, low, high):
        # Helper function for quick sort
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                self.visualiser.draw_bars(arr)  # Draw bars after each swap
                time.sleep(self.sleep_time)  # Delay visualization by sleep time
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quick_sort(self, arr, low, high):
        # Quick sort algorithm
        if low < high:
            pi = self.partition(arr, low, high)
            self.quick_sort(arr, low, pi - 1)
            self.quick_sort(arr, pi + 1, high)
