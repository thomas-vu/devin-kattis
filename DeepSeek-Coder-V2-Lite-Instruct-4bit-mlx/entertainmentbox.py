def max_shows(n, k):
    shows = []
    for _ in range(n):
        x_i, y_i = map(int, input().split())
        shows.append((x_i, y_i))
    
    shows.sort(key=lambda x: x[1])
    
    count = 0
    end_times = []
    
    for i in range(n):
        while end_times and end_times[0] <= shows[i][0]:
            count += 1
            end_times.pop(0)
        if len(end_times) < k:
            end_times.append(shows[i][1])
    
    return count + len(end_times)

n, k = map(int, input().split())
print(max_shows(n, k))