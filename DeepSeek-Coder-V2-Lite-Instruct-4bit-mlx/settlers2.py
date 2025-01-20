def resource_for_tile(n):
    board = [0] * (4 * n + 1)
    counts = {i: 0 for i in range(1, 6)}
    
    def get_neighboring_resources(index):
        neighbors = set()
        while index < len(board) and board[index] != 0:
            neighbors.add(board[index])
            index += 1
        return neighbors
    
    def next_resource(index):
        for i in range(1, 6):
            if i not in get_neighboring_resources(index):
                return i
        for i in range(1, 6):
            if counts[i] == min([counts[j] for j in range(1, 6) if j not in get_neighboring_resources(index)]):
                return i
        for i in range(1, 6):
            if i not in get_neighboring_resources(index):
                return i
    
    index = 0
    while n > 0:
        board[index] = next_resource(index)
        counts[board[index]] += 1
        n -= 1
        index += 1
    
    return board[index - 1]

c = int(input())
for _ in range(c):
    n = int(input())
    print(resource_for_tile(n))