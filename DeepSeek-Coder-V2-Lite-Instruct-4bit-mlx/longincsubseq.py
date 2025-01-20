def read_ints():
    return list(map(int, input().split()))

n = int(input())
seq = read_ints()

# Function to find the longest increasing subsequence and its indices
def lis(seq):
    n = len(seq)
    dp = [1] * n
    prev = [-1] * n
    
    for i in range(n):
        for j in range(i):
            if seq[j] < seq[i]:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j
    
    # Reconstruct the subsequence
    max_len = max(dp)
    index = dp.index(max_len)
    lis_seq = []
    
    while index != -1:
        lis_seq.append(index)
        index = prev[index]
    
    return max_len, lis_seq[::-1]

# Process each test case
for _ in range(n):
    length = int(input())
    sequence = read_ints()
    
    max_len, indices = lis(sequence)
    
    print(max_len)
    print(' '.join(map(str, indices)))