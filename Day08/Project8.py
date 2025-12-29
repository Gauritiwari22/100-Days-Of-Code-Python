# Project8

import string
alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

encoding=input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
message=input("Type your message: \n").lower()
shift=int(input("Enter the shift number: \n"))

def encrypt(message,shifts):
    cipher_text=""
    for letter in message:
        shifted_position= alphabets.index(letter)+shift
        shifted_position=shifted_position%len(alphabets)
        cipher_text+=alphabets[shifted_position]

    print(f"Here is the encoded result:{cipher_text}")

encrypt(message,shift)

decrption=input("Type 'yes' if you want to decrypt the message.\n")
message=input("Type your message: \n").lower()
shift=int(input("Enter the shift number: \n"))


def decrypt(message,shift):
    output_text=""
    for letter in message:
        shifted_position= alphabets.index(letter)-shift
        shifted_position=shifted_position%len(alphabets)
        output_text+=alphabets[shifted_position]

    print(f"Here is the decoded result:{output_text}")

decrypt(message,shift)








