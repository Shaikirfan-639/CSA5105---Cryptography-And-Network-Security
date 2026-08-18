"""
Q2. Performance Analysis of Block Cipher Modes of Operation

Modes compared:
ECB, CBC, CFB and OFB.

Debugging points:
- PKCS#7 padding is applied for CBC/ECB.
- CFB/OFB are stream-like modes and do not require padding.
- A fresh random IV is used for every encryption.
- Decryption uses exactly the same IV as encryption.
"""

import time
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

MODES = {
    "ECB": AES.MODE_ECB,
    "CBC": AES.MODE_CBC,
    "CFB": AES.MODE_CFB,
    "OFB": AES.MODE_OFB,
}


def encrypt(data, key, mode_name):
    mode = MODES[mode_name]
    iv = None if mode_name == "ECB" else get_random_bytes(16)

    if mode_name in ("ECB", "CBC"):
        payload = pad(data, AES.block_size)
    else:
        payload = data

    cipher = AES.new(key, mode, iv=iv) if iv else AES.new(key, mode)
    return iv, cipher.encrypt(payload)


def decrypt(ciphertext, key, mode_name, iv):
    mode = MODES[mode_name]
    cipher = AES.new(key, mode, iv=iv) if iv else AES.new(key, mode)
    plaintext = cipher.decrypt(ciphertext)

    if mode_name in ("ECB", "CBC"):
        plaintext = unpad(plaintext, AES.block_size)

    return plaintext


def benchmark():
    data = b"Real-time secure communication data. " * 200000
    key = get_random_bytes(32)

    print("Q2 - Block Cipher Modes")
    print(f"Data size: {len(data) / (1024 * 1024):.2f} MB")
    print()

    for name in MODES:
        start = time.perf_counter()
        iv, ciphertext = encrypt(data, key, name)
        enc_time = time.perf_counter() - start

        start = time.perf_counter()
        plaintext = decrypt(ciphertext, key, name, iv)
        dec_time = time.perf_counter() - start

        assert plaintext == data
        print(f"{name:4} | Encrypt: {enc_time:.4f}s | Decrypt: {dec_time:.4f}s | PASS")

    print("\nAnalysis: ECB is not recommended because equal plaintext blocks reveal patterns.")
    print("For real applications, authenticated modes such as AES-GCM are preferred.")
    print("Among the requested modes, CFB/OFB avoid padding overhead and can suit streaming data.")


if __name__ == "__main__":
    benchmark()
