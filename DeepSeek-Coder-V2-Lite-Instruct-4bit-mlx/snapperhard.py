def light_state(N, K):
    # The state of the light is determined by the N-th snapper's position in the chain
    # After each snap, the state of the N-th snapper toggles if it has power
    # The N-th snapper will have power after an odd number of snaps
    if (K + 1) % (2 ** N) == 0:
        return "ON"
    else:
        return "OFF"

def main():
    T = int(input())
    for t in range(1, T + 1):
        N, K = map(int, input().split())
        result = light_state(N, K)
        print("Case #{}: {}".format(t, result))

if __name__ == "__main__":
    main()