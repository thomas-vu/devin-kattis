def count_shuffles(n, shuffle_type):
    original_order = list(range(n))
    shuffled_order = original_order[:]
    
    def in_shuffle(deck):
        half = len(deck) // 2
        shuffled = []
        for i in range(half):
            shuffled.append(deck[i])
            shuffled.append(deck[half + i])
        if len(deck) % 2 == 1:
            shuffled.append(deck[-1])
        return shuffled
    
    def out_shuffle(deck):
        half = len(deck) // 2
        shuffled = []
        for i in range(half):
            shuffled.append(deck[i])
            shuffled.append(deck[half + i])
        return shuffled
    
    count = 0
    while True:
        if shuffle_type == 'in':
            shuffled_order = in_shuffle(shuffled_order)
        else:
            shuffled_order = out_shuffle(shuffled_order)
        count += 1
        if shuffled_order == original_order:
            break
    
    return count

def main():
    while True:
        try:
            line = input().strip()
            if not line:
                break
            n, shuffle_type = line.split()
            n = int(n)
            if shuffle_type == 'in':
                result = count_shuffles(n, shuffle_type)
                print(f"Case {count}: {result}")
            elif shuffle_type == 'out':
                result = count_shuffles(n, shuffle_type)
                print(f"Case {count}: {result}")
        except EOFError:
            break

if __name__ == "__main__":
    main()