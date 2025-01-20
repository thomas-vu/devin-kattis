def minimum_trauma_rating(N, K, L, quests):
    # Sort quests by the number of levels gained in ascending order
    quests.sort(key=lambda x: (x[0], -x[1]))
    
    # Initialize the minimum trauma rating to a large number
    min_trauma = float('inf')
    
    # Iterate through all possible combinations of quests to determine the minimum trauma rating
    for mask in range(1 << N):
        count = 0
        trauma_sum = 0
        levels_gained = 0
        
        # Calculate the total levels gained and trauma sum for the current combination of quests
        for i in range(N):
            if mask & (1 << i):
                count += 1
                levels_gained += quests[i][1]
                trauma_sum += quests[i][2]
        
        # Check if the current combination of quests can help Edgar reach level L
        if levels_gained >= L:
            # If the number of quests taken is greater than or equal to K, update min_trauma
            if count >= K:
                min_trauma = min(min_trauma, trauma_sum)
            else:
                # If less than K quests are taken, calculate the sum of the largest K trauma values
                if count > 0:
                    trauma_values = [quests[j][2] for j in range(N) if mask & (1 << j)]
                    trauma_values.sort(reverse=True)
                    min_trauma = min(min_trauma, sum(trauma_values[:K]))
    
    return min_trauma

# Read input
N, K, L = map(int, input().split())
quests = [list(map(int, input().split())) for _ in range(N)]

# Output the minimum trauma rating
print(minimum_trauma_rating(N, K, L, quests))