# Import necessary modules
import os
import time
import csv

# Bubble Sort Implementation
def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Merge Sort Implementation
def merge_sort(arr):
    # If array is of length 1 or less, it's already sorted
    if len(arr) > 1:
        mid = len(arr)//2
        # Create temp arrays
        L = arr[:mid]
        R = arr[mid:]

        # Copy data to temp arrays L[] and R[]
        merge_sort(L)
        merge_sort(R)

        # Merge the temp arrays back into arr[]
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        # CVhecking if any element was right
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

# Function to test sorting algorithms
def test_algorithms(filepath):
    # Read numbers from file
    with open(filepath, 'r') as f:
        numbers = [int(x) for x in f.read().split()]

    # Display file info
    print(f"\nTesting file: {os.path.basename(filepath)}")
    print(f"List length: {len(numbers)}")

    # Bubble Sort
    arr1 = numbers.copy()
    start = time.time()
    bubble_sort(arr1)
    bubble_time = time.time() - start

    # Merge Sort
    arr2 = numbers.copy()
    start = time.time()
    merge_sort(arr2)
    merge_time = time.time() - start

    # Display results
    print(f"Bubble Sort time: {bubble_time:.6f}s")
    print(f"Merge Sort time: {merge_time:.6f}s")

    return len(numbers), bubble_time, merge_time

# Locate data files
data_folder = "data files"
files = sorted([os.path.join(data_folder, f) for f in os.listdir(data_folder) if f.endswith(".dat")])

# Check if files are found
if not files:
    print("⚠️ No data files found in the 'data files' folder.")
else:
    results = [] # Store Results

    # Test each file
    for file in files:
        length, bubble_time, merge_time = test_algorithms(file)
        results.append([os.path.basename(file), length, round(bubble_time, 6), round(merge_time, 6)])

    # Save results to CSV
    with open("sorting_results.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["File Name", "List Length", "Bubble Sort Time (seconds)", "Merge Sort Time (seconds)"])
        writer.writerows(results)

    print("\n✅ Results saved to 'sorting_results.csv'") # End of Program
