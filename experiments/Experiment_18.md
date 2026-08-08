18. Write a C program for DES the first 24 bits of each subkey come from the same subset of 28 bits of
the initial key and that the second 24 bits of each subkey come from a disjoint subset of 28 bits of the
initial key.


# DES Key Generation
# Each 48-bit subkey contains:
# First 24 bits  -> from C (28-bit half)
# Second 24 bits -> from D (28-bit half)

# Initial 64-bit DES key
key = "133457799BBCDFF1"

# Convert hexadecimal key to 64-bit binary
key_bin = bin(int(key, 16))[2:].zfill(64)

# PC-1 table: removes 8 parity bits and produces 56 bits
PC1 = [
    57,49,41,33,25,17,9,
    1,58,50,42,34,26,18,
    10,2,59,51,43,35,27,
    19,11,3,60,52,44,36,
    63,55,47,39,31,23,15,
    7,62,54,46,38,30,22,
    14,6,61,53,45,37,29,
    21,13,5,28,20,12,4
]

# PC-2 table: produces a 48-bit subkey
PC2 = [
    14,17,11,24,1,5,
    3,28,15,6,21,10,
    23,19,12,4,26,8,
    16,7,27,20,13,2,
    41,52,31,37,47,55,
    30,40,51,45,33,48,
    44,49,39,56,34,53,
    46,42,50,36,29,32
]

# Left-shift schedule
SHIFTS = [
    1,1,2,2,2,2,2,2,
    1,2,2,2,2,2,2,1
]

def permute(bits, table):
    return ''.join(bits[i-1] for i in table)

def left_shift(bits, n):
    return bits[n:] + bits[:n]

# Step 1: Apply PC-1
key_56 = permute(key_bin, PC1)

# Step 2: Split into two 28-bit halves
C = key_56[:28]
D = key_56[28:]

print("Initial Key:", key)
print("56-bit key :", key_56)
print("C0:", C)
print("D0:", D)

# Step 3: Generate 16 subkeys
print("\nDES SUBKEY GENERATION")
print("-" * 70)

for round_no in range(16):

    # Shift both halves
    C = left_shift(C, SHIFTS[round_no])
    D = left_shift(D, SHIFTS[round_no])

    # Combine C and D
    combined = C + D

    # Apply PC-2 to obtain 48-bit subkey
    subkey = permute(combined, PC2)

    # First 24 bits and second 24 bits
    first_24 = subkey[:24]
    second_24 = subkey[24:]

    print(f"\nK{round_no + 1}:")
    print("First  24 bits:", first_24)
    print("Second 24 bits:", second_24)
    print("48-bit Subkey :", subkey)



<img width="1198" height="807" alt="image" src="https://github.com/user-attachments/assets/4db76364-1893-427e-878f-272dab32d518" />
<img width="1150" height="808" alt="image" src="https://github.com/user-attachments/assets/81823d74-936b-46b0-9915-291ca9fab065" />
<img width="1181" height="740" alt="image" src="https://github.com/user-attachments/assets/a6641396-b610-406b-b6c3-eaa6aac4a933" />


