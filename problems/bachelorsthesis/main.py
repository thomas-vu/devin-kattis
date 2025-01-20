def count_inversions(a):
    return sum([1 for i in range(len(a)) for j in range(i+1, len(a)) if a[i] > a[j]])

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    min_inversions = float('inf')
    best_sequence = None
    
    for mask in range(1 << n):
        if bin(mask).count('1') == k:
            subsequence = [a[i] for i in range(n) if mask & (1 << i)]
            new_a = a[:]
            for x in reversed(subsequence):
                new_a.remove(x)
            new_a = subsequence[::-1] + new_a
            inversions = count_inversions(new_a)
            if inversions < min_inversions:
                min_inversions = inversions
                best_sequence = mask
    
    sequences = []
    for i in range(n):
        if best_sequence & (1 << i):
            sequences.append('1')
        else:
            sequences.append('0')
    
    print(min_inversions)
    l = bin(best_sequence).count('1')
    print(l)
    for sequence in sequences:
        print(sequence * n)

solve()