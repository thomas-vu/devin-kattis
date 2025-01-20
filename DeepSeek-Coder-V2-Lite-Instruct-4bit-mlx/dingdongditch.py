def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    N = int(data[idx])
    Q = int(data[idx + 1])
    idx += 2
    
    A = list(map(int, data[idx: idx + N]))
    idx += N
    
    B = list(map(int, data[idx:]))
    
    for b in B:
        if b == 1 or b == N:
            print(sum(A))
        else:
            A.sort()
            min_sum = sum(A[:b])
            for i in range(1, N - b + 1):
                min_sum = min(min_sum, sum(A[i:i + b]))
            print(min_sum)

if __name__ == "__main__":
    main()