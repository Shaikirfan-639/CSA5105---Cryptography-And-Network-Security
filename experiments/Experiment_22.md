# ============================================================
# S-DES Encryption and Decryption in CBC Mode
# Google Colab Program
# ============================================================

# -----------------------------
# S-DES Permutation Tables
# -----------------------------

P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
P8  = [6, 3, 7, 4, 8, 5, 10, 9]

IP     = [2, 6, 3, 1, 4, 8, 5, 7]
IP_INV = [4, 1, 3, 5, 7, 2, 8, 6]

EP = [4, 1, 2, 3, 2, 3, 4, 1]
P4 = [2, 4, 3, 1]

S0 = [
    [1, 0, 3, 2],
    [3, 2, 1, 0],
    [0, 2, 1, 3],
    [3, 1, 3, 2]
]

S1 = [
    [0, 1, 2, 3],
    [2, 0, 1, 3],
    [3, 0, 1, 0],
    [2, 1, 0, 3]
]


# -----------------------------
# Permutation Function
# -----------------------------

def permutation(bits, table):
    return ''.join(bits[i - 1] for i in table)


# -----------------------------
# Left Circular Shift
# -----------------------------

def left_shift(bits, n):
    return bits[n:] + bits[:n]


# -----------------------------
# Generate S-DES Keys
# -----------------------------

def generate_keys(key):

    # Apply P10
    key_p10 = permutation(key, P10)

    left = key_p10[:5]
    right = key_p10[5:]

    # LS-1
    left = left_shift(left, 1)
    right = left_shift(right, 1)

    # Generate K1
    K1 = permutation(left + right, P8)

    # LS-2
    left = left_shift(left, 2)
    right = left_shift(right, 2)

    # Generate K2
    K2 = permutation(left + right, P8)

    return K1, K2


# -----------------------------
# S-Box Function
# -----------------------------

def sbox(bits, sbox_table):

    # Row = first and fourth bits
    row = int(bits[0] + bits[3], 2)

    # Column = middle two bits
    column = int(bits[1] + bits[2], 2)

    value = sbox_table[row][column]

    return format(value, '02b')


# -----------------------------
# XOR Function
# -----------------------------

def xor_bits(a, b):
    return ''.join(
        str(int(x) ^ int(y))
        for x, y in zip(a, b)
    )


# -----------------------------
# fk Function
# -----------------------------

def fk(bits, key):

    left = bits[:4]
    right = bits[4:]

    # Expansion and permutation
    expanded = permutation(right, EP)

    # XOR with key
    xor_result = xor_bits(expanded, key)

    # Split into two 4-bit parts
    left_part = xor_result[:4]
    right_part = xor_result[4:]

    # S-Box substitution
    s0_output = sbox(left_part, S0)
    s1_output = sbox(right_part, S1)

    # P4 permutation
    p4_output = permutation(
        s0_output + s1_output,
        P4
    )

    # XOR with left half
    new_left = xor_bits(left, p4_output)

    return new_left + right


# -----------------------------
# S-DES Encryption
# -----------------------------

def sdes_encrypt(plaintext, key):

    K1, K2 = generate_keys(key)

    # Initial Permutation
    bits = permutation(plaintext, IP)

    # Round 1
    bits = fk(bits, K1)

    # Swap halves
    bits = bits[4:] + bits[:4]

    # Round 2
    bits = fk(bits, K2)

    # Inverse Initial Permutation
    ciphertext = permutation(bits, IP_INV)

    return ciphertext


# -----------------------------
# S-DES Decryption
# -----------------------------

def sdes_decrypt(ciphertext, key):

    K1, K2 = generate_keys(key)

    # Initial Permutation
    bits = permutation(ciphertext, IP)

    # Round 1 using K2
    bits = fk(bits, K2)

    # Swap halves
    bits = bits[4:] + bits[:4]

    # Round 2 using K1
    bits = fk(bits, K1)

    # Inverse Initial Permutation
    plaintext = permutation(bits, IP_INV)

    return plaintext


# ============================================================
# CBC MODE
# ============================================================

def cbc_encrypt(plaintext, key, iv):

    # S-DES block size = 8 bits
    if len(plaintext) % 8 != 0:
        raise ValueError("Plaintext length must be a multiple of 8 bits.")

    ciphertext = ""
    previous_block = iv

    # Process every 8-bit block
    for i in range(0, len(plaintext), 8):

        block = plaintext[i:i+8]

        # CBC: XOR plaintext with previous ciphertext
        xor_block = xor_bits(block, previous_block)

        # Encrypt using S-DES
        encrypted_block = sdes_encrypt(xor_block, key)

        ciphertext += encrypted_block

        # Update previous block
        previous_block = encrypted_block

    return ciphertext


def cbc_decrypt(ciphertext, key, iv):

    if len(ciphertext) % 8 != 0:
        raise ValueError("Ciphertext length must be a multiple of 8 bits.")

    plaintext = ""
    previous_block = iv

    # Process every 8-bit block
    for i in range(0, len(ciphertext), 8):

        block = ciphertext[i:i+8]

        # Decrypt S-DES
        decrypted_block = sdes_decrypt(block, key)

        # CBC: XOR decrypted block with previous ciphertext
        plaintext_block = xor_bits(
            decrypted_block,
            previous_block
        )

        plaintext += plaintext_block

        # Update previous block
        previous_block = block

    return plaintext


# ============================================================
# TEST DATA GIVEN IN QUESTION
# ============================================================

key = "0111111101"
iv = "10101010"

plaintext = "0000000100100011"

print("==============================================")
print("       S-DES CBC ENCRYPTION / DECRYPTION")
print("==============================================")

print("\nKey       :", key)
print("IV        :", iv)
print("Plaintext :", plaintext)


# Generate subkeys
K1, K2 = generate_keys(key)

print("\nGenerated S-DES Keys:")
print("K1        :", K1)
print("K2        :", K2)


# -----------------------------
# Encryption
# -----------------------------

ciphertext = cbc_encrypt(
    plaintext,
    key,
    iv
)

print("\n----------- ENCRYPTION -----------")

print("Plaintext :", plaintext)

print("Ciphertext:", ciphertext)


# -----------------------------
# Decryption
# -----------------------------

decrypted_text = cbc_decrypt(
    ciphertext,
    key,
    iv
)

print("\n----------- DECRYPTION -----------")

print("Ciphertext:", ciphertext)

print("Decrypted :", decrypted_text)


# -----------------------------
# Verification
# -----------------------------

expected_ciphertext = "1111010000001011"

print("\n----------- VERIFICATION -----------")

print("Expected Ciphertext :", expected_ciphertext)
print("Generated Ciphertext:", ciphertext)

if ciphertext == expected_ciphertext:
    print("Encryption Test: PASSED")
else:
    print("Encryption Test: FAILED")

if decrypted_text == plaintext:
    print("Decryption Test: PASSED")
else:
    print("Decryption Test: FAILED")

print("\n==============================================")



<img width="896" height="827" alt="image" src="https://github.com/user-attachments/assets/52e29eed-8baa-4cbd-9375-878ffa0e0ce9" />
