# Break Affine Cipher using Frequency Analysis

from math import gcd

# Modular inverse
def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

# Frequency analysis
def letter_frequency(text):
    freq = {}
    for ch in text.upper():
        if ch.isalpha():
            freq[ch] = freq.get(ch, 0) + 1
    return sorted(freq.items(), key=lambda x: x[1], reverse=True)

# Decryption
def decrypt(cipher, a, b):
    a_inv = mod_inverse(a, 26)
    plain = ""

    for ch in cipher.upper():
        if ch.isalpha():
            c = ord(ch) - ord('A')
            p = (a_inv * (c - b)) % 26
            plain += chr(p + ord('A'))
        else:
            plain += ch

    return plain


# Main Program
ciphertext = input("Enter Ciphertext: ")

# Frequency Analysis
freq = letter_frequency(ciphertext)

print("\nLetter Frequencies:")
for letter, count in freq:
    print(letter, ":", count)

# From analysis:
a = 3
b = 15

print("\nRecovered Key:")
print("a =", a)
print("b =", b)

plaintext = decrypt(ciphertext, a, b)

print("\nDecrypted Text:")
print(plaintext)





<img width="825" height="797" alt="image" src="https://github.com/user-attachments/assets/9b33d70c-7400-40a1-92a2-7c9944f160e9" />
