
# Campus Event Financial Planning

print("----- CAMPUS EVENT FINANCIAL PLANNING -----")

# Get event expenses
venue = float(input("Enter venue cost: "))
equipment = float(input("Enter equipment cost: "))
catering = float(input("Enter catering cost: "))
transport = float(input("Enter transport cost: "))
certificate = float(input("Enter certificate cost per participant: "))

# Get financial details
participants = int(input("Enter expected number of participants: "))
registration_fee = float(input("Enter registration fee per participant: "))
sponsorship = float(input("Enter sponsorship amount: "))

# Calculate costs
fixed_cost = venue + equipment + transport
certificate_cost = certificate * participants
catering_cost = catering * participants

total_cost = fixed_cost + certificate_cost + catering_cost

# Calculate contributions
participant_contribution = participants * registration_fee

total_funds = participant_contribution + sponsorship

# Calculate sponsorship shortfall
shortfall = total_cost - total_funds

# Calculate break-even registration count
variable_cost = catering + certificate

if registration_fee > variable_cost:
    break_even = (fixed_cost - sponsorship) / (registration_fee - variable_cost)

    if break_even < 0:
        break_even = 0

    break_even = int(break_even)

    if (fixed_cost - sponsorship) > 0:
        break_even += 1

else:
    break_even = -1

# Display report
print("\n----- EVENT FINANCIAL REPORT -----")

print("Fixed Cost:", fixed_cost)
print("Total Catering Cost:", catering_cost)
print("Total Certificate Cost:", certificate_cost)
print("Total Event Cost:", total_cost)

print("Participant Contributions:", participant_contribution)
print("Sponsorship Amount:", sponsorship)
print("Total Available Funds:", total_funds)

if shortfall > 0:
    print("Sponsorship Shortfall:", shortfall)
else:
    print("Surplus Amount:", abs(shortfall))

if break_even == -1:
    print("Break-even is not possible with this registration fee.")
else:
    print("Minimum Registrations Required:", break_even)
