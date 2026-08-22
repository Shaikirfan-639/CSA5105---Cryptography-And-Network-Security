# ============================================================
# S-DES ENCRYPTION AND DECRYPTION IN COUNTER (CTR) MODE
# ============================================================

# -----------------------------
# S-DES Permutation Tables
# -----------------------------

P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
P8  = [6, 3, 7, 4, 8, 5, 10, 9]

IP = [2, 6, 3, 1, 4, 8, 5, 7]
IP_INV = [4, 1, 3, 5, 7, 2, 8, 6]

EP = [4, 1, 2, 3, 2, 3, 4, 1]
P4 = [2, 4, 3, 1]

# -----------------------------
# S-Boxes
# -----------------------------

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


# ============================================================
# BASIC FUNCTIONS
# ============================================================

def permutation(bits, table):
    return ''.join(bits[i - 1] for i in table)


def left_shift(bits, n):
    return bits[n:] + bits[:n]


def xor_bits(a, b):
    return ''.join(
        str(int(x) ^ int(y))
        for x, y in zip(a, b)
    )


# ============================================================
# KEY GENERATION
# ============================================================

def generate_keys(key):

    # Apply P10
    key_p10 = permutation(key, P10)

    left = key_p10[:5]
    right = key_p10[5:]

    # Left shift by 1
    left = left_shift(left, 1)
    right = left_shift(right, 1)

    # Generate K1
    K1 = permutation(left + right, P8)

    # Left shift by 2
    left = left_shift(left, 2)
    right = left_shift(right, 2)

    # Generate K2
    K2 = permutation(left + right, P8)

    return K1, K2


# ============================================================
# S-BOX FUNCTION
# ============================================================

def sbox(bits, box):

    row = int(bits[0] + bits[3], 2)
    column = int(bits[1] + bits[2], 2)

    return format(box[row][column], '02b')


# ============================================================
# fk FUNCTION
# ============================================================

def fk(bits, key):

    left = bits[:4]
    right = bits[4:]

    # Expansion and permutation
    expanded = permutation(right, EP)

    # XOR with subkey
    temp = xor_bits(expanded, key)

    # Divide into two 4-bit parts
    left_part = temp[:4]
    right_part = temp[4:]

    # S-Box substitution
    s0_result = sbox(left_part, S0)
    s1_result = sbox(right_part, S1)

    # P4 permutation
    p4_result = permutation(
        s0_result + s1_result,
        P4
    )

    # XOR with left half
    new_left = xor_bits(left, p4_result)

    return new_left + right


# ============================================================
# S-DES ENCRYPTION
# ============================================================

def sdes_encrypt(plaintext, key):

    K1, K2 = generate_keys(key)

    # Initial permutation
    bits = permutation(plaintext, IP)

    # First round
    bits = fk(bits, K1)

    # Swap halves
    bits = bits[4:] + bits[:4]

    # Second round
    bits = fk(bits, K2)

    # Inverse initial permutation
    ciphertext = permutation(bits, IP_INV)

    return ciphertext


# ============================================================
# S-DES DECRYPTION
# ============================================================

def sdes_decrypt(ciphertext, key):

    K1, K2 = generate_keys(key)

    # Initial permutation
    bits = permutation(ciphertext, IP)

    # First round with K2
    bits = fk(bits, K2)

    # Swap halves
    bits = bits[4:] + bits[:4]

    # Second round with K1
    bits = fk(bits, K1)

    # Inverse initial permutation
    plaintext = permutation(bits, IP_INV)

    return plaintext


# ============================================================
# COUNTER MODE ENCRYPTION
# ============================================================

