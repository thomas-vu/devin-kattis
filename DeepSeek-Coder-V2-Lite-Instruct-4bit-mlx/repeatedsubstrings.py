def longest_repeated_substring(s):
    n = len(s)
    # Initialize the suffix array and lcp array
    sa = [i for i in range(n)]
    rank = [ord(s[i]) for i in range(n)]
    temp = [0] * n
    
    # Build the suffix array using radix sort
    def get_count(k):
        count = [0] * (max(n, 256) + 1)
        for i in range(n):
            count[rank[min(i + k, n - 1)]] += 1
        for j in range(1, max(n, 256) + 1):
            count[j] += count[j - 1]
        for i in range(n - 1, -1, -1):
            count[rank[min(i + k, n - 1)]] -= 1
            temp[count[rank[min(i + k, n - 1)]]] = i
        sa, temp = temp, sa
        return sa
    
    k = 1
    while True:
        sa = get_count(k)
        temp = [0] * n
        r = 0
        for i in range(1, n):
            if rank[sa[i]] != rank[sa[i - 1]] or rank[min(sa[i] + k, n - 1)] != rank[min(sa[i - 1] + k, n - 1)]:
                r += 1
            temp[sa[i]] = r
        rank, temp = temp, rank
        k *= 2
        if k >= n: break
    
    lcp = [0] * (n - 1)
    k = 0
    for i in range(n):
        if rank[i] == n - 1: continue
        j = sa[rank[i] + 1]
        while i + k < n and j + k < n and s[i + k] == s[j + k]:
            k += 1
        lcp[rank[i]] = k
        if k > 0: k -= 1
    
    max_len = 0
    idx = -1
    for i in range(n - 1):
        if lcp[i] > max_len:
            max_len = lcp[i]
            idx = sa[i]
        elif lcp[i] == max_len and sa[i] < idx:
            idx = sa[i]
    
    return s[idx:idx + max_len] if idx != -1 else ""

# Read input from stdin
import sys
input_string = sys.stdin.readline().strip()

# Output the result
print(longest_repeated_substring(input_string))