
# Manufacturing Cost and Profitability Analysis

name = input("Enter product name: ")

material = float(input("Enter material cost: "))
labour = float(input("Enter labour charges: "))
wastage = float(input("Enter wastage cost: "))
machine = float(input("Enter machine cost: "))
selling = float(input("Enter selling price: "))
target = float(input("Enter profit target: "))

# Calculate total cost
total = material + labour + wastage + machine

# Calculate profit
profit = selling - total

# Display details
print("\n----- Manufacturing Report -----")
print("Product Name:", name)
print("Material Cost:", material)
print("Labour Charges:", labour)
print("Wastage Cost:", wastage)
print("Machine Cost:", machine)
print("Total Cost:", total)
print("Selling Price:", selling)
print("Profit:", profit)

# Check profit target
if profit >= target:
    print("Production Target Achieved")
else:
    print("Production Target Not Achieved")

if profit > 0:
    print("Result: Profit")
elif profit == 0:
    print("Result: No Profit No Loss")
else:
    print("Result: Loss")
