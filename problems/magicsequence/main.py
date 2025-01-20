def generate_sequence(N, A, B, C):
    S = [0] * N
    S[0] = A
    for i in range(1, N):
        S[i] = (S[i - 1] * B + A) % C
    return S

def hash_sequence(R, X, Y):
    V = 0
    for i in range(len(R)):
        V = (V * X + R[i]) % Y
    return V

def main():
    TC = int(input())
    results = []
    for _ in range(TC):
        N = int(input())
        A, B, C = map(int, input().split())
        X, Y = map(int, input().split())
        S = generate_sequence(N, A, B, C)
        R = sorted(S)
        V = hash_sequence(R, X, Y)
        results.append(V)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()