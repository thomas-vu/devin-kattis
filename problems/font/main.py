def count_test_sentences(words):
    unique_letters = set('abcdefghijklmnopqrstuvwxyz')
    for word in words:
        unique_letters.intersection_update(set(word))
    if not unique_letters:
        return 0
    factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)
    return factorial(len(words)) // factorial(len(unique_letters)) ** len(words)

def main():
    while True:
        try:
            N = int(input())
            words = [input().strip() for _ in range(N)]
            result = count_test_sentences(words)
            print(result)
        except EOFError:
            break

if __name__ == "__main__":
    main()