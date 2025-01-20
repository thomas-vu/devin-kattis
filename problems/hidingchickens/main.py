import itertools
from math import sqrt

def distance(p1, p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def min_distance(roost, spots):
    min_dist = float('inf')
    for combo in itertools.permutations(spots, len(spots)):
        dist = 0
        for i in range(len(combo) - 1):
            dist += distance(combo[i], combo[i+1])
        dist += distance(roost, combo[0]) + distance(roost, combo[-1])
        min_dist = min(min_dist, dist)
    return min_dist

def main():
    roost = list(map(float, input().split()))
    N = int(input())
    spots = [list(map(float, input().split())) for _ in range(N)]
    result = min_distance(roost, spots)
    print("{:.6f}".format(result))

if __name__ == "__main__":
    main()