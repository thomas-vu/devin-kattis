def is_antiarithmetic(perm):
    n = len(perm)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if perm[i] - perm[j] == perm[j] - perm[k]:
                    return "no"
    return "yes"

while True:
    line = input()
    if line == "0":
        break
    parts = line.split(": ")
    n = int(parts[0])
    perm = list(map(int, parts[1].split()))
    result = is_antiarithmetic(perm)
    print(result)