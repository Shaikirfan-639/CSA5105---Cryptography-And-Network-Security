# SHA-3: 1024-bit block size
rate = 1024
lane_size = 64
capacity = 1600 - rate

rate_lanes = rate // lane_size
capacity_lanes = capacity // lane_size

state = [1] * rate_lanes + [0] * capacity_lanes

print("Rate lanes     :", rate_lanes)
print("Capacity lanes :", capacity_lanes)
print("Initial state  :", state)

# Ignore permutation
rounds = 10
for r in range(1, rounds + 1):
    nonzero = sum(x != 0 for x in state[rate_lanes:])
    print("Round", r, ": Capacity nonzero lanes =", nonzero)

print("\nResult: Capacity lanes never become nonzero.")
print("Time required = Infinite (without permutation)")

<img width="1115" height="787" alt="image" src="https://github.com/user-attachments/assets/ee53fc11-87b2-441c-8cf8-db91aab56640" />
