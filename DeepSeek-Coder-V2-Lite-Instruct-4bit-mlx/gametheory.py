def solve(n, p, a):
    # Create a list to store the final score for each starting cell
    result = []
    
    # Iterate over each possible starting position for SoCCat's token
    for s in range(n):
        # Initialize the score and position of the token
        score = 0
        pos = s
        
        # Play the game optimally for this starting position
        while pos <= n:
            score += a[pos - 1]
            pos += p[pos - 1]
        
        # Append the final score for this starting position to the result list
        result.append(score)
    
    return result

# Read the number of test cases from input
C = int(input())
for _ in range(C):
    # Read the number of cells and the positions on the cells for the current test case
    n = int(input())
    p = list(map(int, input().split()))
    
    # Read the array a for the current test case
    a = list(map(int, input().split()))
    
    # Solve the problem for the current test case and print the result
    solution = solve(n, p, a)
    print(' '.join(map(str, solution)))