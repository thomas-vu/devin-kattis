def count_ways(A, B, x):
    freq_a = {}
    for a in A:
        if (x - a) in freq_a:
            freq_a[x - a] += 1
        else:
            freq_a[x - a] = 1
    
    count = 0
    for b in B:
        if b in freq_a and freq_a[b] > 0:
            count += freq_a[b]
    return count

n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
q = int(input())
for _ in range(q):
    x = int(input())
    print(count_ways(A, B, x))