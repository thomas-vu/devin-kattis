import sys
from math import sqrt

def calculate_distance(x, y):
    return sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)

def main():
    N = int(sys.stdin.readline().strip())
    L, W = map(int, sys.stdin.readline().strip().split())
    trees_left = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
    
    min_distance = float('inf')
    
    for i in range(2**N):
        left_indices = [j for j in range(N) if (i & (1 << j))]
        right_indices = [j for j in range(N) if not (i & (1 << j))]
        
        left_positions = [trees_left[j] for j in left_indices]
        right_positions = [trees_left[j] for j in right_indices]
        
        left_positions.sort(key=lambda x: x[0])
        right_positions.sort(key=lambda x: x[0])
        
        if len(left_positions) == N // 2 and len(right_positions) == N // 2:
            min_distance = min(min_distance, sum(calculate_distance((left_positions[j], right_positions[j]), (trees_left[j][0], trees_left[j][1])) for j in range(N // 2)))
    
    print("{:.10f}".format(min_distance))

if __name__ == "__main__":
    main()