def optimal_path_length(steps, directions):
    # Create a dictionary to count the occurrences of each direction
    dir_count = {'N': 0, 'E': 0, 'S': 0, 'W': 0}
    
    # Count the occurrences of each direction in the given path
    for dir in directions:
        dir_count[dir] += 1
    
    # Calculate the optimal path length based on the rules provided
    horizontal = abs(dir_count['E'] - dir_count['W'])
    vertical = abs(dir_count['N'] - dir_count['S'])
    
    # The optimal path length is the sum of horizontal and vertical steps taken
    return horizontal + vertical

def main():
    n = int(input())  # Read the number of paths
    input()  # Skip the blank line after the number of paths
    
    for _ in range(n):
        s = int(input())  # Read the number of steps for this path
        
        # Read the directions for this path and store them in a list
        directions = [input().strip() for _ in range(s)]
        
        # Calculate and print the optimal path length for this path
        print(optimal_path_length(s, directions))
        
        # Skip the blank line after each path description if it's not the last one
        if _ < n - 1:
            input()  # Skip the blank line after each path description

if __name__ == "__main__":
    main()