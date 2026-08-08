11. Write a C program for possible keys does the Playfair cipher have? Ignore the fact that some keys
might produce identical encryption results. Express your answer as an approximate power of 2.
a. Now take into account the fact that some Playfair keys produce the same encryption results. How
many effectively unique keys does the Playfair cipher have?

import math

# Number of letters in Playfair matrix
n = 25

# (a) Total possible keys
total_keys = math.factorial(n)
power_total = math.log2(total_keys)

# (b) Effectively unique keys
unique_keys = total_keys // (5 * 5)
power_unique = math.log2(unique_keys)

print("Total possible keys =", total_keys)
print("Approximate power of 2 =", round(power_total))

print("Effectively unique keys =", unique_keys)
print("Approximate power of 2 =", round(power_unique))

<img width="1245" height="786" alt="image" src="https://github.com/user-attachments/assets/e158edba-faa5-4370-92d6-b794071501e2" />
