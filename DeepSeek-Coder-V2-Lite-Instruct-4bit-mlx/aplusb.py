from collections import defaultdict
import sys
input = sys.stdin.readline

def count_ways(N, a):
    freq = defaultdict(int)
    for num in a:
        freq[num] += 1
    
    ways = 0
    for i in range(N):
        for j in range(i + 1, N):
            target = a[i] + a[j]
            if freq[target] > 0:
                ways += 1
    return ways

N = int(input())
a = list(map(int, input().split()))
print(count_ways(N, a))