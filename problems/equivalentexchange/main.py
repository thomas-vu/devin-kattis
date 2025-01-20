d = int(input())
items_found = {}
for _ in range(d):
    query = list(map(int, input().split()))
    if query[0] == 1:
        f_i = query[1]
        if f_i not in items_found:
            items_found[f_i] = 1
        else:
            items_found[f_i] += 1
    elif query[0] == 2:
        s_i, d_i = query[1], query[2]
        if s_i in items_found:
            count = min(items_found[s_i], d_i)
            items_found[d_i] = count if d_i not in items_found else items_found[d_i] + count
            if items_found[s_i] == d_i:
                del items_found[s_i]
for day in sorted(items_found.keys()):
    print(day)