import numpy as np
import pandas as pd
import mplfinance as mpf

# --- THE DATA GENERATOR ---
# We simulate 20 "Trading Days" of Data Integrity
days = 20
data = {
    'Open':  np.random.randint(50, 70, size=days),
    'High':  np.random.randint(71, 90, size=days),
    'Low':   np.random.randint(30, 49, size=days),
    'Close': np.random.randint(50, 70, size=days)
}

# Create the DataFrame and set a Date index (required for Candles)
df = pd.DataFrame(data)
df.index = pd.date_range(start='2026-05-01', periods=days, freq='D')

# --- THE VISUALIZATION ---
# Using the "charles" style for that classic Green/Red or Yellow look
mpf.plot(df, type='candle', style='charles', 
         title='DATA GHOST: OHLC INTEGRITY',
         ylabel='Value Magnitude',
         savefig='ghost_candles.png')

print("Candlestick Chart generated: ghost_candles.png")
