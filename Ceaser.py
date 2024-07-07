# Function to encrypt the message
def encrypt(shift, message):
    result = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char
    return result

# Function to decrypt the message
def decrypt(shift, message):
    result = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - 65 - shift) % 26 + 65)
            else:
                result += chr((ord(char) - 97 - shift) % 26 + 97)
        else:
            result += char
    return result

# Main program
while True:
    print("Caesar Cipher")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")
    option = input("Choose an option: ")

    if option == '3':
        print("Exiting...")
        break

    shift = int(input("Enter the shift value: "))
    message = input("Enter the message: ")

    if option == '1':
        result = encrypt(shift, message)
        print(f"Encrypted message: {result}")
    elif option == '2':
        result = decrypt(shift, message)
        print(f"Decrypted message: {result}")
    else:
        print("Invalid option")
