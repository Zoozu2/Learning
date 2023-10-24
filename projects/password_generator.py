import random
import string

# Define a function to generate a random password
def generate_password(length):
    # Define the character set to use for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password by selecting characters from the character set
    password = ''.join(random.choice(characters) for i in range(length))

    print("Your password is:", password)

# Get input from the user for the desired password length
length = int(input("Enter password length: "))
generate_password(length)
