N, M = map(int, input().split())
if N > M:
    P = N - M
    print(f"Dr. Chaz will have {P} piece[s] of chicken left over!")
else:
    Q = M - N
    print(f"Dr. Chaz needs {Q} more piece[s] of chicken!")