import random
import string

print("=== Random Password Generator ===")

# Password length
length = int(input("Enter password length: "))

# User choices
use_upper = input("Include Uppercase letters? (y/n): ").lower() == "y"
use_lower = input("Include Lowercase letters? (y/n): ").lower() == "y"
use_numbers = input("Include Numbers? (y/n): ").lower() == "y"
use_symbols = input("Include Special Characters? (y/n): ").lower() == "y"

characters = ""

if use_upper:
    characters += string.ascii_uppercase

if use_lower:
    characters += string.ascii_lowercase

if use_numbers:
    characters += string.digits

if use_symbols:
    characters += string.punctuation

if not characters:
    print("Error: Select at least one character type.")
else:
    password = ""

    for _ in range(length):
        password += random.choice(characters)

    print("\nGenerated Password:")
    print(password)
