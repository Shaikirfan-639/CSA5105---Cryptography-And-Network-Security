15.Write a C program that can perform a letter frequency attack on any monoalphabetic substitution
cipher without human intervention. Your software should produce possible plaintexts in rough order of
likelihood. It would be good if your user interface allowed the user to specify “give me the top 10
possible plaintexts.”

import random
import math
import string
from collections import Counter

# English letter frequencies
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

# Common English words
COMMON_WORDS = {
    "the": 10, "and": 8, "that": 7, "this": 7,
    "with": 6, "from": 5, "have": 5, "will": 5,
    "you": 5, "are": 5, "for": 5, "not": 5,
    "was": 4, "but": 4, "they": 4, "is": 4,
    "to": 3, "of": 3, "in": 3, "on": 3
}


def decrypt(ciphertext, key):
    """Decrypt using a substitution key."""
    plaintext = ""

    for ch in ciphertext:
        if ch.isalpha():
            plaintext += key[ord(ch.lower()) - ord('a')]
        else:
            plaintext += ch

    return plaintext


def score_text(text):
    """Score plaintext using letter frequencies and common words."""
    letters = [c for c in text.lower() if c.isalpha()]

    if not letters:
        return -999999

    counts = Counter(letters)
    total = len(letters)

    # Frequency score
    score = 0

    for letter in alphabet:
        observed = counts.get(letter, 0) / total
        expected = ENGLISH_FREQ[letter] / 100

        score -= abs(observed - expected) * 100

    # Common-word score
    words = text.lower().split()

    for word in words:
        word = ''.join(c for c in word if c.isalpha())

        if word in COMMON_WORDS:
            score += COMMON_WORDS[word]

    return score


def random_key():
    """Generate a random substitution alphabet."""
    key = list(alphabet)
    random.shuffle(key)
    return key


def improve_key(ciphertext, key):
    """Improve key by swapping two letters."""
    best_key = key[:]
    best_score = score_text(decrypt(ciphertext, best_key))

    temperature = 20.0

    for _ in range(30000):
        new_key = best_key[:]

        a, b = random.sample(range(26), 2)
        new_key[a], new_key[b] = new_key[b], new_key[a]

        new_score = score_text(decrypt(ciphertext, new_key))

        if new_score > best_score:
            best_key = new_key
            best_score = new_score
        else:
            probability = math.exp(
                (new_score - best_score) / temperature
            )

            if random.random() < probability:
                best_key = new_key
                best_score = new_score

        temperature *= 0.9998

        if temperature < 0.1:
            temperature = 0.1

    return best_key, best_score


# ---------------- MAIN PROGRAM ----------------

ciphertext = input("Enter ciphertext: ")
top_n = int(input("How many possible plaintexts? "))

results = []

# Run several independent attacks
for _ in range(30):
    key = random_key()

    best_key, score = improve_key(ciphertext, key)

    plaintext = decrypt(ciphertext, best_key)

    results.append((score, plaintext))


# Remove duplicate plaintexts
unique_results = {}

for score, plaintext in results:
    unique_results[plaintext] = max(
        score,
        unique_results.get(plaintext, -999999)
    )

# Sort by likelihood
results = sorted(
    [(score, text) for text, score in unique_results.items()],
    reverse=True
)

# Display results
print("\nPossible plaintexts in rough order of likelihood:")
print("-" * 70)

for i, (score, plaintext) in enumerate(results[:top_n], 1):
    print(f"{i}. Score = {score:.2f}")
    print("   ", plaintext)


<img width="995" height="810" alt="image" src="https://github.com/user-attachments/assets/09495a18-e568-4d17-b745-14f8fde99260" />




