MOD = 1000000007

def count_inversions(s):
    n = len(s)
    zeros = s.count('0')
    ones = s.count('1')
    qs = s.count('?')
    
    # Calculate the number of inversions for each sequence
    total_inversions = 0
    
    # Calculate the number of inversions for each sequence where '?' is replaced by '0'
    current_zeros = 0
    for i in range(n):
        if s[i] == '0' or s[i] == '?':
            total_inversions += (ones - current_zeros)
        if s[i] == '0':
            current_zeros += 1
    
    # Calculate the number of inversions for each sequence where '?' is replaced by '1'
    current_zeros = 0
    for i in range(n):
        if s[i] == '1' or s[i] == '?':
            total_inversions += (zeros - current_zeros)
        if s[i] == '1':
            current_zeros += 1
    
    # Adjust for the number of sequences
    total_inversions *= pow(2, qs, MOD)
    
    return total_inversions % MOD

# Read input
s = input().strip()

# Output the result
print(count_inversions(s))