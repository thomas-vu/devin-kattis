def right_justify(words):
    max_length = max(len(word) for word in words)
    justified_words = [word.rjust(max_length) for word in words]
    return justified_words

def dyslectionary(words):
    words.sort(key=lambda word: word[::-1])
    return right_justify(words)

def main():
    import sys
    input = sys.stdin.readlines()
    i = 0
    while i < len(input):
        words = []
        line = input[i].strip()
        while line:
            words.append(line)
            i += 1
            line = input[i].strip()
        words_sorted = dyslectionary(words)
        for word in words_sorted:
            print(word)
        if i < len(input) - 1:
            print()
        i += 1

if __name__ == "__main__":
    main()