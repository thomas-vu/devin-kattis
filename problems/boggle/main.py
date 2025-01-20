import sys
from itertools import product

# Helper function to find words in the Boggle board
def find_words(board, trie):
    rows, cols = len(board), len(board[0])
    visited = [[False] * cols for _ in range(rows)]
    
    def dfs(x, y, node):
        if visited[x][y]:
            return []
        char = board[x][y]
        if char not in node:
            return []
        visited[x][y] = True
        word_list = list(node[char])
        for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                word_list.extend(dfs(nx, ny, node[char]))
        visited[x][y] = False
        return word_list
    
    words = set()
    for x in range(rows):
        for y in range(cols):
            words.update(dfs(x, y, trie))
    return words

# Helper function to build the Trie for efficient word search
def build_trie(words):
    trie = {}
    for word in words:
        node = trie
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['#'] = word  # Mark the end of a word
    return trie

# Read input
input_lines = sys.stdin.read().splitlines()
index = 0
w = int(input_lines[index])
index += 1
dictionary = [input_lines[index + i] for i in range(w)]
index += w + 1
b = int(input_lines[index])
index += 1
boards = [input_lines[index + i].split() for i in range(b)]

# Process each Boggle board
results = []
for board in boards:
    trie = build_trie(dictionary)
    found_words = find_words(board, trie)
    score = 0
    longest_word = ""
    word_count = len(found_words)
    
    for word in found_words:
        if len(word) == 3 or len(word) == 4:
            score += 1
        elif len(word) == 5:
            score += 2
        elif len(word) == 6:
            score += 3
        elif len(word) == 7:
            score += 5
        elif len(word) >= 8:
            score += 11
        
        if len(longest_word) < len(word):
            longest_word = word
        elif len(longest_word) == len(word):
            longest_word = min(longest_word, word)
    
    results.append((score, longest_word, word_count))

# Output the results
for result in results:
    print(result[0], result[1], result[2])