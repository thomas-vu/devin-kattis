def maximum_speed(N, L, positions):
    low = 0.1
    high = 10.0
    
    while high - low > 1e-9:
        mid = (low + high) / 2.0
        
        max_gap = float('-inf')
        for i in range(N):
            for j in range(i+1, N):
                gap = (positions[j] - positions[i]) / mid
                if gap > max_gap:
                    max_gap = gap
        
        if max_gap >= L:
            high = mid
        else:
            low = mid
    
    return (low + high) / 2.0 if high - low <= 1e-9 else "no fika"

# Read input
import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
L = int(data[1])
positions = [float(x) for x in data[2:]]

# Get the result and print it
result = maximum_speed(N, L, positions)
print("{:.9f}".format(result))