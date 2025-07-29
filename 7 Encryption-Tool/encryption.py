def display_menu():
    print("\n" + "=" * 40)
    print("       ENCRYPTION TOOL")
    print("=" * 40)
    print(" 1. Encrypt text (Caesar Cipher)")
    print(" 2. Decrypt text")
    print(" 3. AES Encryption (Advanced)")
    print(" 4. AES Decryption (Advanced)")
    print(" 5. Exit")
    print("=" * 40)


def get_shift():
    while True:
        try:
            shift = int(input("Enter shift value (integer): "))
            return shift
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def get_message():
    message = input("Enter your message: ")
    if not message:
        print("Error: Message cannot be empty.")
        return None
    return message


def caesar_encrypt(text, shift):
    result = ""
    shift = shift % 26

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26
            result += chr(base + shifted)
        else:
            result += char

    return result


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


def aes_encrypt(message):
    try:
        from cryptography.fernet import Fernet
    except ImportError:
        print("cryptography library not installed.")
        print("Install it with: pip install cryptography")
        return None, None

    key = Fernet.generate_key()
    cipher = Fernet(key)
    encrypted = cipher.encrypt(message.encode())
    return encrypted.decode(), key.decode()


def aes_decrypt(encrypted_message, key):
    try:
        from cryptography.fernet import Fernet
    except ImportError:
        print("cryptography library not installed.")
        return None

    try:
        cipher = Fernet(key.encode())
        decrypted = cipher.decrypt(encrypted_message.encode())
        return decrypted.decode()
    except Exception as e:
        print(f"Decryption failed: {str(e)}")
        return None


def main():
    print("\n--- Encryption Tool (CLI) ---")

    while True:
        display_menu()
        choice = input("Select option (1-5): ").strip()

        if choice == "1":
            message = get_message()
            if message:
                shift = get_shift()
                encrypted = caesar_encrypt(message, shift)
                print(f"\nEncrypted: {encrypted}")

        elif choice == "2":
            message = get_message()
            if message:
                shift = get_shift()
                decrypted = caesar_decrypt(message, shift)
                print(f"\nDecrypted: {decrypted}")

        elif choice == "3":
            message = get_message()
            if message:
                encrypted, key = aes_encrypt(message)
                if encrypted:
                    print(f"\nEncrypted: {encrypted}")
                    print(f"Key (save this to decrypt): {key}")

        elif choice == "4":
            encrypted = input("Enter encrypted message: ").strip()
            key = input("Enter decryption key: ").strip()
            if encrypted and key:
                decrypted = aes_decrypt(encrypted, key)
                if decrypted:
                    print(f"\nDecrypted: {decrypted}")

        elif choice == "5":
            print("\nGoodbye!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()