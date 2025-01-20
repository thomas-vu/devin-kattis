def add_word_to_dict(start, end, words):
    word_set = set(words)
    if end in word_set:
        return 0, -1
    
    queue = [(start, [start])]
    visited = set()
    
    while queue:
        word, path = queue.pop(0)
        for i in range(len(word)):
            for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                new_word = word[:i] + char + word[i+1:]
                if new_word in word_set and new_word not in visited:
                    new_path = path + [new_word]
                    if new_word == end:
                        return '', len(new_path) - 1
                    queue.append((new_word, new_path))
                    visited.add(new_word)
    return '', -1

def main():
    n = int(input())
    words = [input().strip() for _ in range(n)]
    start, end = words[0], words[-1]
    
    if len(start) != len(end):
        print("0")
        print("-1")
        return
    
    word_to_add, steps = add_word_to_dict(start, end, words)
    if word_to_add:
        print(word_to_add)
        print(steps)
    else:
        print("0")
        print("-1")

if __name__ == "__main__":
    main()