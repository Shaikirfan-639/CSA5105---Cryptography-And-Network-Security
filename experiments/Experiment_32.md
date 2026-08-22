import hashlib, random

# Small demonstration values
p, q, g = 23, 11, 4
x = 3                      # private key
y = pow(g, x, p)           # public key
m = "HELLO"
h = int(hashlib.sha256(m.encode()).hexdigest(), 16) % q

def dsa_sign():
    k = random.randint(1, q-1)
    r = pow(g, k, p) % q
    s = (pow(k, -1, q) * (h + x*r)) % q
    return r, s

print("DSA Signature 1:", dsa_sign())
print("DSA Signature 2:", dsa_sign())

# Simplified RSA demonstration
n, d = 3233, 2753
H = h % n

print("RSA Signature 1:", pow(H, d, n))
print("RSA Signature 2:", pow(H, d, n))

<img width="825" height="798" alt="image" src="https://github.com/user-attachments/assets/85fb30d9-7226-47b1-8721-90112d0a8657" />
