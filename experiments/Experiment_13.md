13. Write a python program for Hill cipher succumbs to a known plaintext attack if sufficient plaintext–ciphertext pairs are provided. It is even easier to solve the Hill cipher if a chosen plaintext attack can be mounted.


import numpy as np

# Actual secret Hill cipher key
K = np.array([[9, 4],
              [5, 7]])

# Convert text to numbers: A=0, B=1, ..., Z=25
def text_to_numbers(text):
    return [ord(c) - ord('A') for c in text.upper()]

def numbers_to_text(nums):
    return ''.join(chr(n + ord('A')) for n in nums)

# Hill cipher encryption
def encrypt(text, key):
    nums = text_to_numbers(text)
    result = []

    for i in range(0, len(nums), 2):
        vector = np.array(nums[i:i+2])
        encrypted = key.dot(vector) % 26
        result.extend(encrypted)

    return numbers_to_text(result)

# ---------------- CHOSEN PLAINTEXT ATTACK ----------------

# Attacker chooses two plaintext blocks
P1 = "BA"
P2 = "AB"

# Obtain corresponding ciphertexts
C1 = encrypt(P1, K)
C2 = encrypt(P2, K)

print("Chosen plaintexts :", P1, P2)
print("Observed ciphertexts:", C1, C2)

# Convert plaintext and ciphertext pairs to matrices
P = np.array([
    text_to_numbers(P1),
    text_to_numbers(P2)
]).T

C = np.array([
    text_to_numbers(C1),
    text_to_numbers(C2)
]).T

print("\nPlaintext matrix P:")
print(P)

print("\nCiphertext matrix C:")
print(C)

# Since P = [[1,0],[0,1]], P inverse is also identity
# Therefore K = C * P^-1 (mod 26)

P_inv = np.array([
    [1, 0],
    [0, 1]
])

recovered_key = (C.dot(P_inv)) % 26

print("\nRecovered Hill Cipher Key:")
print(recovered_key)

# Test the recovered key
test_plaintext = "HELP"
test_ciphertext = encrypt(test_plaintext, recovered_key)

print("\nTest plaintext :", test_plaintext)
print("Encrypted text :", test_ciphertext)
