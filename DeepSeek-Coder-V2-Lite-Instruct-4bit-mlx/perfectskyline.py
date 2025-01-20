def can_build_skyline(blocks, buildings):
    n = len(blocks)
    s = len(buildings)
    
    # DP to check if we can build a skyline with the given blocks
    dp = [[False] * (sum(buildings) + 1) for _ in range(n + 1)]
    dp[0][0] = True
    
    # Prefix sums to speed up the DP
    prefix_sums = [[0] * (sum(buildings) + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(sum(buildings) + 1):
            prefix_sums[i][j] = prefix_sums[i - 1][j] + (blocks[i - 1] if dp[i - 1][j] else 0)
            if j >= blocks[i - 1]:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - blocks[i - 1]]
    
    # Reconstruct the solution if possible
    result = []
    for i in range(1, s + 1):
        found = False
        for j in range(sum(buildings) + 1):
            if dp[n][j] and j == buildings[i - 1]:
                found = True
                used_blocks = []
                current_height = j
                remain_blocks = n
                while remain_blocks > 0:
                    if dp[remain_blocks - 1][current_height]:
                        remain_blocks -= 1
                    else:
                        used_blocks.append(remain_blocks)
                        current_height -= blocks[remain_blocks - 1]
                        remain_blocks -= 1
                result.append((i, used_blocks))
                break
        if not found:
            return -1
    for r in result:
        print(r[0], len(r[1]))
        for b in r[1]:
            print(b, end=' ')
        print()
    return 0

# Read input
N, S = map(int, input().split())
blocks = list(map(int, input().split()))
buildings = list(map(int, input().split()))

# Solve the problem
can_build_skyline(blocks, buildings)