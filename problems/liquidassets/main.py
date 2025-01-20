def remove_unnecessary_letters(words):
    def process_word(word):
        result = []
        skip_next = False
        for i in range(len(word)):
            if skip_next:
                skip_next = False
                continue
            current_char = word[i]
            next_char = word[i + 1] if i + 1 < len(word) else ''
            if current_char == next_char:
                skip_next = True
            else:
                if current_char not in 'aeiou':
                    result.append(current_char)
        return ''.join(result)
    
    for i in range(len(words)):
        words[i] = process_word(words[i])
    
    return ' '.join(words)

# Read input
n = int(input())
S = input().split()

# Process and output the result
result = remove_unnecessary_letters(S)
print(result)