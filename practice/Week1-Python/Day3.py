# Employee Bonus Eligibility System

# Taking input from the user
employee_name = input("Enter Employee Name: ")
salary = float(input("Enter Salary (₹): "))
experience = float(input("Enter Years of Experience: "))
performance_rating = float(input("Enter Performance Rating (1-5): "))

# Display Employee Details
print("\n------ Employee Details ------")
print("Employee Name:", employee_name)
print("Salary: ₹", salary)
print("Experience:", experience, "years")
print("Performance Rating:", performance_rating)

# Checking Bonus Eligibility
print("\n------ Bonus Eligibility ------")

if salary < 50000 and experience >= 2 and performance_rating >= 4:
    print("Status: Eligible for Performance Bonus")
else:
    print("Status: Not Eligible for Performance Bonus")
    print("Reason(s):")

    if salary >= 50000:
        print("- Salary is ₹50,000 or more.")

    if experience < 2:
        print("- Experience is less than 2 years.")

    if performance_rating < 4:
        print("- Performance rating is less than 4.")