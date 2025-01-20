def time_before(H, M):
    if M >= 45:
        return H, M - 45
    else:
        if H == 0:
            return 23, M + 60 - 45
        else:
            return H - 1, M + 60 - 45

H, M = map(int, input().split())
new_H, new_M = time_before(H, M)
print(new_H, new_M)