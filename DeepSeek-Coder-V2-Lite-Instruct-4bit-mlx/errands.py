import sys
from itertools import permutations

def distance(loc1, loc2):
    x1, y1 = map(float, loc1.split())
    x2, y2 = map(float, loc2.split())
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

def total_distance(order, locations):
    start = 'work'
    dist = 0
    for stop in order:
        if start == 'work':
            dist += distance(start, locations[stop])
        else:
            dist += distance(locations[start], locations[stop])
        start = stop
    if start == 'work':
        dist += distance(start, locations[order[-1]])
    else:
        dist += distance(locations[start], locations['work'])
    return dist

def main():
    while True:
        try:
            n = int(sys.stdin.readline().strip())
            locations = {}
            for _ in range(n):
                loc_name, x, y = sys.stdin.readline().strip().split()
                locations[loc_name] = f"{x} {y}"
            
            trips = []
            while True:
                trip = sys.stdin.readline().strip()
                if not trip:
                    break
                trips.append(trip.split())
            
            best_order = None
            min_distance = float('inf')
            for order in permutations(trips[0]):
                dist = total_distance(order, locations)
                if dist < min_distance:
                    min_distance = dist
                    best_order = order
            
            print(' '.join(best_order))
        except EOFError:
            break

if __name__ == "__main__":
    main()