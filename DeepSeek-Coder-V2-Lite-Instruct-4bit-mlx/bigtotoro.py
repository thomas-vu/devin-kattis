N, K = map(int, input().split())
acorns = list(map(int, input().split()))

# Create a set to store the unique acorn sizes that Totoro can eat
possible_sizes = set()

# Function to calculate the maximum size Totoro can achieve
def max_size(N, K, acorns):
    for acorn in acorns:
        if (acorn % 4) == (K % 4):
            possible_sizes.add(acorn + K)
    
    return max(possible_sizes) if possible_sizes else K

# Output the result
print(max_size(N, K, acorns))