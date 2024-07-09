# Caesar Cipher Project

# Description

This project is a simple implementation of the Caesar Cipher, a type of substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet. The project includes functions to both encrypt and decrypt messages using a specified shift value.

# How to Use  Prerequisites

->Python 3.x installed on your system.

# Running the Program

1. Clone the repository or download the script file.
git clone <repository_url>
cd <repository_directory>

2. Run the script using Python.
python caesar_cipher.py
Program Menu
When you run the script, you will see a menu with the following options:

1) Encrypt: Encrypt a message.

2) Decrypt: Decrypt a message.

3) Exit: Exit the program.
   
   ![image](https://github.com/umarfarooq003/PRODIGY-CS-1/assets/174965538/c8e400e8-10ac-4451-a79a-ecbd1e5be1a4)

# Example Usage
1. Encrypt a Message:
   
   Choose option 1.
   Enter the shift value (e.g., 4).
   Enter the message to encrypt (e.g., Hello World).
   The program will output the encrypted message (e.g., Lipps Asvph ).

![image](https://github.com/umarfarooq003/PRODIGY-CS-1/assets/174965538/7358a36a-44f2-4fa8-8c1c-13f969ecbf0e)

2. Decrypt a Message:
   
   Choose option 2.
   Enter the shift value used to encrypt the message (e.g., 4).
   Enter the encrypted message (e.g., Lipps Asvph).
   The program will output the decrypted message (e.g., Hello World).

![image](https://github.com/umarfarooq003/PRODIGY-CS-1/assets/174965538/3bf102ed-2151-428c-bbfa-1fafcbf80889)

3. Exit the Program:
   
   Choose option 3.

![image](https://github.com/umarfarooq003/PRODIGY-CS-1/assets/174965538/aaa67c44-7365-4e45-8a79-3917b3c873c9)

# Code Overview

1) Encrypt Function
The encrypt function takes a shift value and a message as input, and returns the encrypted message. It shifts each letter by the specified shift value, wrapping around the alphabet if necessary.

2) Decrypt Function
The decrypt function takes a shift value and an encrypted message as input, and returns the original message. It shifts each letter back by the specified shift value, wrapping around the alphabet if necessary.

3) Main Program Loop
The main program loop presents a menu to the user, processes the user's choice, and calls the appropriate function (encrypt or decrypt) based on the choice.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
This project is inspired by the classic Caesar Cipher encryption technique.
