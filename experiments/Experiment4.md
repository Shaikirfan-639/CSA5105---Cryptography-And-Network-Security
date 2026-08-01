# Polyalphabetic Substitution Cipher (Vigenère Cipher)

def encrypt(plaintext, key):
    ciphertext = ""
    key = key.upper()
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')

            if char.isupper():
                encrypted = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encrypted = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))

            ciphertext += encrypted
            key_index += 1
        else:
            ciphertext += char

    return ciphertext


def decrypt(ciphertext, key):
    plaintext = ""
    key = key.upper()
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')

            if char.isupper():
                decrypted = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                decrypted = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))

            plaintext += decrypted
            key_index += 1
        else:
            plaintext += char

    return plaintext


# Main Program
plaintext = input("Enter Plaintext: ")
key = input("Enter Key: ")

ciphertext = encrypt(plaintext, key)
print("Encrypted Text:", ciphertext)

decrypted = decrypt(ciphertext, key)
print("Decrypted Text:", decrypted)








<img width="896" height="773" alt="image" src="https://github.com/user-attachments/assets/850197c9-8164-4223-9c06-39c57b949a7f" />
