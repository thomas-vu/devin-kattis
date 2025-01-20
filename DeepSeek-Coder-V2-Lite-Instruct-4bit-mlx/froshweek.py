def min_swaps(students):
    n = len(students)
    swaps = 0
    for i in range(n):
        for j in range(1, n - i):
            if students[j] < students[j - 1]:
                students[j], students[j - 1] = students[j - 1], students[j]
                swaps += 1
    return swaps

n = int(input())
students = [int(input()) for _ in range(n)]
print(min_swaps(students))