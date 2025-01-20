P, T, L = map(int, input().split())
initial_indices = list(map(int, input().split()))

# Create a list to simulate the number of fries each person has
fries = [0] * (10**7 + 2)
for index in initial_indices:
    fries[index] = P

# Simulate the process for T time steps
for _ in range(T):
    new_fries = [0] * (10**7 + 2)
    for i in range(len(fries)):
        if fries[i] >= 1:
            half = fries[i] / 2
            new_fries[i - 1] += half
            new_fries[i + 1] += half
            fries[i] -= fries[i]
    fries = new_fries

# Count the number of people who have at least L fries
full_count = sum(1 for f in fries if f >= L)
print(full_count)