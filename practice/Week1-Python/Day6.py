# Customer Login Verification

# Correct Credentials
correct_username = "Stella"
correct_password = "al123"

# Allow 3 login attempts
for attempt in range(1, 4):
    print("\nLogin Attempt", attempt)

    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username == correct_username and password == correct_password:
        print("\nLogin Successful!")
        break
    else:
        print("Invalid Credentials!")

else:
    print("\nAccount Locked!")