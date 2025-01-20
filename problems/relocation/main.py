N, Q = map(int, input().split())
locations = list(map(int, input().split()))

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        C, X = query[1], query[2]
        locations[C - 1] = X
    elif query[0] == 2:
        A, B = query[1], query[2]
        distance = abs(locations[A - 1] - locations[B - 1])
        print(distance)