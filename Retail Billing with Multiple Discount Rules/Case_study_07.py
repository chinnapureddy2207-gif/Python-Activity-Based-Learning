
# Retail Billing System

n = int(input("Enter number of products: "))

total = 0

for i in range(n):
    print("\nProduct", i + 1)

    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    category = input("Enter category (food/electronics): ")

    amount = price * quantity

    # Category based tax
    if category == "food":
        tax = amount * 0.05
    else:
        tax = amount * 0.18

    bill = amount + tax

    print("Product:", name)
    print("Amount:", amount)
    print("Tax:", tax)
    print("Total:", bill)

    total = total + bill

# Discount calculation
if total >= 5000:
    discount = total * 0.20
elif total >= 2000:
    discount = total * 0.10
else:
    discount = 0

# Maximum discount limit
if discount > 1000:
    discount = 1000

final_bill = total - discount

# Final Invoice
print("\n----- FINAL INVOICE -----")
print("Total Amount:", round(total, 2))
print("Discount:", round(discount, 2))
print("Final Bill:", round(final_bill, 2))
print("-------------------------")
