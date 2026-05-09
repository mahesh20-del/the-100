import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt

# --- THE ALGORITHM ---
def linear_search(arr, x):
    start_time = time.time()
    for i in range(len(arr)):
        if arr[i] == x:
            return time.time() - start_time
    return time.time() - start_time

# --- THE SIMULATION ---
# We are testing different "Loads" (Data Sizes)
sizes = [10000, 50000, 100000, 500000, 1000000]
results = []

print("Starting Stress Test...")
for s in sizes:
    test_data = np.random.randint(0, 1000, size=s)
    # We force a "Worst Case" by searching for a number not in the list
    duration = linear_search(test_data, -1) 
    results.append(duration)
    print(f"Size {s} complete.")

# --- THE VISUALIZATION ---
plt.figure(figsize=(10, 6))
plt.style.use('dark_background') # The Ghost Aesthetic
plt.plot(sizes, results, color='#FFFF00', marker='o', linestyle='-')

plt.title("Mechanical Stress Test of Linear Search")
plt.xlabel("Data Points (n)")
plt.ylabel("Time Taken (seconds)")
plt.grid(True, linestyle='--', alpha=0.5)

# Save the plot so you can view it
plt.savefig("my_stress_test.png")
print("\nSuccess! Plot saved as 'my_stress_test.png'")
