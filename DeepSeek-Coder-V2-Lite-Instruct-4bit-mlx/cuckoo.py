def cuckoo_hashing(m, n, hash_values):
    table = [None] * n
    for i in range(m):
        word, h1, h2 = hash_values[i]
        pos1, pos2 = h1 % n, h2 % n
        if table[pos1] is None:
            table[pos1] = word
        elif table[pos2] is None:
            table[pos2] = word
        else:
            initial_word = word
            current_word = table[pos1]
            pos = pos1
            while True:
                next_pos = current_word[h1] % n if table[current_word[h1]] is not None else -1
                if next_pos == -1:
                    break
                table[pos], current_word = current_word, table[next_pos]
                pos = next_pos
            if next_pos == -1:
                table[next_pos] = initial_word
            else:
                table[pos] = initial_word
    return "successful hashing" if all(w is not None for w in table) else "rehash necessary"

def main():
    t = int(input())
    for _ in range(t):
        m, n = map(int, input().split())
        hash_values = [tuple(map(int, input().split())) for _ in range(m)]
        result = cuckoo_hashing(m, n, hash_values)
        print(result)

if __name__ == "__main__":
    main()