def distance(a, b):
    x1, y1 = divmod(ord(a) - ord('a'), 5)
    x2, y2 = divmod(ord(b) - ord('a'), 5)
    return abs(x1 - x2) + abs(y1 - y2)

def sort_words(typed, words):
    word_distances = []
    for word in words:
        dist = sum(distance(a, b) for a, b in zip(typed, word))
        word_distances.append((word, dist))
    word_distances.sort(key=lambda x: (x[1], x[0]))
    return word_distances

def main():
    t = int(input())
    for _ in range(t):
        typed, l = input().split()
        words = [input().strip() for _ in range(int(l))]
        sorted_words = sort_words(typed, words)
        for word, dist in sorted_words:
            print(f"{word} {dist}", end=" ")
        print()

if __name__ == "__main__":
    main()