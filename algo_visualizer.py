import tkinter as tk
import random
import time

# Create the main Tkinter window
root = tk.Tk()
root.title("Sorting Algorithm Visualization")
root.geometry("900x470")

# Canvas for drawing bars
canvas = tk.Canvas(root, width=900, height=400, bg="white")
canvas.pack()

# Generate random array
num_elements = 50
arr = [random.randint(10, 100) for _ in range(num_elements)]
bar_width = 900 / num_elements

# Draw bars representing the array
bars = []
for i in range(num_elements):
    x0 = i * bar_width
    y0 = 400 - arr[i] * 3
    x1 = (i + 1) * bar_width
    y1 = 400
    bar = canvas.create_rectangle(x0, y0, x1, y1, fill="grey")
    bars.append(bar)

# Function to update the visualization
def update_canvas(arr):
    for i in range(num_elements):
        x0 = i * bar_width
        y0 = 400 - arr[i] * 3
        x1 = (i + 1) * bar_width
        y1 = 400
        canvas.coords(bars[i], x0, y0, x1, y1)
    root.update()
    time.sleep(0.01)

# Sorting Algorithms
def bubble_sort():
    global arr
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                update_canvas(arr)

def selection_sort():
    global arr
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        update_canvas(arr)

def insertion_sort():
    global arr
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        update_canvas(arr)

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        update_canvas(arr)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
        update_canvas(arr)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            update_canvas(arr)
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    update_canvas(arr)
    return i + 1

def merge_sort(arr, l, r):
    if l < r:
        mid = (l + r) // 2
        merge_sort(arr, l, mid)
        merge_sort(arr, mid + 1, r)
        merge(arr, l, mid, r)
        update_canvas(arr)

def merge(arr, l, mid, r):
    left = arr[l:mid + 1]
    right = arr[mid + 1:r + 1]
    i = j = 0
    k = l
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
        update_canvas(arr)

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
        update_canvas(arr)

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
        update_canvas(arr)


def shell_sort():
    global arr
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
            update_canvas(arr)
        gap //= 2

def gnome_sort():
    global arr
    i = 0
    while i < len(arr):
        if i == 0 or arr[i] >= arr[i - 1]:
            i += 1
        else:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1
        update_canvas(arr)

def comb_sort():
    global arr
    n = len(arr)
    gap = n
    shrink = 1.3
    sorted = False
    while not sorted:
        gap = int(gap / shrink)
        if gap <= 1:
            gap = 1
            sorted = True
        i = 0
        while i + gap < n:
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                sorted = False
            update_canvas(arr)
            i += 1

def pancake_sort():
    global arr
    def flip(k):
        global arr
        arr[:k+1] = arr[:k+1][::-1]

    n = len(arr)
    for i in range(n, 1, -1):
        max_idx = arr.index(max(arr[:i]))
        if max_idx != i - 1:
            flip(max_idx)
            update_canvas(arr)
            flip(i - 1)
            update_canvas(arr)

def cocktail_shaker_sort():
    global arr
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1
    while swapped:
        swapped = False
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
                update_canvas(arr)
        if not swapped:
            break
        swapped = False
        end -= 1
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
                update_canvas(arr)
        start += 1

# Reset function to shuffle array
def reset_array():
    global arr
    arr = [random.randint(10, 100) for _ in range(num_elements)]
    update_canvas(arr)

# Buttons for Sorting Algorithms
btn_selection = tk.Button(root, text="Selection Sort", command=selection_sort)
btn_selection.pack(side=tk.LEFT, padx=2)

btn_pancake = tk.Button(root, text="Pancake Sort", command=pancake_sort)
btn_pancake.pack(side=tk.LEFT, padx=2)

btn_insertion = tk.Button(root, text="Insertion Sort", command=insertion_sort)
btn_insertion.pack(side=tk.LEFT, padx=2)

btn_merge = tk.Button(root, text="Merge Sort", command=lambda: merge_sort(arr, 0, len(arr)-1))
btn_merge.pack(side=tk.LEFT, padx=2)

btn_quick = tk.Button(root, text="Quick Sort", command=lambda: quick_sort(arr, 0, len(arr)-1))
btn_quick.pack(side=tk.LEFT, padx=2)

btn_shell = tk.Button(root, text="Shell Sort", command=shell_sort)
btn_shell.pack(side=tk.LEFT, padx=2)

btn_comb = tk.Button(root, text="Comb Sort", command=comb_sort)
btn_comb.pack(side=tk.LEFT, padx=2)

btn_bubble = tk.Button(root, text="Bubble Sort", command=bubble_sort)
btn_bubble.pack(side=tk.LEFT, padx=2)

btn_gnome = tk.Button(root, text="Gnome Sort", command=gnome_sort)
btn_gnome.pack(side=tk.LEFT, padx=2)

btn_cocktail = tk.Button(root, text="Cocktail Shaker Sort", command=cocktail_shaker_sort)
btn_cocktail.pack(side=tk.LEFT, padx=2)

btn_reset = tk.Button(root, text="Reset", command=reset_array)
btn_reset.pack(side=tk.RIGHT, padx=5)

# Run Tkinter event loop
root.mainloop()
