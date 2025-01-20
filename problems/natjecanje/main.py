def min_teams_cannot_start(N, S, R, damaged, reserve):
    # Create a set of all teams with reserve kayaks for easy lookup
    reserve_set = set(reserve)
    
    # Create a list to mark teams that can start the race
    can_start = [1] * N  # Initially, all teams can start (marked as 1)
    
    # Mark damaged teams that cannot start the race
    for team in damaged:
        can_start[team - 1] = 0
    
    # Mark teams that have reserve kayaks and can start the race
    for team in reserve:
        if can_start[team - 1] == 1:
            # Check if the adjacent teams can borrow a kayak
            if team - 1 > 0 and can_start[team - 2] == 0:
                can_start[team - 2] = 1
            if team < N and can_start[team] == 0:
                can_start[team] = 1
    
    # Count the number of teams that cannot start the race
    return can_start.count(0)

# Read input
N, S, R = map(int, input().split())
damaged = list(map(int, input().split()))
reserve = list(map(int, input().split()))

# Calculate the result and print it
result = min_teams_cannot_start(N, S, R, damaged, reserve)
print(result)