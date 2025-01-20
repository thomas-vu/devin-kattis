import math
from itertools import combinations

def min_distance(W, N, sacred_numbers):
    shrines = set()
    for num in range(1, N + 1):
        for sacred in sacred_numbers:
            if num % sacred == 0:
                shrines.add(num)
    
    min_dist = float('inf')
    for worker_set in combinations(shrines, W):
        max_distance = 0
        for shrine in worker_set:
            distance = min(abs(a - b) for a, b in zip(worker_set, worker_set[1:] + [worker_set[0]]))
            max_distance = max(max_distance, distance)
        min_dist = min(min_dist, max_distance)
    
    return min_dist * 2 * math.pi / N

def main():
    while True:
        input_line = list(map(int, input().split()))
        if input_line[0] == 0:
            break
        W, N, D = input_line[:3]
        sacred_numbers = input_line[3:]
        
        result = min_distance(W, N, sacred_numbers)
        print("{:.1f}".format(result))

if __name__ == "__main__":
    main()