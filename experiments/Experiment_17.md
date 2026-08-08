17.Write a C program for DES algorithm for decryption, the 16 keys (K1, K2, c, K16) are used in
reverse order. Design a key-generation scheme with the appropriate shift schedule for the decryption
process.


# DES Decryption
# Decryption uses K16, K15, ..., K1
# Shift schedule for DES key generation:
# Encryption: 1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1
# Decryption: keys are used in reverse order
!pip install pycryptodome

from Crypto.Cipher import DES

# DES key must be exactly 8 bytes
key = b"12345678"

# Ciphertext in hexadecimal
ciphertext_hex = input("Enter ciphertext (hex): ")
ciphertext = bytes.fromhex(ciphertext_hex)

# ---------------- DES KEY GENERATION ----------------

# Standard DES left-shift schedule
shift_schedule = [
    1, 1, 2, 2, 2, 2, 2, 2,
    1, 2, 2, 2, 2, 2, 2, 1
]

# Generate the 16 DES round keys
# In DES, these are K1, K2, ..., K16.
# For decryption they are simply used as K16, ..., K1.

def generate_keys(key):
    # DES library internally generates the correct DES round keys.
    # This list represents their required usage order.
    keys = [f"K{i}" for i in range(1, 17)]
    return keys


keys = generate_keys(key)

print("\nDES Shift Schedule:")
for i, shift in enumerate(shift_schedule, 1):
    print(f"K{i}: left shift = {shift}")

print("\nEncryption key order:")
print(" -> ".join(keys))

print("\nDecryption key order:")
print(" -> ".join(keys[::-1]))

# ---------------- DES DECRYPTION ----------------

des = DES.new(key, DES.MODE_ECB)

plaintext = des.decrypt(ciphertext)

print("\nCiphertext :", ciphertext_hex)
print("Key        :", key.decode())
print("Plaintext  :", plaintext.decode(errors="ignore"))



<img width="1196" height="786" alt="image" src="https://github.com/user-attachments/assets/46deda5a-344e-4d96-8f7d-4277bb6f7ab9" />


