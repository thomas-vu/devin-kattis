def min_moves_to_destroy_city(T, test_cases):
    results = []
    for case in test_cases:
        N, D = case[0]
        H = case[1]
        E = case[2]
        
        # Calculate the health of each building after explosion from adjacent buildings
        for i in range(N):
            if i > 0:
                H[i] = max(H[i] - E[i-1], 0)
            if i < N - 1:
                H[i] = max(H[i] - E[i+1], 0)
        
        # Count the number of moves needed to destroy each building
        moves = 0
        for health in H:
            if health > 0:
                moves += (health + D - 1) // D
        
        results.append(moves)
    return results

# Read input from stdin for the number of test cases and each test case's details
T = int(input().strip())
test_cases = []
for _ in range(T):
    N, D = map(int, input().strip().split())
    H = list(map(int, input().strip().split()))
    E = list(map(int, input().strip().split()))
    test_cases.append((N, D, H, E))

# Get the results for each test case and print them
results = min_moves_to_destroy_city(T, test_cases)
for result in results:
    print(result)