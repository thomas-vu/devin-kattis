def find_smallest_T(N, preferences):
    # Create a list to store the top T entries for each kid's preference list
    top_T_entries = [[] for _ in range(N)]
    
    # Populate the top_T_entries list with the appropriate entries from each kid's preference list
    for i in range(N):
        teacher = preferences[i][0]
        prefs = preferences[i][1:]
        for j in range(len(prefs)):
            top_T_entries[prefs[j] - 1].append((i, j + 1))
    
    # Find the minimum T such that no kid has a classmate with the same teacher as before
    min_T = float('inf')
    for t in range(N):
        # Create a list to store the top T entries for each kid's preference list at step t
        current_top_T = [[] for _ in range(N)]
        
        # Populate the current_top_T list with the appropriate entries from each kid's preference list at step t
        for i in range(N):
            teacher = preferences[i][0]
            prefs = preferences[i][1:]
            for j in range(len(prefs)):
                if prefs[j] - 1 <= t:
                    current_top_T[i].append((i, j + 1))
        
        # Check if the partitioning is valid for this step t
        valid = True
        for i in range(N):
            if preferences[i][0] == teacher:
                valid = False
                break
        
        # If the partitioning is valid, update min_T with t + 1 (since we start counting from 0)
        if valid:
            min_T = t + 1
    
    return min_T

# Read input
N = int(input())
preferences = [list(map(int, input().split())) for _ in range(N)]

# Find and print the smallest T
print(find_smallest_T(N, preferences))