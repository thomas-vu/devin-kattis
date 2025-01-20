def count_winning_instances(board):
    n = len(board)
    winning_count = 0
    
    for start in range(n):
        visited = [False] * n
        position = start
        while True:
            value = board[position]
            visited[position] = True
            
            if value == 0:
                break
            
            if value > 0:
                position += value
            else:
                position -= abs(value)
            
            if position < 0 or position >= n:
                break
            
            if visited[position]:
                # Cycle detected
                break
            
            if board[position] == m:
                winning_count += 1
                break
    
    return winning_count

# Read input
n = int(input())
board = list(map(int, input().split()))
m = board[0]  # The first number on the board is the magic number

# Count winning instances
winning_instances = count_winning_instances(board)
print(winning_instances)