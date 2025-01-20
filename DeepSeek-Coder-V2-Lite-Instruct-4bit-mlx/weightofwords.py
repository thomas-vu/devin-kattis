def find_word(l, w):
    def letter_weight(c):
        return ord(c) - ord('a') + 1
    
    def generate_words():
        for i in range(1, l + 1):
            min_weight = (i - 1) * 1 + i * 1
            max_weight = (i - 1) * 26 + i * 26
            if min_weight <= w <= max_weight:
                for combo in range(min_weight, max_weight + 1):
                    if sum([combo // i for i in range(1, l + 1)]) == w:
                        letters = [chr(ord('a') + (combo // i) - 1) for i in range(1, l + 1)]
                        yield ''.join(letters)
    
    for word in generate_words():
        return word
    return "impossible"

# Read input
l, w = map(int, input().split())
result = find_word(l, w)
print(result)