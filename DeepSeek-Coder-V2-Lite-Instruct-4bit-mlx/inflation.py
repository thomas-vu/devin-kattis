import sys

def read_ints():
    return list(map(int, input().split()))

n = int(input())
cannisters = read_ints()

if min(cannisters) == 0:
    print("impossible")
else:
    total_capacity = sum(cannisters)
    min_fraction = float('inf')
    
    for i in range(n):
        if cannisters[i] > 0:
            min_fraction = min(min_fraction, cannisters[i] / (i + 1))
    
    print("{:.6f}".format(min_fraction))