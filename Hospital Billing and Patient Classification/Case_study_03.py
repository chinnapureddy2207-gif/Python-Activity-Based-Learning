
# Hospital Billing and Patient Classification

name = input("Enter patient name: ")
consultation = int(input("Enter consultation charges: "))
diagnostic = int(input("Enter diagnostic charges: "))
treatment = int(input("Enter treatment charges: "))
payment = int(input("Enter payment amount: "))

# Calculate total bill
total = consultation + diagnostic + treatment

# Apply concession
if total >= 5000:
    concession = total * 0.10
else:
    concession = 0

bill = total - concession

print("\nPatient Name:", name)
print("Total Bill:", bill)
print("Concession:", concession)

# Validate billing
if consultation < 0 or diagnostic < 0 or treatment < 0 or payment < 0:
    print("Invalid Billing Details")

elif payment >= bill:
    print("Payment Status: Fully Paid")

elif payment > 0:
    print("Payment Status: Partially Paid")

else:
    print("Payment Status: Not Paid")

# Patient Classification
if bill <= 2000:
    print("Patient Category: Low Cost")
elif bill <= 5000:
    print("Patient Category: Medium Cost")
else:
    print("Patient Category: High Cost")
