def can_drink_all_potions(N, T, durations):
    total_time = sum(durations) + (N - 1) * T
    return "YES" if total_time <= 24 * 60 else "NO"

# Read input from stdin
import sys
input = sys.stdin.read
data = input().split()
N, T = int(data[0]), int(data[1])
durations = [int(data[i + 2]) for i in range(N)]

# Check if it's possible to drink all potions at the same time
result = can_drink_all_potions(N, T, durations)
print(result)