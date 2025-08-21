import random
import string

def generate_password(length=12, use_specials=True):
    chars = string.ascii_letters + string.digits
    if use_specials:
        chars += string.punctuation

    return ''.join(random.choice(chars) for _ in range(length))

if __name__ == "__main__":
    length = int(input("Enter password length: "))
    use_specials = input("Include special characters? (y/n): ").lower() == "y"
    password = generate_password(length, use_specials)
    print(f"Generated Password: {password}")
