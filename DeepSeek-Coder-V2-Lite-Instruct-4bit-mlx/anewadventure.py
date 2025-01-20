from collections import deque

def min_time_to_reach(C, A, board):
    # Directions for moving in the circular grid
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # Initialize the queue with Gon's starting position and time 0
    queue = deque([(0, 0)])
    
    # Create a visited set to keep track of visited states
    visited = set()
    visited.add((0, 0))
    
    # Perform BFS to find the minimum time to reach the Examination Hall
    while queue:
        x, y = queue.popleft()
        
        # Check if Gon has reached the Examination Hall
        if (x, y) == (C-1, -1):
            return x
        
        # Check all adjacent positions
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # Ensure the new position is within bounds
            if 0 <= nx < C and -1 <= ny < A:
                # Check the state of the new position
                if board[nx][ny] == 'G':
                    continue  # Gon's position, skip it
                elif board[nx][ny] == 'M':
                    continue  # Motorbike's position, skip it
                
                # Mark the new position as visited and add to the queue
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny))
    
    # If the Examination Hall is unreachable
    return -1

# Read input
C, A = map(int, input().split())
board = [input() for _ in range(C)]

# Output the result
print(min_time_to_reach(C, A, board))