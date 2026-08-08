Write a C program for ECB, CBC, and CFB modes, the plaintext must be a sequence of one or more
complete data blocks (or, for CFB mode, data segments). In other words, for these three modes, the total
number of bits in the plaintext must be a positive multiple of the block (or segment) size. One common
method of padding, if needed, consists of a 1 bit followed by as few zero bits, possibly none, as are
necessary to complete the final block. It is considered good practice for the sender to pad every message,
including messages in which the final message block is already complete. What is the motivation for
including a padding block when padding is not needed?



!pip install pycryptodome -q

from Crypto.Cipher import AES

# AES uses a 128-bit (16-byte) block
key = b"1234567890123456"
iv = b"abcdefghijklmnop"

BLOCK_SIZE = 16


# ---------------------------------------------------------
# Padding: 1 bit followed by 0 bits
# In bytes: 0x80 followed by zero bytes
# Always add padding, even if already a complete block
# ---------------------------------------------------------
def add_padding(data):
    padding_length = BLOCK_SIZE - (len(data) % BLOCK_SIZE)

    if padding_length == 0:
        padding_length = BLOCK_SIZE

    padding = bytes([0x80]) + bytes(padding_length - 1)

    return data + padding


# Remove padding
def remove_padding(data):
    index = data.rfind(b'\x80')

    if index != -1 and all(x == 0 for x in data[index + 1:]):
        return data[:index]

    return data


# ---------------------------------------------------------
# Plaintext
# ---------------------------------------------------------
plaintext = b"THIS IS A SECRET MESSAGE"

print("Original Plaintext:")
print(plaintext.decode())

# Add padding
padded = add_padding(plaintext)

print("\nPadded Plaintext:")
print(padded)
print("Padded length:", len(padded), "bytes")


# =========================================================
# ECB MODE
# =========================================================
ecb_encrypt = AES.new(key, AES.MODE_ECB)
ecb_ciphertext = ecb_encrypt.encrypt(padded)

ecb_decrypt = AES.new(key, AES.MODE_ECB)
ecb_plaintext = ecb_decrypt.decrypt(ecb_ciphertext)

ecb_plaintext = remove_padding(ecb_plaintext)

print("\n========== ECB MODE ==========")
print("Ciphertext:", ecb_ciphertext.hex())
print("Decrypted :", ecb_plaintext.decode())


# =========================================================
# CBC MODE
# =========================================================
cbc_encrypt = AES.new(key, AES.MODE_CBC, iv)
cbc_ciphertext = cbc_encrypt.encrypt(padded)

cbc_decrypt = AES.new(key, AES.MODE_CBC, iv)
cbc_plaintext = cbc_decrypt.decrypt(cbc_ciphertext)

cbc_plaintext = remove_padding(cbc_plaintext)

print("\n========== CBC MODE ==========")
print("IV        :", iv.hex())
print("Ciphertext:", cbc_ciphertext.hex())
print("Decrypted :", cbc_plaintext.decode())


# =========================================================
# CFB MODE
# =========================================================
# CFB with full 128-bit segment size
cfb_encrypt = AES.new(key, AES.MODE_CFB, iv=iv, segment_size=128)
cfb_ciphertext = cfb_encrypt.encrypt(padded)

cfb_decrypt = AES.new(key, AES.MODE_CFB, iv=iv, segment_size=128)
cfb_plaintext = cfb_decrypt.decrypt(cfb_ciphertext)

cfb_plaintext = remove_padding(cfb_plaintext)

print("\n========== CFB MODE ==========")
print("IV        :", iv.hex())
print("Ciphertext:", cfb_ciphertext.hex())
print("Decrypted :", cfb_plaintext.decode())


# =========================================================
# ANSWER
# =========================================================
print("\n========== ANSWER ==========")
print("Padding block is added even when plaintext is already")
print("a complete block to make padding unambiguous.")

print("\nMotivation:")
print("Without mandatory padding, the receiver cannot determine")
print("whether the final byte(s) are actual plaintext or padding.")
print("Adding a complete padding block makes the end of the")
print("plaintext unambiguous and provides consistent message formatting.")


<img width="1082" height="783" alt="image" src="https://github.com/user-attachments/assets/b260c9b4-3622-42ac-87b0-3df580e401b2" />





