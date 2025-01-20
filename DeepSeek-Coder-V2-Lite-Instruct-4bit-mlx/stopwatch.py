def stopwatch(N, times):
    if N % 2 != 0:
        return "still running"
    
    timer = 0
    for i in range(1, N, 2):
        timer += times[i] - times[i-1]
    return timer

N = int(input())
times = [int(input()) for _ in range(N)]
print(stopwatch(N, times))