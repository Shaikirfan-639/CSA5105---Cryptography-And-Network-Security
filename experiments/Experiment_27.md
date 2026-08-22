# RSA character-by-character attack

e = 65537
n = 999999937  # example large modulus

# Attacker creates a lookup table for A-Z
table = {pow(m, e, n): chr(65 + m) for m in range(26)}

# Example encrypted character
c = pow(7, e, n)   # plaintext = 7 = H

# Find plaintext using the table
print("Encrypted:", c)
print("Recovered character:", table[c])

<img width="1033" height="660" alt="image" src="https://github.com/user-attachments/assets/54bd4c67-5ea3-42e1-b014-1a7d2162359b" />
