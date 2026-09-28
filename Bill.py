import os
from datetime import datetime

# Create bills folder
os.makedirs("bills", exist_ok=True)

print("=" * 45)
print("      SHOPPING BILLING SYSTEM")
print("=" * 45)

# Customer Details
customer = input("Customer Name: ")
phone = input("Phone Number: ")

cart = []
subtotal = 0

while True:
    print("\nAdd Product")

    item = input("Product Name: ")
    qty = int(input("Quantity: "))
    price = float(input("Price per Item: ₹"))

    total = qty * price
    subtotal += total

    cart.append([item, qty, price, total])

    choice = input("Add another product? (y/n): ").lower()
    if choice != "y":
        break

# Discount
discount = float(input("\nDiscount (%) : "))

discount_amount = subtotal * discount / 100
after_discount = subtotal - discount_amount

gst = after_discount * 0.18
grand_total = after_discount + gst

# Bill
bill = "\n" + "=" * 45 + "\n"
bill += "        SHOPPING BILL\n"
bill += "=" * 45 + "\n"

bill += f"Customer : {customer}\n"
bill += f"Phone    : {phone}\n"
bill += f"Date     : {datetime.now().strftime('%d-%m-%Y %H:%M')}\n"

bill += "-" * 45 + "\n"
bill += "{:<15}{:<8}{:<10}{:<10}\n".format("Item","Qty","Price","Total")
bill += "-" * 45 + "\n"

for i in cart:
    bill += "{:<15}{:<8}{:<10.2f}{:<10.2f}\n".format(i[0], i[1], i[2], i[3])

bill += "-" * 45 + "\n"
bill += f"Subtotal      : ₹{subtotal:.2f}\n"
bill += f"Discount({discount}%): -₹{discount_amount:.2f}\n"
bill += f"GST (18%)     : ₹{gst:.2f}\n"
bill += "-" * 45 + "\n"
bill += f"Grand Total   : ₹{grand_total:.2f}\n"
bill += "=" * 45 + "\n"

print(bill)

# Save Bill
filename = f"bills/{customer}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

with open(filename, "w", encoding="utf-8") as f:
    f.write(bill)
print(f"Bill saved successfully in: {filename}")