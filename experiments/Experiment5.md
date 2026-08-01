# Affine Caesar Cipher

from math import gcd

# Function to find modular inverse
def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

# Encryption
def encrypt(text, a, b):
    cipher = ""
    for ch in text.upper():
        if ch.isalpha():
            p = ord(ch) - ord('A')
            c = (a * p + b) % 26
            cipher += chr(c + ord('A'))
        else:
            cipher += ch
    return cipher

# Decryption
def decrypt(cipher, a, b):
    plain = ""
    a_inv = mod_inverse(a, 26)

    if a_inv is None:
        return "Decryption not possible. 'a' has no modular inverse."

    for ch in cipher.upper():
        if ch.isalpha():
            c = ord(ch) - ord('A')
            p = (a_inv * (c - b)) % 26
            plain += chr(p + ord('A'))
        else:
            plain += ch
    return plain

# Main Program
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

# Check validity of a
if gcd(a, 26) != 1:
    print("Invalid value of a. Choose a value relatively prime to 26.")
else:
    text = input("Enter Plaintext: ")
    cipher = encrypt(text, a, b)
    print("Encrypted Text:", cipher)
    print("Decrypted Text:", decrypt(cipher, a, b))






<img width="806" height="780" alt="image" src="https://github.com/user-attachments/assets/241cae19-825b-4f61-9904-f652ad17a3b1" />
