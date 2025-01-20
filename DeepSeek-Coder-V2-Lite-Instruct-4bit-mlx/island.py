def find_islands(map):
    islands = []
    visited = set()
    
    def dfs(x, y):
        if (x, y) in visited:
            return
        visited.add((x, y))
        if map[y][x] == 'X' or map[y][x] == 'B':
            return
        islands[-1].append((x, y))
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(map[0]) and 0 <= ny < len(map):
                dfs(nx, ny)
    
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == '#' and (x, y) not in visited:
                islands.append([])
                dfs(x, y)
    
    return islands

def count_bridges(map):
    bridges = 0
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == 'B':
                # Check horizontally
                if x + 1 < len(map[0]) and map[y][x + 1] == 'B':
                    bridges += 1
                # Check vertically
                if y + 1 < len(map) and map[y + 1][x] == 'B':
                    bridges += 1
    return bridges // 2

def main():
    import sys
    input = sys.stdin.read
    data = input().split('\n\n')
    
    map_number = 0
    for i, map in enumerate(data):
        if not map:
            continue
        map_number += 1
        lines = map.split('\n')
        grid = [list(line) for line in lines]
        
        islands = find_islands(grid)
        bridges = count_bridges(grid)
        
        island_count = len(islands)
        bus_count = max(1, min(island_count - 1, bridges))
        
        print("Map", map_number)
        print("islands:", island_count)
        print("bridges:", bridges)
        print("buses needed:", bus_count)
        if i < len(data) - 1 and data[i + 1]:
            print()

if __name__ == "__main__":
    main()