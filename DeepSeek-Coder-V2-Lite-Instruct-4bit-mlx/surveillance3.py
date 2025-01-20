def surveillance(B, W, S, T):
    count = 0
    for i in range(B - W + 1):
        for j in range(B - W + 1):
            match = True
            for k in range(W):
                for l in range(W):
                    if S[i + k][j + l] != T[k][l]:
                        match = False
                        break
                if not match:
                    break
            if match:
                count += 1
    return count