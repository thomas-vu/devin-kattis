n, r, c = map(int, input().split())
seating_arrangement = [input().split() for _ in range(r)]
attendance_list = [input() for _ in range(n)]

for row in seating_arrangement:
    if attendance_list.index(row[0]) < attendance_list.index(row[-1]):
        print("left")
    else:
        print("right")