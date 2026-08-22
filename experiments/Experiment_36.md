from math import gcd

def encrypt(text, a, b):
    return ''.join(chr((a*(ord(c)-65)+b)%26+65) for c in text.upper())

def decrypt(text, a, b):
    a_inv = pow(a, -1, 26)
    return ''.join(chr((a_inv*(ord(c)-65-b))%26+65) for c in text)

text = "HELLO"
a, b = 5, 8

if gcd(a, 26) != 1:
    print("Invalid a: encryption is not one-to-one")
else:
    cipher = encrypt(text, a, b)
    print("Plaintext :", text)
    print("Ciphertext:", cipher)
    print("Decrypted :", decrypt(cipher, a, b))

    <img width="1027" height="751" alt="image" src="https://github.com/user-attachments/assets/5de788e5-8130-4554-ad60-2e7edba57996" />
