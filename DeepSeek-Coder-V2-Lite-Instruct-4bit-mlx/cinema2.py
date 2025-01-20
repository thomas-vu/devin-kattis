N, M = map(int, input().split())
groups = list(map(int, input().split()))

accepted_count = 0
for group in groups:
    if N >= group:
        N -= group
        accepted_count += 1
print(M - accepted_count)