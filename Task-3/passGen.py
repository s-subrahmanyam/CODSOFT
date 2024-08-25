import random
import string

def generate_password(length):
    # Define possible characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a password by randomly selecting characters
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Ask the user for the desired password length
password_length = int(input("Enter the desired password length: "))

# Generate and display the password
generated_password = generate_password(password_length)
print(f"Your generated password is: {generated_password}")
