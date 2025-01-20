x_min, x_max = map(int, input().split())
Q = int(input())
cameras = {}
installations = []
vandalizations = []

for _ in range(Q):
    query = input().split()
    if query[0] == '+':
        s, a, b = int(query[1]), int(query[2]), int(query[3])
        cameras[s] = (a, b)
        installations.append(s)
    else:
        s = int(query[1])
        vandalizations.append(s)
        if s in cameras:
            del cameras[s]

# Check if it's possible to monitor the entire segment with one or two cameras
possible_one = False
possible_two = False
active_cameras = set()
for camera in cameras.values():
    a, b = camera
    if b < x_min or a > x_max:
        continue
    for i in range(a, b + 1):
        if i >= x_min and i <= x_max:
            active_cameras.add(i)
if len(active_cameras) == x_max - x_min + 1:
    possible_one = True
else:
    for i in range(x_min, x_max + 1):
        if i not in active_cameras:
            for camera in cameras.values():
                a, b = camera
                if i >= a and i <= b:
                    active_cameras.add(i)
            if len(active_cameras) == x_max - x_min + 1:
                possible_two = True
                break
            else:
                active_cameras.remove(i)

for _ in range(Q):
    if possible_one:
        print(1)
    elif possible_two:
        print(2)
    else:
        print(-1)