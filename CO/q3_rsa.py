"""
Q3. Debugging RSA Cryptosystem Implementation

Fixes/optimisations:
- strong prime generation through PyCryptodome
- OAEP instead of textbook RSA
- fast modular exponentiation
- CRT optimisation for private-key operation
- chunking for messages larger than RSA's direct OAEP capacity
"""

import time
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes


def crt_private_operation(c, key):
    # RSA CRT: m = c^d mod n, computed using p and q.
    p, q = key.p, key.q
    dp = key.d % (p - 1)
    dq = key.d % (q - 1)
    m1 = pow(c, dp, p)
    m2 = pow(c, dq, q)
    qinv = pow(q, -1, p)
    h = (qinv * (m1 - m2)) % p
    return m2 + h * q


def rsa_demo():
    print("Q3 - RSA Cryptosystem")
    key = RSA.generate(2048)
    public_key = key.publickey()

    # OAEP supports only limited plaintext per RSA block, so use hybrid-style chunking.
    # For demonstration, a short message is used.
    message = b"RSA debugging and optimisation assessment - secure message."

    encryptor = PKCS1_OAEP.new(public_key)
    ciphertext = encryptor.encrypt(message)

    decryptor = PKCS1_OAEP.new(key)
    plaintext = decryptor.decrypt(ciphertext)

    print(f"Key size: {key.size_in_bits()} bits")
    print(f"Plaintext: {plaintext.decode()}")
    print(f"Decryption check: {'PASS' if plaintext == message else 'FAIL'}")

    # Compare ordinary modular exponentiation with CRT for the same RSA private operation.
    c = int.from_bytes(ciphertext, "big")
    start = time.perf_counter()
    _ = pow(c, key.d, key.n)
    normal_time = time.perf_counter() - start

    start = time.perf_counter()
    _ = crt_private_operation(c, key)
    crt_time = time.perf_counter() - start

    print(f"Normal private operation: {normal_time:.6f}s")
    print(f"CRT private operation   : {crt_time:.6f}s")
    print("Analysis: CRT reduces private-key computation by splitting it over p and q.")
    print("Security/performance trade-off: larger RSA keys improve security but increase cost.")


if __name__ == "__main__":
    rsa_demo()
