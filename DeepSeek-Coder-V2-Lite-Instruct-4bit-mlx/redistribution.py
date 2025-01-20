def is_safe_order(rooms):
    n = len(rooms)
    total_exams = sum(rooms)
    visited = [False] * n
    order = []
    
    def dfs(room_index):
        if visited[room_index]:
            return False
        visited[room_index] = True
        order.append(room_index)
        
        # Calculate the number of exams in the pile after visiting this room
        pile = total_exams - sum(visited)
        
        # Check if the number of exams in the pile is enough for the next room
        next_room = (room_index + 1) % n
        while not visited[next_room]:
            if pile < rooms[next_room]:
                return False
            pile -= rooms[next_room]
            next_room = (next_room + 1) % n
        
        # Recur for the next room if it's safe to do so
        return dfs(next_room)
    
    # Start DFS from the first room
    if dfs(0):
        return order
    else:
        return "impossible"

# Read input
n = int(input().strip())
rooms = list(map(int, input().strip().split()))

# Get the safe order or determine if it's impossible
result = is_safe_order(rooms)
print(result)