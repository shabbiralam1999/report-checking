# Simple login program with 3 attempts

correct_username = "admin"
correct_password = "12345"

attempts = 0

while attempts < 3:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Login successful! 🎉")
        break
    else:
        attempts += 1
        print("Incorrect username or password. Try again.")

if attempts == 3:
    print("Too many failed attempts. Access blocked.")
