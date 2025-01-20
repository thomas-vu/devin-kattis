def longest_common_subsequence(strings):
    def count_chars(s):
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - ord('A')] += 1
        return cnt
    
    def min_count(cnts):
        min_cnt = [float('inf')] * 26
        for cnt in cnts:
            for i in range(26):
                min_cnt[i] = min(min_cnt[i], cnt[i])
        return min_cnt
    
    n = len(strings)
    cnts = [count_chars(s) for s in strings]
    min_cnt = min_count(cnts)
    
    result = 0
    for i in range(26):
        if min_cnt[i] == n:
            result += min_cnt[i]
    
    return result

# Read input
n, k = map(int, input().split())
strings = [input() for _ in range(n)]

# Compute and output the result
print(longest_common_subsequence(strings))