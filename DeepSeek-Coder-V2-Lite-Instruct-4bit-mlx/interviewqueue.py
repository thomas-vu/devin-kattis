N = int(input())
values = list(map(int, input().split()))

minutes = 0
while True:
    leave_queue = []
    for i in range(len(values) - 1):
        if values[i] > values[i + 1]:
            leave_queue.append(values[i])
        else:
            leave_queue.append(values[i + 1])
    if len(leave_queue) == len(values):
        break
    values = leave_queue
    minutes += 1
    print('\n'.join(map(str, leave_queue)))

print(' '.join(map(str, values)))