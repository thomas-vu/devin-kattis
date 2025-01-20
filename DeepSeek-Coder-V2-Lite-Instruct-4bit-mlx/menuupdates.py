d, U = map(int, input().split())
available = []
reserved = set()
next_available = 1

for _ in range(U):
    line = input().split()
    if line[0] == 'a':
        available.append(next_available)
        print(next_available)
        next_available += 1
    elif line[0] == 'r':
        item = int(line[1])
        reserved.add(item)
        for _ in range(d):
            if item in available:
                available.remove(item)
        next_available = max(next_available, item + d)