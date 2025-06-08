# main.py
# pass_generate.py

import random
import string

def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True):
    chars = string.ascii_lowercase
    if use_upper:
        chars += string.ascii_uppercase + name
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    password = ''.join(random.choice(chars) for _ in range(length))
    return password


print("")
print("🔐 Welcome to the CLI Password Generator")
print("----------------------------------------")

try:
    length = int(input("Enter desired password length (e.g., 12): "))
    use_upper = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'

    password = generate_password(length, use_upper, use_digits, use_symbols)
    print(f"\n✅ Generated Password: {password}")
except ValueError:
    print("❌ Please enter a valid number for password length.")

print("\nMade by @Mr_adex 🔓")
