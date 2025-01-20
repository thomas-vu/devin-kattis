N = int(input())
M = int(input())

students_per_room = M // N
extra_students = M % N

for i in range(N):
    if i < extra_students:
        print('*' * (students_per_room + 1), end='')
    else:
        print('*' * students_per_room, end='')
    print()