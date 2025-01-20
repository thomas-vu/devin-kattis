def find_path(kitten_position, branches):
    path = []
    while kitten_position != -1:
        path.append(kitten_position)
        for branch in branches:
            if kitten_position in branches[branch]:
                kitten_position = branch
                break
    return path[::-1]

branches = {}
kitten_position = int(input())
while True:
    line = list(map(int, input().split()))
    if line[0] == -1:
        break
    a = line[0]
    b_list = line[1:]
    for b in b_list:
        if a not in branches:
            branches[a] = set()
        branches[a].add(b)
path = find_path(kitten_position, branches)
print(' '.join(map(str, path)))