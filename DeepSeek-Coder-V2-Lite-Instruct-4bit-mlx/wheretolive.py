import sys
from typing import List, Tuple

def min_average_squared_distance(locations: List[Tuple[int, int]]) -> Tuple[int, int]:
    min_x = min(loc[0] for loc in locations)
    max_x = max(loc[0] for loc in locations)
    min_y = min(loc[1] for loc in locations)
    max_y = max(loc[1] for loc in locations)
    
    best_x, best_y = min_x, min_y
    min_total_distance = float('inf')
    
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            total_distance = sum((x - loc[0])**2 + (y - loc[1])**2 for loc in locations)
            if total_distance < min_total_distance:
                min_total_distance = total_distance
                best_x, best_y = x, y
    
    return best_x, best_y

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        locations = [tuple(map(int, input().split())) for _ in range(n)]
        x, y = min_average_squared_distance(locations)
        print(x, y)

if __name__ == "__main__":
    main()