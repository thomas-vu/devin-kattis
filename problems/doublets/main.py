from collections import deque

def is_doublet(word1, word2):
    if len(word1) != len(word2):
        return False
    diff_count = 0
    for c1, c2 in zip(word1, word2):
        if c1 != c2:
            diff_count += 1
    return diff_count == 1

def find_shortest_sequence(dictionary, start, end):
    queue = deque([[start]])
    visited = set()
    
    while queue:
        path = queue.popleft()
        current_word = path[-1]
        
        if current_word == end:
            return path
        
        for word in dictionary:
            if is_doublet(current_word, word) and word not in visited:
                new_path = list(path)
                new_path.append(word)
                queue.append(new_path)
                visited.add(word)
    
    return "No solution."

# Read the dictionary
dictionary = []
while True:
    word = input().strip()
    if not word:
        break
    dictionary.append(word)

# Process the input pairs
while True:
    try:
        start, end = input().strip().split()
        result = find_shortest_sequence(dictionary, start, end)
        if result == "No solution.":
            print("No solution.")
        else:
            for word in result:
                print(word)
        print()
    except EOFError:
        break