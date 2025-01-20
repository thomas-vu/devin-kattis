def can_move_cows(m, l, M, L, tm, tl):
    # Calculate the time required for each cow to reach their new positions
    time_monica = abs(M - m)
    time_lydia = abs(L - l)
    
    # Check if both cows can reach their new positions before their meal times
    return "possible" if time_monica <= tm and time_lydia <= tl else "impossible"

# Read input
m, l = map(int, input().split())
M, L = map(int, input().split())
tm, tl = map(int, input().split())

# Output the result
print(can_move_cows(m, l, M, L, tm, tl))