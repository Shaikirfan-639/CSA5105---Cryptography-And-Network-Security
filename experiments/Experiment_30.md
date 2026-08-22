from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

K = get_random_bytes(16)
X = b"ABCDEFGHIJKLMNOP"       # 1 block
cipher = AES.new(K, AES.MODE_ECB)

# CBC-MAC of X
T = cipher.encrypt(X)

# Forged two-block message
X2 = bytes(a ^ b for a, b in zip(X, T))
forged = X + X2

# CBC-MAC of forged message
C1 = cipher.encrypt(X)
C2 = cipher.encrypt(bytes(a ^ b for a, b in zip(C1, X2)))

print("MAC of X       :", T.hex())
print("Forged message :", forged.hex())
print("MAC of X||X^T  :", C2.hex())
print("MACs equal?    :", T == C2)

<img width="1221" height="706" alt="image" src="https://github.com/user-attachments/assets/a49c73a9-ea35-4aba-b3be-6a26f3ffd8b7" />
