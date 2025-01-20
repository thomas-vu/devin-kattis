N, C = map(int, input().split())
w = list(map(int, input().split()))

windows = {}
s, e = 0, -1
result = [0] * N

while s < N:
    if e + 1 >= N:
        s += 1
    else:
        window_sum = sum(w[s:e+2])
        if window_sum > C:
            s += 1
        else:
            e += 1
    
    current_window = (s, e)
    if current_window not in windows:
        windows[current_window] = 0
    for i in range(s, e + 1):
        windows[current_window] += 1
        result[i] = len(windows)

for r in result:
    print(r)