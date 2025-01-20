def solve(bags):
    bags.sort(reverse=True)
    dp = [[] for _ in range(len(bags))]
    
    for i in range(len(bags)):
        dp[i] = [bags[i]]
        for j in range(i):
            if bags[j] <= bags[i] and len(dp[j]) + 1 < len(dp[i]):
                dp[i] = dp[j] + [bags[i]]
    
    min_pieces, best_index = float('inf'), -1
    for i in range(len(bags)):
        if len(dp[i]) < min_pieces:
            min_pieces = len(dp[i])
            best_index = i
    
    return min_pieces, dp[best_index]

while True:
    n = int(input())
    if n == 0:
        break
    
    bags = list(map(int, input().split()))
    min_pieces, solution = solve(bags)
    
    print(min_pieces)
    for bag in solution:
        print(bag)
    print()