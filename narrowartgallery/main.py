def solve(N, K, gallery):
    # dp[floor][closed][side] represents max value when:
    # - considering floors 0 to floor
    # - having closed 'closed' rooms
    # - with last closure on 'side' (-1: none, 0: left, 1: right)
    dp = {}
    
    def get_value(floor, closed, side):
        if closed > K:
            return float('-inf')
        if floor == N:
            return 0 if closed == K else float('-inf')
        
        key = (floor, closed, side)
        if key in dp:
            return dp[key]
        
        left, right = gallery[floor]
        max_value = float('-inf')
        
        # Don't close any room on this floor
        max_value = max(max_value, left + right + get_value(floor + 1, closed, -1))
        
        # Close left room if possible
        if side in [-1, 0]:
            max_value = max(max_value, right + get_value(floor + 1, closed + 1, 0))
            
        # Close right room if possible
        if side in [-1, 1]:
            max_value = max(max_value, left + get_value(floor + 1, closed + 1, 1))
            
        dp[key] = max_value
        return max_value

    result = get_value(0, 0, -1)
    return result

while True:
    N, K = map(int, input().split())
    if N == 0 and K == 0:
        break
        
    gallery = []
    total = 0
    for _ in range(N):
        left, right = map(int, input().split())
        gallery.append((left, right))
        total += left + right
        
    print(solve(N, K, gallery))
