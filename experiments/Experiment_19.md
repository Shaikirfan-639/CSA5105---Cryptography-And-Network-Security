Write a C program for encryption in the cipher block chaining (CBC) mode using an algorithm
stronger than DES. 3DES is a good candidate. Both of which follow from the definition of CBC.
Which of the two would you choose:
a. For security?
b. For performance?


# CBC Mode Encryption using 3DES
# Install first in Google Colab/Jupyter:
# !pip install pycryptodome

from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad

# 3DES requires a 16 or 24 byte key
key = DES3.adjust_key_parity(b"123456789012345678901234")

# CBC requires an 8-byte IV for 3DES
iv = get_random_bytes(8)

plaintext = b"Meet me at the usual place."

# Padding
padded_text = pad(plaintext, DES3.block_size)

# Create 3DES CBC cipher
cipher = DES3.new(key, DES3.MODE_CBC, iv)

# Encrypt
ciphertext = cipher.encrypt(padded_text)

print("Plaintext :", plaintext.decode())
print("IV        :", iv.hex())
print("Ciphertext:", ciphertext.hex())

<img width="1200" height="698" alt="image" src="https://github.com/user-attachments/assets/6271ec9c-b3fa-47ab-a75b-e26d463aea84" />




