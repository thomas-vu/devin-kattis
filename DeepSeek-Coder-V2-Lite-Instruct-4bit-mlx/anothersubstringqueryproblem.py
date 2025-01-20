def find_kth_occurrence(s, t, k):
    count = 0
    index = -1
    while k > 0 and index == -1:
        start = s.find(t, count) + 1
        if start == 0:
            index = -1
            break
        count = start + len(t)
        k -= 1
    return index

s = input().strip()
q = int(input().strip())
for _ in range(q):
    t, k = input().strip().split()
    k = int(k)
    result = find_kth_occurrence(s, t, k)
    print(result)