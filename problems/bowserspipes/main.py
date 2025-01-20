def find_coin_rooms(F, D):
    n = len(F)
    coin_rooms = [-1] * n
    
    # First, identify all the coin rooms.
    for i in range(n):
        if F[i] == -1:
            coin_rooms[i] = i
    
    # Now, use a depth-first search to propagate the coin room information.
    for i in range(n):
        if F[i] != -1:
            continue
        visited = set()
        while F[i] not in visited and F[i] != -1:
            visited.add(F[i])
            i = F[i]
        if F[i] == -1:
            coin_rooms[i] = i
    
    # Create a map from each pipe to the coin room it leads to.
    pipe_to_coin = {}
    for i in range(n):
        if F[i] != -1:
            pipe_to_coin[i] = coin_rooms[F[i]]
    
    # For each pipe Luigi enters, find the corresponding pipe Mario should enter.
    result = []
    for d in D:
        while F[d] != -1 and pipe_to_coin[d] == -1:
            d = F[d]
        result.append(d)
    
    return result

# Read input
N = int(input())
F = list(map(int, input().split()))
A = int(input())
D = list(map(int, input().split()))

# Solve the problem and output the result
result = find_coin_rooms(F, D)
for r in result:
    print(r)