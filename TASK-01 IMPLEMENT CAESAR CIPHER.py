#TASK-01 IMPLEMENT CAESAR CIPHER

def caesar_encrypt(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                new_char = chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            else:
                new_char = chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
            encrypted_message += new_char
        else:
            encrypted_message += char  # Non-alphabetic characters are unchanged
    return encrypted_message

def caesar_decrypt(encrypted_message, shift):
    return caesar_encrypt(encrypted_message, -shift)  # Decrypting is just encrypting with a negative shift

def get_user_input():
    message = input("Enter your message: ")
    while True:
        try:
            shift = int(input("Enter shift value (positive or negative): "))
            break
        except ValueError:
            print("Please enter a valid integer for the shift value.")
    return message, shift

def main():
    print("Caesar Cipher Encryption and Decryption")
    while True:
        choice = input("Would you like to (e)ncrypt or (d)ecrypt? (or 'q' to quit): ").strip().lower()
        if choice == 'e':
            message, shift = get_user_input()
            encrypted = caesar_encrypt(message, shift)
            print("Encrypted message:", encrypted)
        elif choice == 'd':
            message, shift = get_user_input()
            decrypted = caesar_decrypt(message, shift)
            print("Decrypted message:", decrypted)
        elif choice == 'q':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 'e' to encrypt, 'd' to decrypt, or 'q' to quit.")

if __name__ == "__main__":
    main()
