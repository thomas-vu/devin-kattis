def is_possible(n, m, maps):
    # Create a list to track the possible assignments for each location
    possible_traps = [set() for _ in range(m + 1)]
    
    # Process each map's claims
    for m1, m2 in maps:
        if m1 > 0:
            possible_traps[m1].add(True)  # m1 contains treasure
        else:
            possible_traps[abs(m1)].add(False)  # m1 contains trap
        
        if m2 > 0:
            possible_traps[m2].add(True)  # m2 contains treasure
        else:
            possible_traps[abs(m2)].add(False)  # m2 contains trap
    
    # Check if it's possible to assign treasures and traps such that all maps are reasonable
    for i in range(1, m + 1):
        if len(possible_traps[i]) == 2:
            return "NO"
    return "YES"

# Read input
n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

# Check if it's possible and print the result
print(is_possible(n, m, maps))