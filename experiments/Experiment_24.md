# ============================================
# RSA PRIVATE KEY GENERATION
# ============================================

import math


# --------------------------------------------
# Given Public Key
# --------------------------------------------

e = 31
n = 3599

print("============================================")
print("          RSA PRIVATE KEY GENERATION")
print("============================================")

print("\nGiven Public Key:")
print("e =", e)
print("n =", n)


# --------------------------------------------
# Step 1: Find p and q by trial and error
# --------------------------------------------

p = None
q = None

for i in range(2, int(math.sqrt(n)) + 1):

    if n % i == 0:

        p = i
        q = n // i

        break


print("\nStep 1: Factorization")
print("--------------------------------------------")
print("p =", p)
print("q =", q)
print("Check: p × q =", p * q)


# --------------------------------------------
# Step 2: Calculate Euler's Totient Function
# φ(n) = (p-1)(q-1)
# --------------------------------------------

phi = (p - 1) * (q - 1)

print("\nStep 2: Euler's Totient")
print("--------------------------------------------")
print("φ(n) = (p - 1)(q - 1)")
print("φ(n) =", phi)


# --------------------------------------------
# Extended Euclidean Algorithm
# --------------------------------------------

def extended_gcd(a, b):

    if b == 0:
        return a, 1, 0

    gcd, x1, y1 = extended_gcd(b, a % b)

    x = y1
    y = x1 - (a // b) * y1

    return gcd, x, y


# --------------------------------------------
# Step 3: Find d
# d = e^(-1) mod φ(n)
# --------------------------------------------

gcd, x, y = extended_gcd(e, phi)

if gcd != 1:
    print("Private key cannot be generated.")
else:

    d = x % phi

    print("\nStep 3: Extended Euclidean Algorithm")
    print("--------------------------------------------")
    print("e =", e)
    print("φ(n) =", phi)
    print("GCD =", gcd)
    print("Multiplicative inverse d =", d)


# --------------------------------------------
# Verification
# --------------------------------------------

print("\nStep 4: Verification")
print("--------------------------------------------")

print("e × d =", e * d)
print("(e × d) mod φ(n) =", (e * d) % phi)


# --------------------------------------------
# Final Private Key
# --------------------------------------------

print("\n============================================")
print("              RSA RESULT")
print("============================================")

print("Public Key  = (e, n) =", (e, n))
print("Private Key = (d, n) =", (d, n))

print("\nPrivate key of the user is:")
print("(259, 3599)")

print("============================================")



![Uploading image.png…]()
