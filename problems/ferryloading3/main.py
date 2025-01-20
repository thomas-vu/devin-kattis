from collections import deque

def ferry_crossing(n, t, m, cars):
    left_queue = deque()
    right_queue = deque()
    
    for arrival, bank in cars:
        if bank == "left":
            left_queue.append((arrival, i))
        else:
            right_queue.append((arrival, i))
    
    time = 0
    current_bank = "left"
    result = [0] * m
    
    while left_queue or right_queue:
        if current_bank == "left":
            loaded = 0
            while left_queue and loaded < n:
                if left_queue[0][0] <= time:
                    car = left_queue.popleft()
                    result[car[1]] = time + t
                    loaded += 1
                else:
                    break
            if left_queue or right_queue and loaded < n:
                time = max(time + t, left_queue[0][0] if left_queue else float('inf'))
            else:
                time = max(time + t, right_queue[0][0] if right_queue else float('inf'))
            current_bank = "right"
        else:
            loaded = 0
            while right_queue and loaded < n:
                if right_queue[0][0] <= time:
                    car = right_queue.popleft()
                    result[car[1]] = time + t
                    loaded += 1
                else:
                    break
            if left_queue or right_queue and loaded < n:
                time = max(time + t, right_queue[0][0] if right_queue else float('inf'))
            else:
                time = max(time + t, left_queue[0][0] if left_queue else float('inf'))
            current_bank = "left"
    
    return result

c = int(input())
for _ in range(c):
    n, t, m = map(int, input().split())
    cars = [input().split() for _ in range(m)]
    cars = [(int(arrival), bank) for arrival, bank in cars]
    
    result = ferry_crossing(n, t, m, cars)
    for time in result:
        print(time)
    if _ < c - 1:
        print()