def solve(n, m, prizes, stickers):
    total_value = 0
    for prize in prizes:
        k, *sticker_types, value = prize
        can_claim = True
        for sticker_type in sticker_types:
            if stickers[sticker_type - 1] == 0:
                can_claim = False
                break
        if can_claim:
            for sticker_type in sticker_types:
                stickers[sticker_type - 1] -= 1
            total_value += value
    return total_value

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    test_cases = int(data[index])
    index += 1
    results = []
    
    for _ in range(test_cases):
        n = int(data[index])
        m = int(data[index + 1])
        index += 2
        prizes = []
        for _ in range(n):
            k, *sticker_types, value = map(int, data[index].split())
            prizes.append((k, sticker_types, value))
            index += 1
        stickers = list(map(int, data[index].split()))
        index += 1
        results.append(solve(n, m, prizes, stickers))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()