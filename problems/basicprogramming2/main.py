N, t = map(int, input().split())
A = list(map(int, input().split()))

if t == 1:
    found = False
    for x in A:
        if 7777 - x in A and x != (7777 - x):
            found = True
            break
    print("Yes" if found else "No")
elif t == 2:
    unique = len(set(A)) == N
    print("Unique" if unique else "Contains duplicate")
elif t == 3:
    from collections import Counter
    count = Counter(A)
    for num, cnt in count.items():
        if cnt > N / 2:
            print(num)
            break
    else:
        print(-1)
elif t == 4:
    A.sort()
    mid = N // 2
    if N % 2 == 0:
        print(A[mid - 1], A[mid])
    else:
        print(A[mid])
elif t == 5:
    filtered = [x for x in A if 100 <= x <= 999]
    filtered.sort()
    print(" ".join(map(str, filtered)))