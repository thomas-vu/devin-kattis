n = int(input())
residents = {}
for _ in range(n):
    name = input().split()
    if len(name) == 1:
        residents[name[0]] = False
    else:
        residents[name[0]] = name[1]

m = int(input())
queries = [input().strip() for _ in range(m)]

for query in queries:
    if query not in residents:
        print("Neibb")
    elif not residents[query]:
        print(f"Jebb")
    else:
        correct_name = query + " " + residents[query]
        print(f"Neibb en {correct_name} er heima")