import math

n = 3599
e = 31

# Suppose plaintext block shares a factor with n
m = 59

# Find common factor
p = math.gcd(m, n)
q = n // p

# Calculate phi(n)
phi = (p - 1) * (q - 1)

# Find private key d
d = pow(e, -1, phi)

print("Common factor p =", p)
print("Other factor q =", q)
print("phi(n) =", phi)
print("Private key d =", d)
print("Private Key =", (d, n))



<img width="725" height="687" alt="image" src="https://github.com/user-attachments/assets/737dbc30-2ff1-4633-9056-0019c6a1abd7" />
