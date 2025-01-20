def solve(n, permutation):
    swaps = []
    for i in range(n):
        min_idx = i
        for j in range(i, n):
            if permutation[j] < permutation[min_idx]:
                min_idx = j
        if min_idx != i:
            swaps.append((i, min_idx))
            permutation[i], permutation[min_idx] = permutation[min_idx], permutation[i]
    return swaps

def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        permutation = list(map(int, input().split()))
        swaps = solve(n, permutation)
        print(len(swaps))
        for swap in swaps:
            print(*swap)

if __name__ == "__main__":
    main()