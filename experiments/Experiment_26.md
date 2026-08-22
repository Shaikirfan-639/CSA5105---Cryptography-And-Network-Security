from math import gcd

# Old RSA keys
p, q = 61, 53
n = p * q
e = 17
phi = (p-1) * (q-1)
d = pow(e, -1, phi)

print("Old Public Key :", (e, n))
print("Old Private Key:", (d, n))

# Bob changes e and d but keeps n
new_e = 7
new_d = pow(new_e, -1, phi)

print("New Public Key :", (new_e, n))
print("New Private Key:", (new_d, n))

print("\nSafe?", "No - modulus n is still the same.")
print("Correct solution: Generate new p, q and a new n.")

<img width="840" height="707" alt="image" src="https://github.com/user-attachments/assets/6d644b7b-eba6-4494-805f-2ff10d5e5069" />
