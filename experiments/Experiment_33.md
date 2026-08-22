from Crypto.Cipher import DES

key = b"12345678"
text = b"ABCDEFGH"

cipher = DES.new(key, DES.MODE_ECB)

encrypted = cipher.encrypt(text)
decrypted = cipher.decrypt(encrypted)

print("Plaintext :", text.decode())
print("Encrypted :", encrypted.hex())
print("Decrypted :", decrypted.decode())





<img width="786" height="622" alt="image" src="https://github.com/user-attachments/assets/b4657abc-cabe-4e07-a929-ee07653aef8f" />
