def min_voters_to_win(states):
    total_delegates = 0
    min_persuadable = 0
    
    for state in states:
        D, C, F, U = state
        total_delegates += D
        if C == F:
            min_persuadable += (U + 1) // 2 + 1
        elif C > F:
            min_persuadable += (U + 1) // 2 + 1 if U % 2 == 0 else (U + 1) // 2
        else:
            min_persuadable += U + 1
    
    if min_persuadable > total_delegates:
        return "impossible"
    else:
        return min_persuadable

# Read number of states
S = int(input())
states = [tuple(map(int, input().split())) for _ in range(S)]

# Output the result
print(min_voters_to_win(states))