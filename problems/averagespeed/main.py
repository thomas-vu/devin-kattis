def time_to_seconds(time_str):
    h, m, s = map(int, time_str.split(':'))
    return h * 3600 + m * 60 + s

def seconds_to_time(seconds):
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return f"{h:02d}:{m:02d}:{s:02d}"

speeds = []
while True:
    try:
        time_str, speed_str = input().split()
        speeds.append((time_to_seconds(time_str), int(speed_str)))
    except EOFError:
        break

queries = []
while True:
    try:
        query_time = time_to_seconds(input())
        queries.append(query_time)
    except EOFError:
        break

distances = []
current_speed = 0
start_time = 0
for i in range(len(speeds)):
    if i == 0:
        start_time = speeds[i][0]
        current_speed = speeds[i][1]
    else:
        time_diff = speeds[i][0] - speeds[i-1][0]
        distances.append((start_time, current_speed))
        start_time = speeds[i][0]
        current_speed = speeds[i][1]
distances.append((start_time, current_speed))

for query in queries:
    total_distance = 0.0
    for start, speed in distances:
        if query >= start and (len(distances) == 1 or query < distances[distances.index((start, speed)) + 1][0]):
            time_diff = query - start
            total_distance += speed * (time_diff / 3600)
            break
    print(f"{seconds_to_time(query)} {total_distance:.2f} km")