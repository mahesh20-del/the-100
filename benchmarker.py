<<<<<<< HEAD
# ---------------------------------------------------------
# The Data Ghost Protocol: Project #4
# Title: Linear Search Algorithm & Large-Scale Data Simulation
# Goal: Analyze Worst-Case Time Complexity using NumPy & Pandas.
# ---------------------------------------------------------
=======
>>>>>>> 4d1b962 (Migration complete: Environment cleaned and files secured)
import numpy as np
import pandas as pd
import time

# --- THE DATA GENERATOR (NumPy) ---
# Creating 100,000 random numbers. This is our "Haystack".
data_size = 100000
database = np.random.randint(1000, 10000, size=data_size)

# Picking the very last item as our "Needle" to test the Worst Case.
target = database[-1]

# --- THE ALGORITHM (DSA: Linear Search) ---
def linear_search(arr, x):
    start_time = time.time()
    
    # The "One-by-One" loop
    for i in range(len(arr)):
        if arr[i] == x:
            end_time = time.time()
            return i, (end_time - start_time)
            
    return -1, 0

# --- THE EXECUTION ---
index_found, duration = linear_search(database, target)

# --- THE REPORT (Pandas) ---
report_card = {
    "Project Metric": ["Search Type", "Data Points", "Target ID", "Time Taken (s)"],
    "Value": ["Linear Search", data_size, target, f"{duration:.6f}"]
}

df = pd.DataFrame(report_card)

print("\n" + "="*30)
print("  DATA GHOST: PROJECT #4  ")
print("="*30)
print(df)