def ctr_encrypt(plaintext, key, counter_start):

    if len(plaintext) % 8 != 0:
        raise ValueError(
            "Plaintext length must be a multiple of 8 bits."
        )

    ciphertext = ""

    # Number of 8-bit blocks
    number_of_blocks = len(plaintext) // 8

    for i in range(number_of_blocks):

        # Counter value
        counter_value = counter_start + i

        # Convert counter to 8-bit binary
        counter = format(counter_value, '08b')

        # Encrypt counter using S-DES
        keystream = sdes_encrypt(counter, key)

        # Get plaintext block
        plaintext_block = plaintext[i * 8:(i + 1) * 8]

        # XOR plaintext with encrypted counter
        ciphertext_block = xor_bits(
            plaintext_block,
            keystream
        )

        ciphertext += ciphertext_block

    return ciphertext


# ============================================================
# COUNTER MODE DECRYPTION
# ============================================================

def ctr_decrypt(ciphertext, key, counter_start):

    if len(ciphertext) % 8 != 0:
        raise ValueError(
            "Ciphertext length must be a multiple of 8 bits."
        )

    plaintext = ""

    number_of_blocks = len(ciphertext) // 8

    for i in range(number_of_blocks):

        # Counter value
        counter_value = counter_start + i

        # Convert counter to 8-bit binary
        counter = format(counter_value, '08b')

        # Encrypt counter to generate keystream
        keystream = sdes_encrypt(counter, key)

        # Get ciphertext block
        ciphertext_block = ciphertext[i * 8:(i + 1) * 8]

        # XOR ciphertext with keystream
        plaintext_block = xor_bits(
            ciphertext_block,
            keystream
        )

        plaintext += plaintext_block

    return plaintext


# ============================================================
# TEST DATA FROM QUESTION
# ============================================================

key = "0111111101"

counter_start = 0

plaintext = "000000010000001000000100"

expected_ciphertext = "001110000100111100110010"


# ============================================================
# DISPLAY INPUT
# ============================================================

print("=" * 60)
print("       S-DES COUNTER (CTR) MODE")
print("=" * 60)

print("\nInput Parameters")
print("-" * 60)

print("Binary Key       :", key)
print("Starting Counter :", format(counter_start, '08b'))
print("Plaintext        :", plaintext)


# ============================================================
# GENERATE S-DES KEYS
# ============================================================

K1, K2 = generate_keys(key)

print("\nGenerated S-DES Subkeys")
print("-" * 60)

print("K1 :", K1)
print("K2 :", K2)


# ============================================================
# SHOW COUNTER VALUES AND KEYSTREAM
# ============================================================

print("\nCounter and Keystream")
print("-" * 60)

for i in range(3):

    counter = format(counter_start + i, '08b')

    keystream = sdes_encrypt(
        counter,
        key
    )

    print(
        "Counter:", counter,
        " -> Keystream:", keystream
    )


# ============================================================
# ENCRYPTION
# ============================================================

ciphertext = ctr_encrypt(
    plaintext,
    key,
    counter_start
)

print("\nEncryption")
print("-" * 60)

print("Plaintext : ", plaintext)
print("Ciphertext: ", ciphertext)


# ============================================================
# DECRYPTION
# ============================================================

decrypted_text = ctr_decrypt(
    ciphertext,
    key,
    counter_start
)

print("\nDecryption")
print("-" * 60)

print("Ciphertext: ", ciphertext)
print("Plaintext : ", decrypted_text)


# ============================================================
# VERIFICATION
# ============================================================

print("\nVerification")
print("-" * 60)

print("Expected Ciphertext : ", expected_ciphertext)
print("Generated Ciphertext: ", ciphertext)

if ciphertext == expected_ciphertext:
    print("\nEncryption Test: PASSED")
else:
    print("\nEncryption Test: FAILED")

if decrypted_text == plaintext:
    print("Decryption Test: PASSED")
else:
    print("Decryption Test: FAILED")



<img width="780" height="822" alt="image" src="https://github.com/user-attachments/assets/9c5dd5a1-1909-4e50-83a6-8de182eee8db" />


print("\n" + "=" * 60)
print("             PROGRAM COMPLETED")
print("=" * 60)
