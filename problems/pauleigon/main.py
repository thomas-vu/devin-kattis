def determine_server(N, P, Q):
    total_rounds = (P + Q) // N
    if total_rounds % 2 == 0:
        return "paul"
    else:
        return "opponent"

# Read input
N, P, Q = map(int, input().split())
result = determine_server(N, P, Q)
print(result)