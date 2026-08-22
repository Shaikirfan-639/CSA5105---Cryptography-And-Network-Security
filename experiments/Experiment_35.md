import random
import string

def encrypt(text, key):
    return ''.join(
        chr((ord(c)-65+k) % 26 + 65)
        for c, k in zip(text.upper(), key)
    )

def decrypt(cipher, key):
    return ''.join(
        chr((ord(c)-65-k) % 26 + 65)
        for c, k in zip(cipher, key)
    )

text = "HELLO"
key = [3, 19, 5, 12, 8]   # Random key: 0-25

cipher = encrypt(text, key)
plain = decrypt(cipher, key)

print("Plaintext :", text)
print("Key       :", key)
print("Ciphertext:", cipher)
print("Decrypted :", plain)

<img width="781" height="666" alt="image" src="https://github.com/user-attachments/assets/7f779f3d-2ca0-4531-88af-8e094e9dc54c" />
