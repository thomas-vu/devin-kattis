def shiritori_game(words):
    used_words = set()
    last_char = ''
    
    for i, word in enumerate(words):
        if word in used_words or (last_char and word[0] != last_char):
            return f"Player {i % 2 + 1} lost"
        used_words.add(word)
        last_char = word[-1]
    
    return "Fair Game"

# Read input
N = int(input())
words = [input().strip() for _ in range(N)]

# Output the result
print(shiritori_game(words))