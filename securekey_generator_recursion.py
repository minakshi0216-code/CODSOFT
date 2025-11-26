import random
import string

# Function to generate password using recursion
# created by Minakshi
def generate_password(length, level):
    if length == 0:
        return ""
    
    if level == "weak":
        chars = string.ascii_lowercase
    elif level == "medium":
        chars = string.ascii_letters + string.digits
    else:
        chars = string.ascii_letters + string.digits + string.punctuation
    
    # Pick one random character + call the function again
    return random.choice(chars) + generate_password(length - 1, level)


# Recursive function to continue if user wants again
def ask_user():
    print("\n--- Smart Password Generator ---")
    try:
        length = int(input("Enter password length: "))
        if length <= 0:
            print("Length should be positive")
            return ask_user()
    except ValueError:
        print("Please enter a valid number")
        return ask_user()
    
    level = input("Choose strength (weak / medium / strong): ").lower()
    if level not in ["weak", "medium", "strong"]:
        print("Invalid  Try again.")
        return ask_user()

    password = generate_password(length, level)
    print(f"\nYour {level} password is: {password}")

    again = input("\nGenerate another password? (yes/no): ").lower()
    if again == "yes":
        ask_user()
    else:
        print("\nThanks for using Smart Password Generator ")


# Start program
ask_user()