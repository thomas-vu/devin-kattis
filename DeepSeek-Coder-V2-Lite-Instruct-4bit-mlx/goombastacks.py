def can_mario_escape(N, rooms):
    current_goombas = 0
    for i in range(N):
        goombas, button_threshold = rooms[i]
        current_goombas += goombas
        if current_goombas < button_threshold:
            return "impossible"
    return "possible"

# Read input
N = int(input())
rooms = [tuple(map(int, input().split())) for _ in range(N)]

# Determine if Mario can escape
result = can_mario_escape(N, rooms)
print(result)