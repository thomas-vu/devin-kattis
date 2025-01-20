def create_mean_word(words):
    mean_word = ""
    for i in range(len(words[0])):
        char_sum = 0
        for word in words:
            if i < len(word):
                char_sum += ord(word[i])
        mean_char = chr(char_sum // len(words))
        mean_word += mean_char
    return mean_word

def main():
    N = int(input())
    words = [input() for _ in range(N)]
    mean_word = create_mean_word(words)
    print(mean_word)

if __name__ == "__main__":
    main()