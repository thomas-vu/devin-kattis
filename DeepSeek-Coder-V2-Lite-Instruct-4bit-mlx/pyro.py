def count_alternates(L, values):
    powers = [1]
    for i in range(1, 19):
        powers.append(powers[-1] * 2)
    
    def generate_values():
        for mask in range(1, 1 << 18):
            yield sum([powers[i] for i in range(18) if mask & (1 << i)])
    
    original_values = set()
    for value in generate_values():
        if value <= L:
            original_values.add(value)
    
    count = 0
    for value in generate_values():
        if L < value <= 250000 and value != L:
            diff = value - L
            if sum((diff & x) == x for x in powers) <= 2:
                count += 1
                if value not in values:
                    values.add(value)
    
    return count

def main():
    while True:
        L = int(input())
        if L == -1:
            break
        values = set()
        count = count_alternates(L, values)
        print(f"{L}:{count}")

if __name__ == "__main__":
    main()