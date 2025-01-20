def find_route(pieces):
    stations = {}
    for piece in pieces:
        station, connections = piece.split(' ', 1)
        connections = connections.split()
        stations[station] = connections
        for conn in connections:
            if conn not in stations:
                stations[conn] = []
            if station not in stations[conn]:
                stations[conn].append(station)
    
    start, end = next((line.split() for line in pieces if ' ' in line), ['', ''])[0], next((line.split() for line in pieces if ' ' in line), ['', ''])[1]
    
    visited = set()
    path = []
    def dfs(current):
        if current == end:
            path.append(current)
            return True
        if current in visited:
            return False
        visited.add(current)
        path.append(current)
        for neighbor in stations[current]:
            if dfs(neighbor):
                return True
        path.pop()
        visited.remove(current)
        return False
    
    if dfs(start):
        return ' '.join(path)
    else:
        return "no route found"

# Read input and call the function
import sys
input = sys.stdin.read
pieces = input().splitlines()
print(find_route(pieces))