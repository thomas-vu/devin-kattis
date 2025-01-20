def light_state(N, K):
    if (K % (2**N)) % 2 == 1:
        return "ON"
    else:
        return "OFF"

def main():
    T = int(input())
    for t in range(1, T + 1):
        N, K = map(int, input().split())
        result = light_state(N, K)
        print("Case #{}: {}".format(t, result))

main()