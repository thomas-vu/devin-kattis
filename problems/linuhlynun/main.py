n = int(input())
students = []
for _ in range(n):
    x_i, c_i = map(int, input().split())
    students.append((x_i, c_i))

min_pollution = float('inf')
best_house = 0
for i in range(n):
    total_pollution = 0
    for j in range(n):
        distance = abs(students[i][0] - students[j][0])
        total_pollution += distance * students[j][1]
    if total_pollution < min_pollution:
        min_pollution = total_pollution
        best_house = students[i][0]
    elif total_pollution == min_pollution:
        best_house = min(best_house, students[i][0])

print(best_house)