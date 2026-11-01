
# Railway Fare and Reservation Calculator

n = int(input("Enter number of passengers: "))

for i in range(n):
    print("\nPassenger", i + 1)

    name = input("Enter passenger name: ")
    age = int(input("Enter age: "))
    distance = int(input("Enter travel distance: "))

    print("1. Sleeper")
    print("2. AC")
    choice = int(input("Select travel class: "))

    # Distance based fare
    if distance <= 100:
        fare = distance * 2
    elif distance <= 500:
        fare = distance * 3
    else:
        fare = distance * 4

    # Travel class charges
    if choice == 1:
        fare = fare + 100
    elif choice == 2:
        fare = fare + 300
    else:
        print("Invalid class")
        continue

    # Age concession
    if age >= 60:
        fare = fare * 0.80

    # Reservation fee
    fare = fare + 50

    print("\nPassenger Name:", name)
    print("Total Fare: Rs.", round(fare, 2))

    # Cancellation
    cancel = input("Cancel ticket? (yes/no): ")

    if cancel == "yes":
        penalty = fare * 0.20
        refund = fare - penalty
        print("Cancellation Penalty: Rs.", round(penalty, 2))
        print("Refund Amount: Rs.", round(refund, 2))
    else:
        print("Ticket Confirmed")
