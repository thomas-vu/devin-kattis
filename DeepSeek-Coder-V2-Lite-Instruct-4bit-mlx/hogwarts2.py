def can_reach_dormitory(n, senior_config, student_config):
    def dfs(room, path):
        if room == n:
            return True
        for i in range(4):
            next_room = student_config[room - 1][i]
            if next_room != 0 and (room, i) not in visited:
                visited.add((room, i))
                if dfs(next_room, path + [i]):
                    return True
        return False
    
    def check_reachable(start, end):
        if start == end:
            return True
        for i in range(4):
            next_room = senior_config[start - 1][i]
            if next_room != 0 and check_reachable(next_room, end):
                return True
        return False
    
    visited = set()
    if not check_reachable(1, n):
        return "Impossible"
    
    if dfs(1, []):
        return "Yes"
    else:
        return "No"

# Read input from stdin
n = int(input().strip())
senior_config = [list(map(int, input().strip().split())) for _ in range(n)]
student_config = [list(map(int, input().strip().split())) for _ in range(n)]

# Output the result
print(can_reach_dormitory(n, senior_config, student_config))