"""
DATA GHOST: PROJECT #6 - VOICE SCALER
Domain: Data Science / NLP
Description: Analyzes word-length distribution using Standard Deviation to quantify tone variety.
Goal: Categorize text "complexity" through statistical variance.
"""

import numpy as np
import pandas as pd

# --- PHASE 2: DATA ISOLATION (Feature Extraction) ---
text_input = "The Data Ghost protocol ensures technical precision by merging analytical rigor with professional ghostwriting."
words = text_input.split()

# --- PHASE 3: REASONING STEP (Statistical Modeling) ---
def analyze_voice(word_list):
    # Mapping strings to numerical lengths (Vectorization)
    lengths = np.array([len(word) for word in word_list])
    
    # Calculating Statistical KPIs
    avg_length = np.mean(lengths)
    variety_score = np.std(lengths) 
    
    return avg_length, variety_score

# --- THE EXECUTION ---
mean_val, variety_val = analyze_voice(words)

# --- THE REPORT (Pandas) ---
report_card = {
    "Metric": ["Total Words", "Avg Word Length", "Variety Score (StdDev)", "DS Logic"],
    "Data Ghost Output": [len(words), f"{mean_val:.2f}", f"{variety_val:.2f}", "Standard Deviation"]
}

df = pd.DataFrame(report_card)

# --- THE TERMINAL OUTPUT ---
print("\n" + "="*45)
print("  DATA GHOST: PROJECT #6 - VOICE SCALER  ")
print("="*45)
print(df.to_string(index=False))

# --- LOGIC GATE: TONE CLASSIFICATION ---
if variety_val > 2.0:
    print("\n[Result]: High Variety Detected - Dynamic & Engaging Tone")
else:
    print("\n[Result]: Low Variety Detected - Consistent & Direct Tone")
print("="*45)
