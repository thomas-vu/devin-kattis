def find_optimal_seat(N, people, K, seats):
    min_max_distance = float('inf')
    optimal_seat = (float('inf'), float('inf'))
    
    for seat in seats:
        max_distance = 0
        for person in people:
            distance = abs(seat[0] - person[0]) + abs(seat[1] - person[1])
            if distance > max_distance:
                max_distance = distance
        if max_distance < min_max_distance or (max_distance == min_max_distance and seat < optimal_seat):
            min_max_distance = max_distance
            optimal_seat = seat
    
    return optimal_seat

# Read input
N = int(input())
people = [tuple(map(int, input().split())) for _ in range(N)]
K = int(input())
seats = [tuple(map(int, input().split())) for _ in range(K)]

# Find and print the optimal seat
optimal_seat = find_optimal_seat(N, people, K, seats)
print(*optimal_seat)