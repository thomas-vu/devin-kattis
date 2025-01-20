import sys

# Read the size of the grid
N = int(input())

# Initialize the grid with unknown configurations
grid = [['?' for _ in range(N)] for _ in range(N)]

# Function to perform an experiment and read the result
def perform_experiment():
    # Print the grid configuration to the grader
    for row in grid:
        print(''.join(row))
    sys.stdout.flush()
    
    # Read the number of lit squares from the grader
    result = int(input())
    return result

# Main logic to determine the minimum number of lamps needed
def solve():
    # First experiment: turn on all vertical and horizontal lamps
    for i in range(N):
        grid[i][i] = 'V' if i % 2 == 0 else 'H'
    
    first_result = perform_experiment()
    
    # Second experiment: toggle some lamps to see if we can reduce the number of lit squares
    for i in range(N):
        for j in range(N):
            if grid[i][j] == '?':
                grid[i][j] = 'V' if i % 2 == 0 else 'H'
    
    second_result = perform_experiment()
    
    # If the number of lit squares didn't change significantly, we can assume a pattern
    if second_result == first_result:
        for i in range(N):
            for j in range(N):
                if grid[i][j] == '?':
                    grid[i][j] = 'V' if i % 2 == 0 else 'H'
        perform_experiment()
    else:
        # Adjust the grid based on the results of the experiments
        for i in range(N):
            for j in range(N):
                if grid[i][j] == '?':
                    grid[i][j] = 'V' if i % 2 == 0 else 'H'
        perform_experiment()
    
    # Output the final configuration of lamps
    print('!')
    for row in grid:
        print(''.join(['1' if x == 'V' else '0' for x in row]))
    sys.stdout.flush()

# Call the solve function to find the solution
solve()