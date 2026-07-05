# Student Grade Analyzer


student_name = input("Enter Student Name: ")
roll_number = int(input("Enter Roll Number: "))

print("\nEnter Marks for 5 Subjects")

mark1 = float(input("Subject 1: "))
mark2 = float(input("Subject 2: "))
mark3 = float(input("Subject 3: "))
mark4 = float(input("Subject 4: "))
mark5 = float(input("Subject 5: "))

# Calculate Total and Percentage
total = mark1 + mark2 + mark3 + mark4 + mark5
percentage = total / 5

# Determine Grade
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "F"

# Determine Pass/Fail
if percentage >= 40:
    result = "PASS"
else:
    result = "FAIL"

# Display Report Card
print("\n=========REPORT CARD============")
print("Student Name :", student_name)
print("Roll Number  :", roll_number)
print("---------------------------------")
print("Subject 1 :", mark1)
print("Subject 2 :", mark2)
print("Subject 3 :", mark3)
print("Subject 4 :", mark4)
print("Subject 5 :", mark5)
print("---------------------------------")
print("Total Marks      :", total, "/ 500")
print("Percentage       :", percentage, "%")
print("Grade            :", grade)
print("Result           :", result)
print("===================================")