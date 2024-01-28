import getpass

# File name constant
FILE_NAME = "passwd.txt"

# Simple substitution cipher for password encryption
def encrypt_password(password):
    return ''.join(chr((ord(char) + 13) % 128) for char in password)

# Function to print the content of a file
def print_file_content(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            print(f"$ cat {file_name}")
            for line in lines:
                print(line.strip())
    except FileNotFoundError:
        print(f"File not found: {file_name}")

# Function to check if a user exists in the user list
def user_exists(username, users):
    for user in users:
        if user[0] == username:
            return True
    return False

# Function to read user information from a file and return a list of User objects
def read_passwd_file():
    try:
        with open(FILE_NAME, 'r') as file:
            lines = file.readlines()
            users = [tuple(line.strip().split(':')) for line in lines]
        return users
    except FileNotFoundError:
        return []

# Function to write user information to a file
def write_passwd_file(users):
    with open(FILE_NAME, 'w') as file:
        for user in users:
            username, real_name, *password_fields = user
            original_password = ''.join(password_fields).strip() if password_fields else ''
            file.write(f"{username}:{real_name}:{original_password}\n")
        file.flush()
        print_file_content(FILE_NAME)  # Print the updated content

# Function to add a new user to the system
def add_user():
    print("$ ./adduser.py")
    username = input("Enter new username: ").lower()
    
    # Read the file to get the current user list
    users = read_passwd_file()

    if user_exists(username, users):
        print("Cannot add. Most likely username already exists.")
        return

    real_name = input("Enter real name: ")
    password = getpass.getpass("Enter password: ")

    users.append((username, real_name, password))
    
    # Write the updated user list to the file
    write_passwd_file(users)

    print(f"User '{username}' Created.")

# Function to delete a user from the system
def delete_user():
    print("$ ./deluser.py")
    username_to_delete = input("Enter username to delete: ").lower()
    password_check = getpass.getpass("Enter your password to confirm: ")

    # Read the file to get the current user list
    users = read_passwd_file()

    found_user = False
    for user in users:
        if user[0] == username_to_delete and user[2] == password_check:
            found_user = True
            users.remove(user)
            # Write the updated user list to the file
            write_passwd_file(users)
            print(f"User '{username_to_delete}' Deleted.")
            break

    if not found_user:
        print(f"Error: User '{username_to_delete}' not found or incorrect password. No change made.")

# Function to change the password for a user
def change_password():
    print("$ ./changepasswd.py")
    username = input("Enter username: ").lower()

    # Read the file to get the current user list
    users = read_passwd_file()

    user_found = False
    for i, user in enumerate(users):
        if user[0] == username:
            user_found = True
            current_password = getpass.getpass("Enter current password: ")
            if user[2] != current_password:
                print("Error: Invalid current password. No change made.")
            else:
                new_password = getpass.getpass("Enter new password: ")
                confirm_password = getpass.getpass("Confirm new password: ")
                if new_password == confirm_password:
                    users[i] = (username, user[1], new_password)
                    
                    # Write the updated user list to the file
                    write_passwd_file(users)
                    
                    print(f"Password changed.")
                else:
                    print("Error: Passwords do not match. No change made.")
            break

    if not user_found:
        print(f"Error: User '{username}' not found. No change made.")

# Function for user login
def login():
    print("$ ./login.py")
    username = input("Enter username: ").lower()
    password = getpass.getpass("Enter password: ")

    # Read the file to get the current user list
    users = read_passwd_file()

    for user in users:
        if user[0] == username and user[2] == password:
            print(f"Access granted for user '{username}'.")
            return

    print("Access denied.")

# Main program
print(f"$ cat {FILE_NAME}")
print_file_content(FILE_NAME)
while True:
    print("\n1. Add User\n2. Delete User\n3. Change Password\n4. Login\n5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_user()
    elif choice == "2":
        delete_user()
    elif choice == "3":
        change_password()
    elif choice == "4":
        login()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
