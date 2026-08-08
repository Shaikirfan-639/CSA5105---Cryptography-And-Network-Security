Write a C program for ECB mode, if there is an error in a block of the transmitted ciphertext, only
the corresponding plaintext block is affected. However, in the CBC mode, this error propagates. For
example, an error in the transmitted C1 obviously corrupts P1 and P2.
a. Are any blocks beyond P2 affected?
b. Suppose that there is a bit error in the source version of P1. Through how many
ciphertext blocks is this error propagated? What is the effect at the receiver?


!pip install pycryptodome -q

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

# AES key and IV
key = b"1234567890123456"
iv = b"abcdefghijklmnop"

# Plaintext
plaintext = b"Block-1-Message!Block-2-Message!Block-3-Message!"
plaintext = pad(plaintext, AES.block_size)

# ==================== ECB ====================

ecb = AES.new(key, AES.MODE_ECB)
ecb_ciphertext = ecb.encrypt(plaintext)

# Introduce 1-bit error in first ciphertext block
ecb_error = bytearray(ecb_ciphertext)
ecb_error[0] ^= 1

ecb_dec = AES.new(key, AES.MODE_ECB)
ecb_plaintext = ecb_dec.decrypt(bytes(ecb_error))

print("========== ECB MODE ==========")
print("Original Ciphertext :", ecb_ciphertext.hex())
print("Modified Ciphertext:", bytes(ecb_error).hex())
print("Decrypted Plaintext :", ecb_plaintext)

print("\nECB Result:")
print("P1 is affected.")
print("P2, P3, ... are NOT affected.")


# ==================== CBC ====================

cbc = AES.new(key, AES.MODE_CBC, iv)
cbc_ciphertext = cbc.encrypt(plaintext)

# Introduce 1-bit error in C1
cbc_error = bytearray(cbc_ciphertext)
cbc_error[0] ^= 1

cbc_dec = AES.new(key, AES.MODE_CBC, iv)
cbc_plaintext = cbc_dec.decrypt(bytes(cbc_error))

print("\n========== CBC MODE ==========")
print("Original Ciphertext :", cbc_ciphertext.hex())
print("Modified Ciphertext:", bytes(cbc_error).hex())
print("Decrypted Plaintext :", cbc_plaintext)

print("\nCBC Result:")
print("P1 is completely corrupted.")
print("P2 has one bit flipped.")
print("P3, P4, ... are NOT affected.")


# ==================== ANSWERS ====================

print("\n========== ANSWERS ==========")

print("\na. Are blocks beyond P2 affected?")
print("Answer: NO.")
print("Only P1 and P2 are affected by an error in transmitted C1.")

print("\nb. If one bit error occurs in source P1:")
print("The error propagates through C1, C2, C3, ...")
print("Thus, all subsequent ciphertext blocks are affected.")
print("At the receiver, P1 and subsequent plaintext blocks are affected.")


<img width="1917" height="758" alt="image" src="https://github.com/user-attachments/assets/4c9d6263-7043-41ea-bdc9-e3acb9e5dd18" />



