def find_shortest_word(words):
    def can_combine(s, t):
        for k in range(1, min(len(s), len(t)) + 1):
            if s[-k:] == t[:k]:
                return True
        return False
    
    def combine_words(s, t):
        for k in range(1, min(len(s), len(t)) + 1):
            if s[-k:] == t[:k]:
                return s + t[k:]
    
    while len(words) > 1:
        combined = False
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if can_combine(words[i], words[j]):
                    new_word = combine_words(words[i], words[j])
                    words.pop(j)
                    words[i] = new_word
                    combined = True
                    break
            if combined:
                break
        if not combined:
            return -1
    
    return words[0]

# Read the number of words
n = int(input())
words = [input().strip() for _ in range(n)]
shortest_word = find_shortest_word(words)
print(shortest_word)