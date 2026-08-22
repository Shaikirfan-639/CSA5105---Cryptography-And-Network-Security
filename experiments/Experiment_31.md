# CMAC Subkey Generation

def left_shift(x, n):
    return ((x << n) & ((1 << 128) - 1))

def cmac_subkeys(L, bits=128):
    Rb = 0x87 if bits == 128 else 0x1B
    mask = (1 << bits) - 1

    K1 = left_shift(L, 1) & mask
    if L & (1 << (bits - 1)):
        K1 ^= Rb

    K2 = left_shift(K1, 1) & mask
    if K1 & (1 << (bits - 1)):
        K2 ^= Rb

    return K1, K2

# Example: result of encrypting the all-zero block
L = 0x123456789ABCDEF0123456789ABCDEF0

K1, K2 = cmac_subkeys(L)

print("L  =", hex(L))
print("K1 =", hex(K1))
print("K2 =", hex(K2))

print("\n64-bit constant  = 0x1B")
print("128-bit constant = 0x87")


<img width="1202" height="815" alt="image" src="https://github.com/user-attachments/assets/f9e86cb6-0b3b-4df0-b600-0fc85908bfee" />
