def min_unicycles(m, marks):
    marks.sort()
    count = 0
    i = 0
    while i < len(marks):
        start = marks[i]
        end = marks[i]
        while i < len(marks) - 1 and marks[i + 1] == marks[i] + 1:
            i += 1
            end = marks[i]
        count += (end - start) // m + 1
        i += 1
    return count

while True:
    try:
        line = input()
        if not line:
            continue
        m, n = map(int, line.split())
        marks = list(map(int, input().split()))
        print(min_unicycles(m, marks))
    except EOFError:
        break