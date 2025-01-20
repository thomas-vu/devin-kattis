def find_largest_gap(n, w, u, v, t1, t2, lanes):
    def calculate_crossing_time(lane, start_position):
        if lane[0] == 'E':
            max_distance = 0
            for i in range(len(lane[1])):
                if lane[1][i][0] == 'W':
                    max_distance = max(max_distance, lane[1][i][1] - start_position)
                else:
                    max_distance = max(max_distance, -lane[1][i][1] + start_position)
            return max_distance / u
        else:
            min_distance = 0
            for i in range(len(lane[1])):
                if lane[1][i][0] == 'E':
                    min_distance = max(min_distance, lane[1][i][1] - start_position)
                else:
                    min_distance = max(min_distance, -lane[1][i][1] + start_position)
            return min_distance / v

    max_gap = 0
    for lane in lanes:
        for i in range(len(lane[1])):
            crossing_time = calculate_crossing_time(lane, lane[1][i][1])
            if t1 + crossing_time <= t2:
                max_gap = max(max_gap, lane[1][i][1] / u)
    return max_gap * 2

# Read input
n, w, u, v = map(int, input().split())
t1, t2 = map(int, input().split())
lanes = []
for _ in range(n):
    lane_data = input().split()
    direction = lane_data[0]
    m = int(lane_data[1])
    ships = []
    for j in range(m):
        l, p = map(int, lane_data[2+j*2])
        ships.append((direction, p))
    lanes.append((direction, ships))

# Calculate and output the result
result = find_largest_gap(n, w, u, v, t1, t2, lanes)
print("{:.8f}".format(result))