from collections import deque

def min_time_to_exit(w, h, building):
    fire_queue = deque()
    player_queue = deque()
    
    # Initialize fire and player positions
    for i in range(h):
        for j in range(w):
            if building[i][j] == '*':
                fire_queue.append((i, j))
            elif building[i][j] == '@':
                player_queue.append((i, j))
    
    # Directions for fire and player movements
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # Fire spread simulation
    while fire_queue:
        for _ in range(len(fire_queue)):
            x, y = fire_queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < h and 0 <= ny < w and building[nx][ny] == '.':
                    building[nx][ny] = '*'
                    fire_queue.append((nx, ny))
    
    # Player escape simulation
    visited = [[False] * w for _ in range(h)]
    time = 0
    
    while player_queue:
        for _ in range(len(player_queue)):
            x, y = player_queue.popleft()
            if x == 0 or x == h - 1 or y == 0 or y == w - 1:
                return time + 1
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and building[nx][ny] == '.':
                    visited[nx][ny] = True
                    player_queue.append((nx, ny))
        time += 1
    
    return "IMPOSSIBLE"

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        w = int(data[index])
        h = int(data[index + 1])
        index += 2
        building = []
        for i in range(h):
            building.append(list(data[index]))
            index += 1
        results.append(min_time_to_exit(w, h, building))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()