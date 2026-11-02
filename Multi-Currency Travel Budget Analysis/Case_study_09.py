
# Multi-Currency Travel Budget Analysis

budget = float(input("Enter your total travel budget: "))

n = int(input("Enter number of expense categories: "))

expenses = []
total = 0

for i in range(n):
    print("\nExpense", i + 1)

    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))
    rate = float(input("Enter exchange rate: "))
    fee = float(input("Enter conversion fee percentage: "))

    converted = amount * rate
    conversion_fee = converted * fee / 100
    final_amount = converted + conversion_fee

    expenses.append((category, final_amount))
    total += final_amount

# Find largest expense category

largest = expenses[0]

for expense in expenses:
    if expense[1] > largest[1]:
        largest = expense

# Display results

print("\n----- TRAVEL BUDGET REPORT -----")

for category, amount in expenses:
    print(category, ":", round(amount, 2))

print("Total Spending:", round(total, 2))
print("Travel Budget:", round(budget, 2))

if total > budget:
    print("Status: Budget Exceeded")
    print("Extra Amount:", round(total - budget, 2))
else:
    print("Status: Within Budget")
    print("Remaining Budget:", round(budget - total, 2))

print("Largest Expense Category:", largest[0])
print("Largest Expense Amount:", round(largest[1], 2))
