from datetime import datetime

customer_name = input("Enter customer name: ")
total = 0
cart = []

while True:
    item = input("Enter item name (or 'done' to finish): ")
    if item.lower() == 'done':
        break

    price = float(input(f"Enter price of {item}: ₹"))
    quantity = int(input(f"Enter quantity of {item}: "))
    item_total = price * quantity

    cart.append((item, price, quantity, item_total))
    total += item_total

discount_percent = float(input("Enter discount percent (0 if none): "))
discount_amount = (discount_percent / 100) * total
final_total = total - discount_amount

now = datetime.now()
date_str = now.strftime("%Y-%m-%d %H:%M:%S")

with open("orders.txt", "a", encoding="utf-8") as file:

    file.write(f"\nSMARTCART BILL - {date_str}\n")

    file.write(f"Customer: {customer_name}\n")
    file.write("-------------------------------\n")

    for item, price, quantity, item_total in cart:
        file.write(f"- {item} x{quantity} @ ₹{price} = ₹{item_total}\n")

    file.write(f"\nSubtotal: ₹{total}")
    file.write(f"\nDiscount: {discount_percent}% (-₹{discount_amount:.2f})")
    file.write(f"\nFinal Total: ₹{final_total:.2f}")
    file.write("\n" + "-"*35 + "\n")

print("\n✅ Order saved successfully!")
print(f"Total after discount: ₹{final_total:.2f}")
