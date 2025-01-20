import math

def min_completion_time(Q, M, S, L):
    # Calculate the time needed for each machine to handle a Q-second slot
    q_time = math.ceil(Q / float(M)) * M
    
    # Calculate the total time needed if we use only 1-second slots
    total_time = S + q_time * L
    
    # Since we can split the Q-second slots between machines, calculate the minimum time
    min_time = total_time
    
    # Check if it's possible to reduce the time by using more efficient allocation of Q-second slots
    for q_slots in range(L + 1):
        remaining_q = L - q_slots
        current_time = max(S + (Q * remaining_q), M * q_slots)
        min_time = min(min_time, current_time)
    
    return min_time

# Read input from stdin
Q, M, S, L = map(int, input().split())

# Output the result
print(min_completion_time(Q, M, S, L))