"""
DATA GHOST: PROJECT #5 - INTEGRITY SORT
Domain: Data Engineering / DSA
Description: Implements Bubble Sort to demonstrate O(n^2) complexity and data integrity.
Goal: Prove the "Swap" logic while maintaining a noise-free output.
"""

import numpy as np
import pandas as pd
import time

# --- PHASE 2: DATA ISOLATION (NumPy) ---
# Generating a small vector to keep the "Swap" logic visible and clear.
data_size = 10
# Using NumPy to create a 'Messy Column'
database = np.random.randint(1, 100, size=data_size)
original_data = database.copy() # Saving the 'Before' state for the report

# --- PHASE 3: REASONING STEP (DSA: Bubble Sort) ---
def bubble_sort(arr):
    n = len(arr)
    start_time = time.time()
    
    # Outer loop: The number of times we pass through the shelf
    for i in range(n):
        # Inner loop: Comparing adjacent 'books'
        for j in range(0, n - i - 1):
            # The "Swap" Logic (Atomicity check)
            if arr[j] > arr[j + 1]:
                # Temporary storage swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
    end_time = time.time()
    return arr, (end_time - start_time)

# --- THE EXECUTION ---
sorted_data, duration = bubble_sort(database)

# --- THE REPORT (Pandas) ---
# Organizing the 'Before' and 'After' vectors into a structured view.
report_card = {
    "Status": ["Unsorted Vector", "Sorted Vector", "Complexity", "Execution Time (s)"],
    "Data Ghost Output": [str(list(original_data)), str(list(sorted_data)), "O(n^2)", f"{duration:.6f}"]
}

df = pd.DataFrame(report_card)

# --- THE TERMINAL OUTPUT ---
print("\n" + "="*40)
print("  DATA GHOST: PROJECT #5 - SORT  ")
print("="*40)
print(df.to_string(index=False))
<<<<<<< HEAD

=======
>>>>>>> 4d1b962 (Migration complete: Environment cleaned and files secured)
