def find_compound_words(words):
    word_set = set(words)
    compound_words = set()
    
    for word in words:
        for i in range(1, len(word)):
            prefix = word[:i]
            suffix = word[i:]
            if prefix in word_set and suffix in word_set:
                compound_words.add(word)
    
    return sorted(compound_words)

def main():
    words = []
    while True:
        try:
            line = input()
            words.extend(line.split())
        except EOFError:
            break
    
    compound_words = find_compound_words(words)
    for word in compound_words:
        print(word)

if __name__ == "__main__":
    main()