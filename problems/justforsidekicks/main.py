N, Q = map(int, input().split())
values = list(map(int, input().split()))
gems = input()

# Convert the string of gem types to a list of integers
gem_types = [int(c) for c in gems]

# Initialize a dictionary to store the total value of each gem type
gem_type_values = {i + 1: [] for i in range(6)}

# Calculate the total value of each gem type initially
for i, gem_type in enumerate(gem_types):
    gem_type_values[gem_type].append(values[gem_type - 1])

# Process the queries
for _ in range(Q):
    query = list(map(int, input().split()))
    
    if query[0] == 1:
        K, P = query[1], query[2]
        old_type = gem_types[K - 1]
        # Update the value of the old type by removing the K-th gem's value
        total_value = sum(gem_type_values[old_type]) - gem_type_values[old_type][K - 1]
        # Update the new type by adding the K-th gem's value
        gem_type_values[P].append(values[P - 1])
        # Update the gem type at position K to P
        gem_types[K - 1] = P
    elif query[0] == 2:
        P, V = query[1], query[2]
        # Update the value of the gem type P to V
        total_value = sum(gem_type_values[P])
        gem_type_values[P] = [V]
    elif query[0] == 3:
        L, R = query[1], query[2]
        # Calculate the total value of gems from L to R inclusive
        total_value = sum(values[gem - 1] for gem in gem_types[L - 1:R])
        print(total_value)