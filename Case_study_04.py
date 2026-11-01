
# Employee Payroll and Deduction Analysis

name = input("Enter employee name: ")

basic = float(input("Enter basic salary: "))
allowance = float(input("Enter allowances: "))
overtime = float(input("Enter overtime amount: "))
incentive = float(input("Enter incentives: "))

# Calculate gross salary
gross = basic + allowance + overtime + incentive

# Calculate deductions
if gross <= 20000:
    deduction = gross * 0.05
elif gross <= 40000:
    deduction = gross * 0.10
else:
    deduction = gross * 0.15

# Calculate net salary
net = gross - deduction

# Salary Statement
print("\n----- Salary Statement -----")
print("Employee Name:", name)
print("Basic Salary:", basic)
print("Allowances:", allowance)
print("Overtime:", overtime)
print("Incentives:", incentive)
print("Gross Salary:", gross)
print("Deduction:", deduction)
print("Net Salary:", net)
print("----------------------------")
