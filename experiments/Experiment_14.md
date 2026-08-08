14. Write a C program for one-time pad version of the Vigenère cipher. In this scheme, the key is a
stream of random numbers between 0 and 26. For example, if the key is 3 19 5 . . . , then the first letter of
plaintext is encrypted with a shift of 3 letters, the second with a shift of 19 letters, the third with a shift of
5 letters, and so on.
a. Encrypt the plaintext send more money with the key stream
9 0 1 7 23 15 21 14 11 11 2 8 9
b. Using the ciphertext produced in part (a), find a key so that the cipher text decrypts to the plaintext
cash not needed.

import string

alphabet = string.ascii_lowercase

def encrypt(plaintext, key):
    plaintext = plaintext.replace(" ", "").lower()
    ciphertext = ""

    for i in range(len(plaintext)):
        p = alphabet.index(plaintext[i])
        c = (p + key[i]) % 26
        ciphertext += alphabet[c]

    return ciphertext


def decrypt(ciphertext, key):
    plaintext = ""

    for i in range(len(ciphertext)):
        c = alphabet.index(ciphertext[i])
        p = (c - key[i]) % 26
        plaintext += alphabet[p]

    return plaintext


# Part (a)
plaintext = "send more money"

key = [9, 0, 1, 7, 23, 15, 21, 14, 11, 11, 2, 8, 9]

ciphertext = encrypt(plaintext, key)

print("Part (a)")
print("Plaintext :", plaintext)
print("Key       :", key)
print("Ciphertext:", ciphertext)


# Part (b)
# Find a new key so the same ciphertext decrypts to "cash not needed"

desired_plaintext = "cash not needed".replace(" ", "")

new_key = []

for i in range(len(ciphertext)):
    c = alphabet.index(ciphertext[i])
    p = alphabet.index(desired_plaintext[i])
    k = (c - p) % 26
    new_key.append(k)

print("\nPart (b)")
print("Ciphertext        :", ciphertext)
print("Required plaintext:", desired_plaintext)
print("New key           :", new_key)
print("Decrypted result   :", decrypt(ciphertext, new_key))





<img width="940" height="780" alt="image" src="https://github.com/user-attachments/assets/d9afe437-bb44-40b5-aabe-737d0926cb16" />




