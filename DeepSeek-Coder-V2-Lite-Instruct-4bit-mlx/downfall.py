def main():
    N, R, K, X0, A, B = map(int, input().split())
    buckets = [0] * N
    
    for i in range(R):
        X_i = (A * X0 + B) % N
        buckets[X_i] += 1
        if buckets[X_i] == K:
            print("OVERFLOW")
            return
        X0 = X_i
    
    a = 0
    for i in range(R):
        O_i = buckets[X0]
        a = (53 * a + O_i) % 199933
        X0 = (X0 + 1) % N
    
    print(a)

if __name__ == "__main__":
    main()