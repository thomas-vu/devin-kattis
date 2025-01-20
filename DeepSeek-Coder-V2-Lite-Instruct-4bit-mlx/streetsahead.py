n, q = map(int, input().split())
streets = [input() for _ in range(n)]
queries = [input().split() for _ in range(q)]

# Create a dictionary to map each street to its index
street_to_index = {street: idx for idx, street in enumerate(streets)}

# Process each query
for start, end in queries:
    start_idx = street_to_index[start]
    end_idx = street_to_index[end]
    # The number of intersections is the absolute difference in indices plus 1
    print(abs(start_idx - end_idx) + 1)