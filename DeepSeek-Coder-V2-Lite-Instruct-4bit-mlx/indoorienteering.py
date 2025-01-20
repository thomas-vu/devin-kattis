def check_race(n, L, distances):
    from itertools import permutations
    
    # Check all possible permutations of control points
    for perm in permutations(range(n)):
        total_distance = 0
        # Calculate the distance for this permutation
        for i in range(n - 1):
            total_distance += distances[perm[i]][perm[i + 1]]
        total_distance += distances[perm[-1]][perm[0]]
        
        # Check if the total distance matches the desired length L
        if total_distance == L:
            return "possible"
    return "impossible"

# Read input
n, L = map(int, input().split())
distances = [list(map(int, input().split())) for _ in range(n)]

# Output the result
print(check_race(n, L, distances))