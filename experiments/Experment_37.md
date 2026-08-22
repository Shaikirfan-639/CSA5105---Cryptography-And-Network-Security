# Letter Frequency Attack

from collections import Counter

freq = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

def attack(cipher, n=10):
    count = Counter(c for c in cipher.upper() if c.isalpha())
    common = [x for x, _ in count.most_common()]
    results = []

    for shift in range(26):
        table = {}
        for i, c in enumerate(common):
            table[c] = freq[(i + shift) % 26]

        plain = ''.join(table.get(c, c) for c in cipher.upper())
        results.append(plain)

    return results[:n]

cipher = "WKH TXLFN EURZQ IRA MXPSV"
for i, text in enumerate(attack(cipher, 10), 1):
    print(i, ":", text)

    <img width="901" height="837" alt="image" src="https://github.com/user-attachments/assets/b8f1f6c6-51ef-40d2-a846-d5eb9f64d0c2" />
