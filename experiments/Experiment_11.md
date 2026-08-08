*/11. Write a C program for possible keys does the Playfair cipher have? Ignore the fact that some keys
might produce identical encryption results. Express your answer as an approximate power of 2./*

import math

# Playfair cipher uses a 5x5 matrix = 25 letters
n = 25

# Number of possible keys
keys = math.factorial(n)

# Convert to approximate power of 2
power = math.log2(keys)

print("Number of possible Playfair keys:", keys)
print("Approximate power of 2: 2^", round(power))


<img width="1327" height="632" alt="image" src="https://github.com/user-attachments/assets/d8b9c063-1f0c-401c-8c62-1211191a5a9b" />
