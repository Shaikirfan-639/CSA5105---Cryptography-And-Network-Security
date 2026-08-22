# Diffie-Hellman demonstration

q = 23
a = 5

# Secret numbers
xA = 6
xB = 15

# Normal Diffie-Hellman
A = pow(a, xA, q)
B = pow(a, xB, q)

key_A = pow(B, xA, q)
key_B = pow(A, xB, q)

print("Normal DH:")
print("Alice sends:", A)
print("Bob sends  :", B)
print("Alice key  :", key_A)
print("Bob key    :", key_B)

# If they send x^a instead
A = pow(xA, a, q)
B = pow(xB, a, q)

print("\nUsing x^a:")
print("Alice sends:", A)
print("Bob sends  :", B)



<img width="955" height="778" alt="image" src="https://github.com/user-attachments/assets/7f0936de-0f80-4a67-81b6-232d88eb1ad6" />


# No common DH key can be obtained from these values
print("\nConclusion: x^a does NOT provide the Diffie-Hellman key agreement.")
