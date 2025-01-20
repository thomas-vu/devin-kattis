from itertools import permutations
import sys

def min_time(students):
    N = len(students)
    if N == 1:
        return 0
    
    min_time = sys.maxsize
    for perm in permutations(students):
        current_position = (0, 0)
        time_taken = 0
        for student in perm:
            distance = abs(student[0] - current_position[0]) + abs(student[1] - current_position[1])
            time_taken += distance
            current_position = student
        min_time = min(min_time, time_taken)
    return min_time

N = int(input().strip())
students = [tuple(map(int, input().strip().split())) for _ in range(N)]
print(min_time(students))