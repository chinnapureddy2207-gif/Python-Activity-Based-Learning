
# Progressive Electricity Billing

bills = []

months = ["January", "February", "March"]

for month in months:
    print("\n", month)
    units = int(input("Enter electricity units: "))

    # Calculate slab charges
    if units <= 100:
        bill = units * 1.5
    elif units <= 200:
        bill = 100 * 1.5 + (units - 100) * 2.5
    else:
        bill = 100 * 1.5 + 100 * 2.5 + (units - 200) * 4

    # Fixed charge
    bill = bill + 50

    # Surcharge
    bill = bill + bill * 0.05

    # Rebate
    if units <= 100:
        bill = bill - bill * 0.10

    bills.append(bill)

    print("Total Bill: Rs.", round(bill, 2))

# Compare monthly bills
print("\nMonthly Bill Comparison")

for i in range(len(bills)):
    print(months[i], ":", round(bills[i], 2))

# Identify unusual increase
for i in range(1, len(bills)):
    if bills[i] > bills[i-1] * 1.20:
        print(months[i], "- Unusual Increase")
    else:
        print(months[i], "- Normal Bill")
