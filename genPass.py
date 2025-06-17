import random
import string

def generate_password(length, options):
    chars = ''
    required_chars = []
    if 'C' in options:
        chars += string.digits
    if 'L' in options:
        chars += string.ascii_letters
        required_chars.append(random.choice(string.ascii_lowercase))
        required_chars.append(random.choice(string.ascii_uppercase))
    if 'S' in options:
        chars += string.punctuation

    if not chars:
        print("Input invalid. Please enter one or more of the values C, L ou S.")
        return None

    if length < len(required_chars):
        print(f"Error, password length must be {len(required_chars)} to satisfy mathematics.")
        return None

    remaining_length = length - len(required_chars)
    password = required_chars + [random.choice(chars) for _ in range(remaining_length)]
    random.shuffle(password)
    return ''.join(password)

def main():
    try:
        length = int(input("Enter password length : "))
        if length <= 0:
            print("The number must be above 0, stop trolling stupid kid.")
            return

        options = input("Enter options (C for numbers, L for letters, S for symbols) : ").upper()

        password = generate_password(length, options)
        if password:
            print(f"Your generated password is : {password}")
    except ValueError:
        print("Please enter a valid number to generate your password.")

if __name__ == "__main__":
    main()