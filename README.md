Caesar Cipher Project

Description

This project is a simple implementation of the Caesar Cipher, a type of substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet. The project includes functions to both encrypt and decrypt messages using a specified shift value.

How to Use
Prerequisites
->Python 3.x installed on your system.
Running the Program
1. Clone the repository or download the script file.
git clone <repository_url>
cd <repository_directory>
2.Run the script using Python.
python caesar_cipher.py
Program Menu
When you run the script, you will see a menu with the following options:

Encrypt: Encrypt a message.
Decrypt: Decrypt a message.
Exit: Exit the program.


Example Usage
1. Encrypt a Message:
Choose option 1.
Enter the shift value (e.g., 3).
Enter the message to encrypt (e.g., Hello World).
The program will output the encrypted message (e.g., Khoor Zruog).

3. Decrypt a Message:
Choose option 2.
Enter the shift value used to encrypt the message (e.g., 3).
Enter the encrypted message (e.g., Khoor Zruog).
The program will output the decrypted message (e.g., Hello World).

4. Exit the Program:
Choose option 3.

Code Overview
Encrypt Function
The encrypt function takes a shift value and a message as input, and returns the encrypted message. It shifts each letter by the specified shift value, wrapping around the alphabet if necessary.

Decrypt Function
The decrypt function takes a shift value and an encrypted message as input, and returns the original message. It shifts each letter back by the specified shift value, wrapping around the alphabet if necessary.

Main Program Loop
The main program loop presents a menu to the user, processes the user's choice, and calls the appropriate function (encrypt or decrypt) based on the choice.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
This project is inspired by the classic Caesar Cipher encryption technique.
