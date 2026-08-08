
# Playfair Cipher Decryption

def generate_key_matrix(key):
    key = key.upper().replace("J", "I")
    matrix = []
    used = set()

    for ch in key:
        if ch.isalpha() and ch not in used:
            matrix.append(ch)
            used.add(ch)

    for ch in "ABCDEFGHIKLMNOPQRSTUVWXYZ":  # J omitted
        if ch not in used:
            matrix.append(ch)
            used.add(ch)

    return [matrix[i:i+5] for i in range(0, 25, 5)]


def find_position(matrix, ch):
    if ch == 'J':
        ch = 'I'
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == ch:
                return i, j


def decrypt(ciphertext, matrix):
    ciphertext = ''.join(ch for ch in ciphertext.upper() if ch.isalpha())
    plaintext = ""

    for i in range(0, len(ciphertext), 2):
        a = ciphertext[i]
        b = ciphertext[i + 1]

        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)

        if r1 == r2:  # Same row
            plaintext += matrix[r1][(c1 - 1) % 5]
            plaintext += matrix[r2][(c2 - 1) % 5]

        elif c1 == c2:  # Same column
            plaintext += matrix[(r1 - 1) % 5][c1]
            plaintext += matrix[(r2 - 1) % 5][c2]

        else:  # Rectangle
            plaintext += matrix[r1][c2]
            plaintext += matrix[r2][c1]

    return plaintext


# Main
key = input("Enter Playfair Key: ")
cipher = """KXJEY UREBE ZWEHE WRYTU HEYFS
KREHE GOYFI WTTTU OLKSY CAJPO
BOTEI ZONTX BYBNT GONEY CUZWR
GDSON SXBOU YWRHE BAAHY USEDQ"""

matrix = generate_key_matrix(key)

print("\nKey Matrix:")
for row in matrix:
    print(" ".join(row))

print("\nDecrypted Text:")
print(decrypt(cipher, matrix))



<img width="1111" height="722" alt="image" src="https://github.com/user-attachments/assets/a57ca288-ac41-47f6-b29a-e458779062c3" />
