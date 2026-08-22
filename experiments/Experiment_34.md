from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)
iv = get_random_bytes(16)
msg = b"HELLO WORLD"

# 1-bit followed by zeros = 0x80 followed by zeros
pad = 16 - (len(msg) % 16)
if pad == 0: pad = 16
data = msg + b'\x80' + b'\x00' * (pad - 1)

# ECB
ecb = AES.new(key, AES.MODE_ECB)
c1 = ecb.encrypt(data)

# CBC
cbc = AES.new(key, AES.MODE_CBC, iv)
c2 = cbc.encrypt(data)

# CFB (16-byte segment)
cfb = AES.new(key, AES.MODE_CFB, iv, segment_size=128)
c3 = cfb.encrypt(data)

print("Plaintext:", msg)
print("ECB:", c1.hex())
print("CBC:", c2.hex())
print("CFB:", c3.hex())



<img width="908" height="781" alt="image" src="https://github.com/user-attachments/assets/0a372fef-2196-4e97-8377-fefe30fc25da" />
