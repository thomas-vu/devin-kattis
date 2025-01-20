def calculate_cost(A, B, C):
    times = [list(map(int, input().split())) for _ in range(3)]
    total_cost = 0
    
    for start, end in times:
        parked_minutes = sum((1 if i >= start and i < end else 0) for i in range(1, 101))
        if parked_minutes == 1:
            total_cost += A
        elif parked_minutes == 2:
            total_cost += B * 2
        elif parked_minutes == 3:
            total_cost += C * 3
    
    return total_cost

A, B, C = map(int, input().split())
print(calculate_cost(A, B, C))