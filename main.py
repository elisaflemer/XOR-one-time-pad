# Implementation of XOR one-time pad. This algorithm takes in an ASCII string, transforms it into
# a binary sequence, generates a random bit key of the same length and computes the XOR operation over
# both sequences to find the ciphertext.
# To decrypt, a XOR operation is executed over the ciphertext and the key. The result is then converted
# back into ASCII.

import random

def generate_key(length):
    '''Generates a random bit-string key according to the length of the plaintext'''

    rng = random.SystemRandom() # gets randomness from the OS
    key = ''
    for i in range(length):
        key += str(rng.randint(0, 1))
    return key

def string_to_binary(string):
    '''Takes in a string and converts it into a binary string'''
    byte_array = [] # array to store bytes in binary notation

    for character in string:
        ascii_decimal = ord(character) # gets ascii code for the current character
        raw_binary_code = str(bin(ascii_decimal))[2:] # turns code into binary and removes leading "b'"

        # turn bits into a byte by adding leading 0s if needed to complete 8-bit chunks
        if len(raw_binary_code) < 8:
            byte = "0" * (8 - len(raw_binary_code)) + raw_binary_code
            byte_array.append(byte) # appends byte to the array

    # joins the byte_array into a string
    binary_string = ''.join(byte_array)
    return binary_string

def encrypt(plaintext):
    '''Encrypts the plaintext according to a generated key and the subsequent XOR operation'''

    print("\nYour plaintext is: " + plaintext)
    # gets plaintext in binary and generates key of the same length
    binary_string = string_to_binary(plaintext)
    print("Plaintext converted to binary: " + binary_string)
    key = generate_key(len(binary_string))
    print("Random key: " + key)

    encrypted = '' # initialize empty string for encrypted binary
    for i in range(len(binary_string)):
        encrypted += str(int(binary_string[i]) ^ int(key[i])) # executes XOR over each bit of the key and plaintext binary

    print("\nAfter XOR, the ciphertext is: " + encrypted)
    return encrypted, key

def binary_to_ascii(plaintext_in_binary):
    '''Converts a binary string to an ASCII string'''
    #breaks string into chunks of bytes
    chunks = [plaintext_in_binary[i:i + 8] for i in range(0, len(plaintext_in_binary), 8)]

    plaintext_in_ascii = '' # initializes empty string to store the plaintext in ascii

    # takes each chunk (byte), converts it to a decimal and decodes it corresponding character in ascii
    for chunk in chunks:
        byte = int(chunk, 2)
        plaintext_in_ascii += chr(byte)

    return plaintext_in_ascii

def decrypt(ciphertext, key):
    '''Applies XOR to ciphertext over key and converts the result back into ASCII'''
    decrypted = ''
    for i in range(len(ciphertext)):
        decrypted += str(int(ciphertext[i]) ^ int(key[i]))
    print("Decrypted binary: " + decrypted)
    return binary_to_ascii(decrypted)

if __name__ == '__main__':
    plaintext = input("Enter the plaintext as an ASCII string: ")
    cipher, key = encrypt(plaintext)
    print("\nNow, onto decryption!")
    print("Decrypted string in ASCII: " + decrypt(cipher, key))