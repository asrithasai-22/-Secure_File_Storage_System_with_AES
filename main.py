from file_manager import encrypt_and_store, decrypt_and_verify
from crypto_utils import generate_key
import os

def main():
    if not os.path.exists("aes.key"):
        print("[*] AES key not found. Generating...")
        generate_key()

    while True:
        print("\nSecure File Storage System")
        print("1. Encrypt File")
        print("2. Decrypt File")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            path = input("Enter path to the file: ")
            encrypt_and_store(path)

        elif choice == "2":
            fname = input("Enter filename to decrypt: ")
            decrypt_and_verify(fname)

        elif choice == "3":
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
