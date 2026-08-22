import numpy as np

P = np.array([[1, 2], [3, 5]])
C = np.array([[5, 8], [9, 14]])

det = int(round(np.linalg.det(P))) % 26
inv = pow(det, -1, 26)

P_inv = inv * np.array([[5, -2], [-3, 1]])
P_inv %= 26

K = (C @ P_inv) % 26

print("Recovered Key:")
print(K.astype(int))

print("\nVerification:")
print((K @ P) % 26)







<img width="841" height="685" alt="image" src="https://github.com/user-attachments/assets/306564b7-05e5-4aae-9e7e-c2ebca33605d" />
