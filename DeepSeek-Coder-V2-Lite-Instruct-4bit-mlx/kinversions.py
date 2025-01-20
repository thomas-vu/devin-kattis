def count_inversions(s):
    n = len(s)
    inversions = [0] * (n - 1)
    
    for k in range(1, n):
        count = 0
        for i in range(n - k):
            if s[i] == 'B' and s[i + k] == 'A':
                count += 1
        inversions[k - 1] = count
    
    return inversions

s = input().strip()
inversions = count_inversions(s)
for inv in inversions:
    print(inv)