# Login with while loop

users = {
    "admin": "1234",
    "shabbir": "password"
}

while True:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users and users[username] == password:
        print("Login successful! 🎉")
        break               # stop the loop after success
    else:
        print("Invalid username or password. Try again!\n")