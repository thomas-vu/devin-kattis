def count_double_vowel_pairs(word):
    vowels = "aeiouy"
    count = 0
    i = 0
    while i < len(word) - 1:
        if word[i] in vowels and word[i + 1] == word[i]:
            count += 1
            i += 2
        else:
            i += 1
    return count

def main():
    while True:
        N = int(input())
        if N == 0:
            break
        words = [input().strip() for _ in range(N)]
        favorite_word = max(words, key=count_double_vowel_pairs)
        print(favorite_word)

if __name__ == "__main__":
    main()