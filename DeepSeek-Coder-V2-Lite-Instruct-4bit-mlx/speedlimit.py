while True:
    n = int(input())
    if n == -1:
        break
    
    distance = 0
    prev_time = 0
    for _ in range(n):
        s, t = map(int, input().split())
        distance += s * (t - prev_time)
        prev_time = t
    
    print(distance, "miles")