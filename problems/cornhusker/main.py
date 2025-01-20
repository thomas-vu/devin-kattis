# Read the input from stdin
A_values = list(map(int, input().split()))
L_values = list(map(int, input().split()))
N, KWF = map(int, input().split())

# Calculate the total number of kernels per ear
total_kernels = 0
for i in range(5):
    total_kernels += A_values[i] * L_values[i]

# Calculate the estimated number of bushels per acre
bushels_per_acre = (total_kernels * N) // KWF

# Output the result
print(bushels_per_acre)