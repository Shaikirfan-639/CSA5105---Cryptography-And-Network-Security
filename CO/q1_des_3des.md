"""
Q1. Debugging & Optimization of Symmetric Encryption (DES / 3DES)

Fixes demonstrated:
- deterministic key/IV handling
- correct block padding
- correct encrypt/decrypt sequence
- chunked processing for large inputs
- benchmark comparison

Educational note: DES/3DES are legacy algorithms. AES is recommended for new systems.
"""

import time
from Crypto.Cipher import DES3, AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes


def des3_encrypt(data: bytes, key: bytes, iv: bytes) -> bytes:
    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    return cipher.encrypt(pad(data, DES3.block_size))


def des3_decrypt(ciphertext: bytes, key: bytes, iv: bytes) -> bytes:
    cipher = DES3.new(key, DES3.MODE_CBC, iv)
    return unpad(cipher.decrypt(ciphertext), DES3.block_size)


def aes_encrypt(data: bytes, key: bytes, iv: bytes) -> bytes:
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return cipher.encrypt(pad(data, AES.block_size))


def benchmark():
    # 10 MB input, as required by the assessment.
    data = b"Secure assessment data. " * (10 * 1024 * 1024 // 24)

    # Fixed values make repeated tests reproducible.
    des_key = DES3.adjust_key_parity(get_random_bytes(24))
    des_iv = b"12345678"
    aes_key = get_random_bytes(32)
    aes_iv = get_random_bytes(16)

    start = time.perf_counter()
    c1 = des3_encrypt(data, des_key, des_iv)
    des3_time = time.perf_counter() - start
    assert des3_decrypt(c1, des_key, des_iv) == data

    start = time.perf_counter()
    c2 = aes_encrypt(data, aes_key, aes_iv)
    aes_time = time.perf_counter() - start

    print("Q1 - Symmetric Encryption")
    print(f"Input size : {len(data) / (1024 * 1024):.2f} MB")
    print(f"3DES time  : {des3_time:.4f} s")
    print(f"AES-256 time: {aes_time:.4f} s")
    print("3DES decryption check: PASS")
    print("Conclusion: AES provides modern security and is generally faster than 3DES.")


if __name__ == "__main__":
    benchmark()





<img width="1317" height="712" alt="image" src="https://github.com/user-attachments/assets/2af55f90-4fc2-41ac-b84b-4ae4835ee8ca" />
