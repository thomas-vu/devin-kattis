def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def parse_input():
    n = int(input())
    gears = [tuple(map(int, input().split())) for _ in range(n)]
    return gears

def is_tangent(g1, g2):
    x1, y1, r1 = g1
    x2, y2, r2 = g2
    return (x1 - x2)**2 + (y1 - y2)**2 == (r1 + r2)**2

def find_connections(gears):
    connections = {0: []}  # Gear 0 is the source gear
    for i in range(1, len(gears)):
        if is_tangent(gears[0], gears[i]):
            connections[0].append(i)
        connections[i] = []
    for i in range(1, len(gears)):
        for j in range(i + 1, len(gears)):
            if is_tangent(gears[i], gears[j]):
                connections[i].append(j)
                connections[j].append(i)
    return connections

def can_move(source, target, connections):
    if not connections[source]:
        return -1
    for conn in connections[source]:
        if conn == target:
            return 0
    return (1, -1)  # Assuming the source turns and moves the target in opposite direction

def solve():
    gears = parse_input()
    connections = find_connections(gears)
    result = can_move(0, len(gears) - 1, connections)
    if result == -1:
        print(-1)
    elif result == 0:
        print(0)
    else:
        a, b = result
        gcd_ab = gcd(a, abs(b))
        print(f"{a // gcd_ab} {-b // gcd_ab}")

solve()