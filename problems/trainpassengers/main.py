def is_possible(C, n, measurements):
    current_passengers = 0
    for i in range(n):
        left, entered, waited = measurements[i]
        current_passengers -= left
        if current_passengers < 0 or current_passengers > C:
            return "impossible"
        current_passengers += entered
        if current_passengers > C:
            return "impossible"
    return "possible" if current_passengers == 0 else "impossible"

# Read input
C, n = map(int, input().split())
measurements = [list(map(int, input().split())) for _ in range(n)]

# Check consistency
result = is_possible(C, n, measurements)
print(result)