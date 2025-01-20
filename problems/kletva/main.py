def min_keys_to_open_locks(W, L, N, upper_edges, lower_edges):
    # Helper function to calculate the GCD of two numbers
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    # Helper function to calculate the least common multiple of two numbers
    def lcm(a, b):
        return (a * b) // gcd(a, b)
    
    # Calculate the GCD of differences between adjacent elements in edges
    def calculate_gcd_differences(edges):
        gcds = []
        for i in range(len(edges)):
            if i == 0:
                gcds.append(edges[i])
            else:
                gcds.append(abs(edges[i] - edges[i-1]))
        return gcds
    
    # Calculate the GCD of all differences in edges
    def calculate_overall_gcd(edges):
        overall_gcd = 0
        for edge in edges:
            overall_gcd = gcd(overall_gcd, edge)
        return overall_gcd
    
    # Calculate the GCD of differences for upper and lower edges
    upper_gcds = calculate_gcd_differences(upper_edges)
    lower_gcds = calculate_gcd_differences(lower_edges)
    
    # Calculate the overall GCD of differences between upper and lower edges
    combined_gcds = calculate_overall_gcd(upper_gcds)
    combined_gcds = calculate_overall_gcd([combined_gcds] + lower_gcds)
    
    # Calculate the least common multiple of all GCDs to find the minimal key width
    min_key_width = 1
    for gcd_val in combined_gcds:
        min_key_width = lcm(min_key_width, gcd_val)
    
    # Calculate the total number of different keys needed
    total_keys = (W - sum(combined_gcds)) // min_key_width
    
    return total_keys

# Read input
W, L, N = map(int, input().split())
upper_edges = list(map(int, input().split()))
lower_edges = list(map(int, input().split()))

# Output the result
print(min_keys_to_open_locks(W, L, N, upper_edges, lower_edges))