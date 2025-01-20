def extract_words(messages):
    words = set()
    for message in messages:
        words.update(message.split())
    return words

def main():
    M = int(input().strip())
    messages = [input().strip() for _ in range(M)]
    
    word_count = {}
    for message in messages:
        words = extract_words([message])
        for word in words:
            if word not in word_count:
                word_count[word] = 0
            word_count[word] += 1
    
    if not word_count:
        print("ALL CLEAR")
        return
    
    sorted_words = sorted(word_count.keys(), key=lambda x: (-word_count[x], x))
    for word in sorted_words:
        print(word)

if __name__ == "__main__":
    main()