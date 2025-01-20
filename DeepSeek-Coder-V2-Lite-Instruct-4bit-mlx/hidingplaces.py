def knight_moves(start, board):
    moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
    queue = [(start, 0)]
    visited = set()
    visited.add(start)
    
    while queue:
        (x, y), dist = queue.pop(0)
        
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 8 and 0 <= ny < 8 and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), dist + 1))
    
    hiding_places = []
    max_dist = dist
    for i in range(8):
        for j in range(8):
            if board[i][j] == 0 and ((i, j) not in visited):
                hiding_places.append((i, j))
    
    return max_dist, sorted(hiding_places)

def main():
    n = int(input().strip())
    for _ in range(n):
        start = input().strip()
        x, y = ord(start[0]) - ord('a'), int(start[1]) - 1
        board = [[0] * 8 for _ in range(8)]
        board[x][y] = 1
        max_dist, hiding_places = knight_moves((x, y), board)
        print(max_dist, end=' ')
        for place in hiding_places:
            print(chr(place[0] + ord('a')) + str(place[1] + 1), end=' ')
        print()

if __name__ == "__main__":
    main()