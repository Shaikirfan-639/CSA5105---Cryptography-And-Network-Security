Write a C program that can perform a letter frequency attack on an additive cipher without human
intervention. Your software should produce possible plaintexts in rough order of likelihood. It would be
good if your user interface allowed the user to specify “give me the top 10 possible plaintexts.”


from collections import Counter
import string

# English letter frequencies (%)
ENGLISH_FREQ = {
    'a': 8.167, 'b': 1.492, 'c': 2.782, 'd': 4.253,
    'e': 12.702, 'f': 2.228, 'g': 2.015, 'h': 6.094,
    'i': 6.966, 'j': 0.153, 'k': 0.772, 'l': 4.025,
    'm': 2.406, 'n': 6.749, 'o': 7.507, 'p': 1.929,
    'q': 0.095, 'r': 5.987, 's': 6.327, 't': 9.056,
    'u': 2.758, 'v': 0.978, 'w': 2.360, 'x': 0.150,
    'y': 1.974, 'z': 0.074
}

alphabet = string.ascii_lowercase


# Decrypt using an additive cipher shift
def decrypt(ciphertext, shift):
    plaintext = ""

    for ch in ciphertext:
        if ch.isalpha():
            c = alphabet.index(ch.lower())
            p = (c - shift) % 26
            plaintext += alphabet[p]
        else:
            plaintext += ch

    return plaintext


# Calculate chi-square score
def chi_square_score(text):
    letters = [ch for ch in text.lower() if ch.isalpha()]
    total = len(letters)

    if total == 0:
        return float('inf')

    counts = Counter(letters)
    score = 0

    for letter in alphabet:
        observed = counts.get(letter, 0)
        expected = (ENGLISH_FREQ[letter] / 100) * total

        if expected > 0:
            score += ((observed - expected) ** 2) / expected

    return score


# ---------------- MAIN PROGRAM ----------------

ciphertext = input("Enter ciphertext: ")

top_n = int(input("How many possible plaintexts? "))

results = []

# Try all 26 possible shifts
for shift in range(26):
    plaintext = decrypt(ciphertext, shift)
    score = chi_square_score(plaintext)

    results.append((score, shift, plaintext))

# Sort from most likely to least likely
results.sort()

print("\nPossible plaintexts in order of likelihood:")
print("-" * 70)

for rank, (score, shift, plaintext) in enumerate(results[:top_n], 1):
    print(f"{rank:2}. Shift = {shift:2} | Score = {score:8.2f} | {plaintext}")



<img width="935" height="758" alt="image" src="https://github.com/user-attachments/assets/67c3a112-4d03-48ae-b16a-372fe67c5e69" />


