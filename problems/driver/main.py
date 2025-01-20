def min_cost_to_pass_gates(N, toll_fees, opening_times):
    # Initialize the minimum cost to reach each gate
    min_cost = [float('inf')] * N
    min_cost[0] = 0
    
    # Process each gate to find the minimum cost
    for i in range(N):
        if min_cost[i] != float('inf'):
            # Update the cost to reach adjacent gates
            if i + 1 < N:
                min_cost[i + 1] = min(min_cost[i + 1], min_cost[i] + toll_fees[i])
            if i - 1 >= 0:
                min_cost[i - 1] = min(min_cost[i - 1], min_cost[i] + toll_fees[i - 1])
    
    # The minimum cost to reach Gate N
    return min_cost[N - 1]

# Read input
import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
toll_fees = list(map(int, data[1].split()))
opening_times = list(map(int, data[2].split()))

# Calculate the minimum cost to pass through Gate N
result = min_cost_to_pass_gates(N, toll_fees, opening_times)
print(result)