from collections import Counter

freq = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

def attack(cipher, top=10):
    count = Counter(c for c in cipher.upper() if c.isalpha())
    most = count.most_common()
    results = []

    for shift in range(26):
        plain = ""
        for c in cipher.upper():
            if c.isalpha():
                p = (ord(c)-65-shift) % 26
                plain += chr(p+65)
            else:
                plain += c

        score = sum(plain.count(x) for x in freq[:10])
        results.append((score, plain))

    return sorted(results, reverse=True)[:top]

cipher = input("Enter ciphertext: ")
top = int(input("How many plaintexts? "))

for i, (score, text) in enumerate(attack(cipher, top), 1):
    print(i, ":", text)



    <img width="870" height="792" alt="image" src="https://github.com/user-attachments/assets/6e0f6773-0b5a-409b-b7ef-c230258d34ff" />
