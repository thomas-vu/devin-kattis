def main():
    n, m, p = map(int, input().split())
    
    # Initialize the lists to store which toys each child likes and toy categories
    children_likes = [list(map(int, input().split()))[1:] for _ in range(n)]
    toy_categories = [list(map(int, input().split())) for _ in range(p)]
    
    # Convert the toy categories into a usable form where each category is a bitmask
    cat_bitmasks = [0] * m
    for i, (l, r) in enumerate(toy_categories):
        bitmask = 0
        for toy in range(l, r + 1):
            bitmask |= (1 << (toy - 1))
        cat_bitmasks[i] = bitmask
    
    # Initialize the DP array where dp[state] represents the maximum number of children satisfied by the toys included in the state
    max_children = 0
    dp = [0] * (1 << m)
    
    # Iterate over each child's preferences and update the DP array accordingly
    for likes in children_likes:
        current_state = sum(1 << (toy - 1) for toy in likes)
        next_dp = dp.copy()
        
        # Try to include each toy category in the current state and update the DP array accordingly
        for cat_bitmask in cat_bitmasks:
            new_state = current_state | cat_bitmask
            next_dp[new_state] = max(next_dp[new_state], dp[current_state] + 1)
        
        # Update the DP array with the new state after trying all possible categories for this child's likes
        dp = next_dp
        max_children = max(max_children, dp[current_state])
    
    print(max_children)

if __name__ == "__main__":
    main()