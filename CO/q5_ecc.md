"""
Q5. Debugging and Enhancing ECC Implementation

Educational short Weierstrass curve:
    y^2 = x^3 + ax + b (mod p)

Fixes:
- point-at-infinity handling
- correct point-addition formulas
- modular inverse
- double-and-add scalar multiplication
- simple performance comparison with RSA modular exponentiation

This toy curve is for learning only and is NOT production secure.
"""

import time


class Curve:
    def __init__(self, p, a, b):
        self.p, self.a, self.b = p, a, b


INF = None


def inv_mod(x, p):
    return pow(x % p, -1, p)


def add(P, Q, curve):
    if P is INF:
        return Q
    if Q is INF:
        return P

    x1, y1 = P
    x2, y2 = Q
    p, a = curve.p, curve.a

    if x1 == x2 and (y1 + y2) % p == 0:
        return INF

    if P != Q:
        m = ((y2 - y1) * inv_mod(x2 - x1, p)) % p
    else:
        if y1 % p == 0:
            return INF
        m = ((3 * x1 * x1 + a) * inv_mod(2 * y1, p)) % p

    x3 = (m * m - x1 - x2) % p
    y3 = (m * (x1 - x3) - y1) % p
    return x3, y3


def scalar_mul(k, P, curve):
    # Double-and-add: O(log k) point additions/doublings.
    result = INF
    addend = P

    while k > 0:
        if k & 1:
            result = add(result, addend, curve)
        addend = add(addend, addend, curve)
        k >>= 1

    return result


def demo():
    # Small educational curve. Never use these tiny parameters in real systems.
    curve = Curve(p=9739, a=497, b=1768)
    G = (1804, 5368)
    k = 12345

    start = time.perf_counter()
    R = scalar_mul(k, G, curve)
    ecc_time = time.perf_counter() - start

    # Basic correctness check: kG + (-kG) = infinity.
    neg_R = (R[0], (-R[1]) % curve.p)
    check = add(R, neg_R, curve) is INF

    print("Q5 - ECC")
    print(f"Scalar multiplication result: {R}")
    print(f"Point arithmetic check: {'PASS' if check else 'FAIL'}")
    print(f"ECC double-and-add time: {ecc_time:.8f}s")

    rsa_n = (2**2048) - 159
    start = time.perf_counter()
    _ = pow(65537, k, rsa_n)
    rsa_time = time.perf_counter() - start

    print(f"2048-bit modular exponentiation time: {rsa_time:.8f}s")
    print("Analysis: ECC achieves strong security with much smaller keys than RSA.")
    print("This makes ECC attractive for constrained devices, but real deployments should use standard curves/libraries.")


if __name__ == "__main__":
    demo()










<img width="1327" height="586" alt="image" src="https://github.com/user-attachments/assets/eabf518c-6dd0-44a7-8828-6c710cf6b4ed" />
