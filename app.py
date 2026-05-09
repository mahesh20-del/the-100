import streamlit as st

# 1. THE ENGINE (Your Algebra)
def calculate_p(a, d_percent):
    d = 1 - (d_percent / 100)
    return a * d

# 2. THE WEB INTERFACE (The Dashboard)
st.title("💀☠️👻👽👾🤖 Price Optimization Engine")
st.write("Input your parameters below to calculate the final value.")

# Create two columns like a pro dashboard
col1, col2 = st.columns(2)

with col1:
    actual_price = st.number_input("Actual Price (a)", min_value=0.0, value=100.0)

with col2:
    discount_val = st.number_input("Discount % (d)", min_value=0.0, max_value=100.0, value=20.0)

# 3. THE EXECUTION (The Stress Test)
final_p = calculate_p(actual_price, discount_val)

# 4. THE OUTPUT (The "Result View")
st.divider()
st.metric(label="Final Discounted Price (p)", value=f"${final_p:.2f}")

if st.button("Run System Check"):
    st.success(f"Algorithm p = {actual_price} * (1 - {discount_val/100}) executed successfully.")
