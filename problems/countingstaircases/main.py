def find_max_staircases(N, M, flags):
    from collections import defaultdict
    
    # Count the number of valid staircases that can be formed with each flag as the middle one
    def count_staircase(flags):
        n = len(flags)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            max_len = 0
            for j in range(i - M + 1, i):
                if j > 0 and flags[j] < flags[i]:
                    max_len = max(max_len, dp[j])
            dp[i] = max_len + 1
        return sum(dp) - n
    
    # Try all permutations to find the maximum number of staircases
    from itertools import permutations
    max_staircases = 0
    best_order = []
    
    for perm in permutations(flags):
        num_staircases = count_staircase([perm[i] for i in range(len(perm))])
        if num_staircases > max_staircases:
            max_staircases = num_staircases
            best_order = perm
    
    return max_staircases, [x for x in best_order]

# Read input
N, M = map(int, input().split())
flags = list(map(int, input().split()))

# Get the result
max_staircases, best_order = find_max_staircases(N, M, flags)

# Output the result
print(max_staircases)
print(' '.join(map(str, best_order)))