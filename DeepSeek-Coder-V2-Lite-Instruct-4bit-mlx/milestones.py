def possible_speeds(M, N, T, X):
    diffs = []
    for i in range(M):
        for j in range(i + 1, M):
            diff = T[j] - T[i]
            dist = X[j] - X[i]
            if diff > 0 and dist % diff == 0:
                speed = dist // diff
                if speed not in diffs:
                    diffs.append(speed)
    return len(diffs), sorted(diffs)

def main():
    M, N = map(int, input().split())
    T = list(map(int, input().split()))
    X = list(map(int, input().split()))
    
    num_speeds, speeds = possible_speeds(M, N, T, X)
    print(num_speeds)
    if num_speeds > 0:
        print(" ".join(map(str, speeds)))

if __name__ == "__main__":
    main()