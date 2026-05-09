import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt

# --- PHASE 2: DATA ISOLATION (NumPy) ---
data_size = 10
database = np.random.randint(1, 100, size=data_size)
original_data = database.copy() 

# --- PHASE 3: REASONING STEP (DSA: Bubble Sort) ---
def bubble_sort(arr):
    n = len(arr)
    start_time = time.time()
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    end_time = time.time()
    return arr, (end_time - start_time)

# --- THE EXECUTION ---
sorted_data, duration = bubble_sort(database)

# --- THE REPORT (Pandas) ---
report_card = {
    "Status": ["Unsorted Vector", "Sorted Vector", "Complexity", "Execution Time (s)"],
    "Data Ghost Output": [str(list(original_data)), str(list(sorted_data)), "O(n^2)", f"{duration:.6f}"]
}
df = pd.DataFrame(report_card)
print(df.to_string(index=False))

# --- THE VISUALIZATION (Matplotlib) ---
plt.figure(figsize=(10, 5))
plt.style.use('dark_background')

# Plotting the "Before" vs "After"
x_axis = np.arange(data_size)

plt.bar(x_axis - 0.2, original_data, width=0.4, label='Unsorted (Raw)', color='gray', alpha=0.6)
plt.bar(x_axis + 0.2, sorted_data, width=0.4, label='Sorted (Integrity)', color='yellow')

plt.title("PROJECT #5: DATA INTEGRITY VISUALIZATION", color='yellow', fontsize=14)
plt.xlabel("Vector Position", color='white')
plt.ylabel("Value (Magnitude)", color='white')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.3)

plt.savefig("integrity_sort_view.png")
print("\n" + "="*40)
print(" VISUAL SAVED: integrity_sort_view.png ")
print("="*40)
