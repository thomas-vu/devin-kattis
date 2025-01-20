def calculate_value(walks):
    value = 0
    for walk in walks:
        temp_value = 1
        for step in walk:
            if step == 'L':
                temp_value *= 2
            elif step == 'R':
                temp_value = temp_value * 2 + 1
            # P represents a pause, so we do nothing in that step
        value += temp_value
    return value

def main():
    pattern = input().strip()
    n = len(pattern)
    from itertools import product
    possible_walks = [''.join(p) for p in product('LR*P', repeat=n)]
    filtered_walks = [walk for walk in possible_walks if all(c != '*' or x == 'X' for c, x in zip(walk, pattern))]
    result = calculate_value(filtered_walks)
    print(result)

if __name__ == "__main__":
    main()