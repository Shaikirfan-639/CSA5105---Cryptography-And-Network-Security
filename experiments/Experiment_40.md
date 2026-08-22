from collections import Counter

freq = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

def attack(cipher, top=10):
    count = Counter(c for c in cipher.upper() if c.isalpha())
    common = [c for c, _ in count.most_common()]
    results = []

    for shift in range(26):
        key = {c: freq[(i + shift) % 26] for i, c in enumerate(common)}
        text = ''.join(key.get(c, c) for c in cipher.upper())
        score = sum(text.count(c) for c in freq[:10])
        results.append((score, text))

    return sorted(results, reverse=True)[:top]

cipher = input("Enter ciphertext: ")
top = int(input("Enter number of plaintexts: "))

for i, (_, text) in enumerate(attack(cipher, top), 1):
    print(f"{i}. {text}")

    <img width="1190" height="810" alt="image" src="https://github.com/user-attachments/assets/5c6a1035-5dea-43a2-bd61-fde5545f45da" />
