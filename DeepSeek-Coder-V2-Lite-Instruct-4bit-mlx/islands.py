def count_islands(sequence):
    islands = 0
    n = len(sequence)
    for i in range(1, n - 1):
        if sequence[i] > sequence[i - 1] and sequence[i] > sequence[i + 1]:
            islands += 1
    return islands

def main():
    P = int(input())
    for _ in range(P):
        K, *sequence = map(int, input().split())
        num_islands = count_islands(sequence)
        print(f"{K} {num_islands}")

if __name__ == "__main__":
    main()