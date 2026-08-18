"""
Q4. Optimization and Security Analysis of Diffie-Hellman Key Exchange

Fixes:
- correct modular arithmetic: pow(g, private, p)
- shared secret is computed using the peer public value
- authentication is added with Ed25519 signatures to reduce MITM risk
- exponentiation is benchmarked

This is an educational demonstration, not a production protocol.
"""

import time
from Crypto.PublicKey import ECC
from Crypto.Signature import eddsa
from Crypto.Hash import SHA256


def demo():
    # RFC 3526-style 2048-bit MODP group prime.
    p = int(
        "FFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD1"
        "29024E088A67CC74020BBEA63B139B22514A08798E3404DD"
        "EF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245"
        "E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7ED"
        "EE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3D"
        "C2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F8"
        "36FF2B3DDA6D7E0F5A5F151B8B3F1D7A431D"
        "A3F1A6E0C8F4F3"
        "FFFFFFFFFFFFFFFF",
        16,
    )
    g = 2

    alice_private = 123456789
    bob_private = 987654321

    start = time.perf_counter()
    alice_public = pow(g, alice_private, p)
    bob_public = pow(g, bob_private, p)
    alice_shared = pow(bob_public, alice_private, p)
    bob_shared = pow(alice_public, bob_private, p)
    elapsed = time.perf_counter() - start

    print("Q4 - Diffie-Hellman")
    print(f"Shared keys equal: {alice_shared == bob_shared}")
    print(f"Exponentiation/exchange time: {elapsed:.6f}s")
    print(f"Derived key digest: {SHA256.new(alice_shared.to_bytes((p.bit_length()+7)//8, 'big')).hexdigest()[:32]}")

    # Authentication enhancement: Ed25519 signatures.
    alice_sign_key = ECC.generate(curve="Ed25519")
    signer = eddsa.new(alice_sign_key, "rfc8032")
    transcript = str(alice_public).encode() + str(bob_public).encode()
    signature = signer.sign(transcript)

    verifier = eddsa.new(alice_sign_key.public_key(), "rfc8032")
    try:
        verifier.verify(transcript, signature)
        print("Authenticated transcript: PASS")
    except ValueError:
        print("Authenticated transcript: FAIL")

    print("Analysis: unauthenticated DH is vulnerable to MITM.")
    print("Adding signatures increases computation slightly but provides authentication.")


if __name__ == "__main__":
    demo()
