# Keyword Monoalphabetic Cipher

import string

# Plain alphabet
plain = string.ascii_lowercase

# Keyword
keyword = "CIPHER".lower()

# Generate cipher alphabet
cipher = ""

# Add keyword letters without duplicates
for ch in keyword:
    if ch not in cipher:
        cipher += ch

# Add remaining letters
for ch in plain:
    if ch not in cipher:
        cipher += ch

print("Plain Alphabet : ", plain)
print("Cipher Alphabet:", cipher)

# Encryption
def encrypt(text):
    result = ""
    for ch in text.lower():
        if ch.isalpha():
            index = plain.index(ch)
            result += cipher[index]
        else:
            result += ch
    return result

# Decryption
def decrypt(text):
    result = ""
    for ch in text.lower():
        if ch.isalpha():
            index = cipher.index(ch)
            result += plain[index]
        else:
            result += ch
    return result

# Main Program
plaintext = input("\nEnter Plaintext: ")

encrypted = encrypt(plaintext)
print("Encrypted Text:", encrypted)

decrypted = decrypt(encrypted)
print("Decrypted Text:", decrypted)






<img width="705" height="720" alt="image" src="https://github.com/user-attachments/assets/347d4be9-dcb1-498f-af86-4a6f19da97d6" />
