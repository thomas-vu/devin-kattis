def find_kth_letter(N, K):
    s1 = 'N'
    s2 = 'A'
    
    if N == 1:
        return s1[K - 1]
    elif N == 2:
        return s2[K - 1]
    
    prev_len = len(s1) + len(s2)
    while K > prev_len:
        s_new = s1 + s2
        s1, s2 = s2, s_new
        prev_len = len(s2)
    
    return s2[K - 1]

# Read input
N, K = map(int, input().split())

# Get the result and print it
result = find_kth_letter(N, K)
print(result)