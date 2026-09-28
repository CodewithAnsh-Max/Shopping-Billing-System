
import streamlit as st

st.set_page_config(page_title="Shopping Billing System", page_icon="🛒")

st.title("🛒 Shopping Billing System")

customer = st.text_input("Customer Name")
phone = st.text_input("Phone Number")

qty = st.number_input("Quantity", min_value=1)
price = st.number_input("Price per Item", min_value=0.0)
discount = st.slider("Discount (%)", 0, 50, 0)

if st.button("Generate Bill"):
    subtotal = qty * price
    discount_amount = subtotal * discount / 100
    after_discount = subtotal - discount_amount
    gst = after_discount * 0.18
    total = after_discount + gst

    st.success(f"Grand Total: ₹{total:.2f}")