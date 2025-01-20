def remove_duplicates(chores):
    seen = set()
    unique_chores = []
    for chore in chores:
        if chore not in seen:
            unique_chores.append(chore)
            seen.add(chore)
    return unique_chores

N = int(input())
chores = [input().strip() for _ in range(N)]
unique_chores = remove_duplicates(chores)
for chore in unique_chores:
    print(chore)