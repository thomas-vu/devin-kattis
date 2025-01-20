import math
from heapq import heappush, heappop

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def time_to_reach(x, y):
    return 2 + distance(0, 0, x, y) / 5.0

def main():
    x1, y1 = map(float, input().split())
    x2, y2 = map(float, input().split())
    n = int(input())
    
    cannons = [tuple(map(float, input().split())) for _ in range(n)]
    
    start = (x1, y1)
    end = (x2, y2)
    
    heap = [(time_to_reach(x1 - x2, y1 - y2), start)]
    visited = set(start)
    
    while heap:
        time_so_far, (x, y) = heappop(heap)
        
        if (x, y) == end:
            print("{:.5f}".format(time_so_far))
            return
        
        for cx, cy in cannons:
            if (cx, cy) not in visited:
                dist = distance(x, y, cx, cy)
                if dist <= 50:
                    heappush(heap, (time_so_far + 2 + dist / 5.0, (cx, cy)))
                    visited.add((cx, cy))
    
    print("{:.5f}".format(time_to_reach(x2 - x1, y2 - y1)))

if __name__ == "__main__":
    main()