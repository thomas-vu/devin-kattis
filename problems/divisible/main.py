def count_divisible_subsequences(d, n, sequence):
    count = 0
    for i in range(len(sequence)):
        current_sum = 0
        for j in range(i, len(sequence)):
            current_sum += sequence[j]
            if current_sum % d == 0:
                count += 1
    return count

def main():
    c = int(input())
    results = []
    for _ in range(c):
        d, n = map(int, input().split())
        sequence = list(map(int, input().split()))
        result = count_divisible_subsequences(d, n, sequence)
        results.append(result)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()