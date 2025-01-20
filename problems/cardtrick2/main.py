def magician_trick(n):
    cards = list(range(1, n + 1))
    result = []
    for i in range(n):
        if i % 2 == 0:
            result.append(cards[i // 2])
        else:
            cards.insert(i // 2 + 1, cards[i // 2])
    return result

def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        result = magician_trick(n)
        print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()