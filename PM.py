import random
import string
import json
import os

# File to store passwords
PASSWORD_DB = 'passwords.json'

# Load existing passwords from file
def load_passwords():
    if os.path.exists(PASSWORD_DB):
        with open(PASSWORD_DB, 'r') as f:
            return json.load(f)
    return {}

# Save passwords to file
def save_passwords(passwords):
    with open(PASSWORD_DB, 'w') as f:
        json.dump(passwords, f, indent=4)

# Generate a random password
def generate_password(length, num_count, symbol_count):
    if length < num_count + symbol_count:
        raise ValueError("Length is too short for the requested numbers and symbols.")
    
    letters_count = length - num_count - symbol_count
    letters = ''.join(random.choices(string.ascii_letters, k=letters_count))
    numbers = ''.join(random.choices(string.digits, k=num_count))
    symbols = ''.join(random.choices(string.punctuation, k=symbol_count))
    
    password = letters + numbers + symbols
    password = ''.join(random.sample(password, len(password)))  # Shuffle the password
    return password

# Add a new username and password
def add_password(user, password):
    passwords = load_passwords()
    passwords[user] = password
    save_passwords(passwords)
    print(f"Password for '{user}' added successfully.")

# View all saved usernames and passwords
def view_passwords():
    passwords = load_passwords()
    if not passwords:
        print("No passwords saved.")
        return
    for user, password in passwords.items():
        print(f"Username: {user}, Password: {password}")

def main():
    while True:
        print("\nPassword Manager")
        print("1. Generate Password")
        print("2. Add Password")
        print("3. View Passwords")
        print("4. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            length = int(input("Enter total length of the password: "))
            num_count = int(input("Enter number of digits: "))
            symbol_count = int(input("Enter number of symbols: "))
            try:
                password = generate_password(length, num_count, symbol_count)
                print(f"Generated Password: {password}")
            except ValueError as e:
                print(e)

        elif choice == '2':
            user = input("Enter username: ")
            password = input("Enter password (leave blank to generate one): ")
            if not password:
                length = int(input("Enter total length of the password: "))
                num_count = int(input("Enter number of digits: "))
                symbol_count = int(input("Enter number of symbols: "))
                try:
                    password = generate_password(length, num_count, symbol_count)
                    print(f"Generated Password: {password}")
                except ValueError as e:
                    print(e)
                    continue
            add_password(user, password)

        elif choice == '3':
            view_passwords()

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
