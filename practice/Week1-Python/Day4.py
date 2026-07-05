# ATM Withdrawal Simulator


account_holder = input("Enter Account Holder Name: ")
balance = float(input("Enter Account Balance (₹): "))

print("\nWelcome,", account_holder)

# Allow up to 3 withdrawal attempts
for attempt in range(1, 4):
    print("\nAttempt", attempt)

    withdrawal = float(input("Enter Withdrawal Amount (₹): "))

    if withdrawal <= 0:
        print("Error: Withdrawal amount must be positive.")

    elif withdrawal > balance:
        print("Error: Insufficient balance.")

    else:
        balance = balance - withdrawal
        print("\nWithdrawal Successful!")
        print("Amount Withdrawn: ₹", withdrawal)
        print("Remaining Balance: ₹", balance)
        break

else:
    print("\nTransaction Failed!")
    print("You have used all 3 withdrawal attempts.")