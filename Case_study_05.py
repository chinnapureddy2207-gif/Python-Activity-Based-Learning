
# Mobile Plan Cost Optimization

budget = int(input("Enter your budget: "))
usage = int(input("Enter required data in GB: "))
days = int(input("Enter required validity days: "))

plans = [
    ["Plan A", 199, 2, 28],
    ["Plan B", 299, 3, 56],
    ["Plan C", 399, 5, 84]
]

best_plan = ""
min_cost = 99999

for p in plans:
    name = p[0]
    price = p[1]
    data = p[2]
    validity = p[3]

    if data >= usage and validity >= days:
        if price <= budget:
            print(name, "Eligible")

            if price < min_cost:
                min_cost = price
                best_plan = name
        else:
            print(name, "Over Budget")
    else:
        print(name, "Not Suitable")

# Display best plan
print("\nBest Mobile Plan")

if best_plan != "":
    print("Plan:", best_plan)
    print("Total Cost: Rs.", min_cost)
    print("Remaining Budget: Rs.", budget - min_cost)
else:
    print("No Eligible Plan Found")
