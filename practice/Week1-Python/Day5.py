# Online Shopping Discount Calculator

# Taking input
customer_name = input("Enter Customer Name: ")
purchase_amount = float(input("Enter Total Purchase Amount (₹): "))
premium_member = input("Are you a Premium Member? (Yes/No): ")

# Calculate Discount
discount = 0

if purchase_amount < 2000:
    discount = 0
elif purchase_amount >= 2000 and purchase_amount < 5000:
    discount = purchase_amount * 0.10
else:
    discount = purchase_amount * 0.20

# Additional discount for Premium Members
if premium_member.lower() == "yes":
    discount = discount + (purchase_amount * 0.05)

# Calculate Final Bill
final_amount = purchase_amount - discount

# Display Bill
print("\n------ Shopping Bill ------")
print("Customer Name:", customer_name)
print("Original Bill: ₹", purchase_amount)
print("Total Discount: ₹", discount)
print("Final Payable Amount: ₹", final_amount)

# Bonus
if final_amount > 10000:
    print("Eligible for Free Shipping")