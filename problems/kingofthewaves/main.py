def can_henk_win(n, win_matrix):
    # Check if Henk (0) can win by trying all possible sequences
    def dfs(node, visited):
        if node == 0:
            return True
        for neighbor in range(n):
            if win_matrix[node][neighbor] == '1' and neighbor not in visited:
                visited.add(neighbor)
                if dfs(neighbor, visited):
                    return True
        return False
    
    # Try to start the tournament with each participant and check if Henk can win
    for start in range(n):
        visited = set()
        if dfs(start, visited):
            sequence = []
            current = start
            while current != 0:
                for next_node in range(n):
                    if win_matrix[current][next_node] == '1':
                        sequence.append(next_node)
                        current = next_node
                        break
            return sequence
    return "impossible"

# Main function to read input and output the result
def main():
    n = int(input().strip())
    win_matrix = [input().strip() for _ in range(n)]
    result = can_henk_win(n, win_matrix)
    if result == "impossible":
        print("impossible")
    else:
        sequence = [0] + result
        print(' '.join(map(str, sequence)))

# Run the main function
if __name__ == "__main__":
    main()