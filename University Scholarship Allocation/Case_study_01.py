
# University Scholarship Allocation

students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nEnter Student Details")

    name = input("Enter student name: ")
    marks = int(input("Enter aggregate marks: "))
    subject = int(input("Enter subject marks: "))
    attendance = int(input("Enter attendance: "))
    income = int(input("Enter family income: "))

    if marks >= 75 and subject >= 40 and attendance >= 75 and income <= 200000:
        students.append([name, marks, attendance])
        print("Eligible")
    else:
        print("Not Eligible")

# Rank students
students.sort(key=lambda x: (x[1], x[2]), reverse=True)

print("\nScholarship Ranking")

rank = 1
for s in students:
    print(rank, s[0], s[1])
    rank += 1
