def count_handshakes(R, S, seating):
    def is_valid(x, y):
        return 0 <= x < R and 0 <= y < S
    
    def count_handshakes_from(x, y):
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        count = 0
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny) and seating[nx][ny] == 'o':
                count += 1
        return count
    
    total_handshakes = 0
    for i in range(R):
        for j in range(S):
            if seating[i][j] == 'o':
                total_handshakes += count_handshakes_from(i, j)
    return total_handshakes // 2

R, S = map(int, input().split())
seating = [input() for _ in range(R)]
print(count_handshakes(R, S, seating))