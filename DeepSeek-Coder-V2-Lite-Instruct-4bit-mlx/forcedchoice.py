N, P, S = map(int, input().split())
for _ in range(S):
    choices = list(map(int, input().split()))
    if P in choices:
        print("KEEP")
    else:
        print("REMOVE")