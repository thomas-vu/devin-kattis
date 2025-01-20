def maximum_cost(n, m):
    # The total number of roads is n * (n - 1) / 2
    total_roads = n * (n - 1) // 2
    # To maximize the cost, we should select m roads from the total n*(n-1)/2 roads
    # The maximum cost is the sum of m largest distinct integers from 1 to total_roads
    max_cost = (total_roads - (total_roads - m)) * m
    return max_cost

# Read input from stdin
import sys
input = sys.stdin.read
data = input().split()
n = int(data[0])
m = int(data[1])

# Output the result
print(maximum_cost(n, m))