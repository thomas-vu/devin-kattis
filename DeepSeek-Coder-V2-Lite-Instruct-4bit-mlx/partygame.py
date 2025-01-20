def determine_outcome(n, cards):
    for i in range(n):
        count = 0
        current = i
        while cards[current] != i + 1:
            count += 1
            current = cards[current] - 1
            if count > n:
                return "Some starve."
    return "All can eat."

def main():
    T = int(input())
    results = []
    for _ in range(T):
        n = int(input())
        cards = list(map(int, input().split()))
        results.append(determine_outcome(n, cards))
    for result in results:
        print(result)

if __name__ == "__main__":
    main()