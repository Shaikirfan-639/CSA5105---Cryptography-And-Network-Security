12. a. Write a C program to Encrypt the message “meet me at the usual place at ten rather than eight
oclock” using the Hill cipher with the key.
[9 4]
[5 7]
a. Show your calculations and the result.
b. Show the calculations for the corresponding decryption of the ciphertext to recover the original
plaintext.


import numpy as np

# Hill Cipher Key
K = np.array([[9, 4],
              [5, 7]])

# Inverse key modulo 26
K_inv = np.array([[5, 12],
                  [15, 25]])

# Plaintext
plaintext = "meet me at the usual place at ten rather than eight oclock"

# Remove spaces
plaintext = plaintext.replace(" ", "").lower()

# Add X if length is odd
if len(plaintext) % 2 != 0:
    plaintext += "x"

# ---------------- ENCRYPTION ----------------
ciphertext = ""

print("ENCRYPTION")
print("-" * 40)

for i in range(0, len(plaintext), 2):
    pair = plaintext[i:i+2]

    vector = np.array([
        ord(pair[0]) - ord('a'),
        ord(pair[1]) - ord('a')
    ])

    result = K.dot(vector) % 26

    cipher_pair = chr(result[0] + ord('a')) + chr(result[1] + ord('a'))
    ciphertext += cipher_pair

    print(pair, "->", cipher_pair)

print("\nCiphertext:", ciphertext)

# ---------------- DECRYPTION ----------------
decrypted = ""

print("\nDECRYPTION")
print("-" * 40)

for i in range(0, len(ciphertext), 2):
    pair = ciphertext[i:i+2]

    vector = np.array([
        ord(pair[0]) - ord('a'),
        ord(pair[1]) - ord('a')
    ])

    result = K_inv.dot(vector) % 26

    plain_pair = chr(result[0] + ord('a')) + chr(result[1] + ord('a'))
    decrypted += plain_pair

    print(pair, "->", plain_pair)

# Remove padding X if present
if decrypted.endswith("x"):
    decrypted = decrypted[:-1]

print("\nDecrypted plaintext:", decrypted)




<img width="1011" height="746" alt="image" src="https://github.com/user-attachments/assets/701b19a3-f181-4807-971a-9d1721ba92b8" />
<img width="945" height="770" alt="image" src="https://github.com/user-attachments/assets/2912044e-e795-4027-981a-cb9196e0c6bd" />




