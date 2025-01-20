def f(x, y, a_list, b_list, c, d):
    if x < 0 or y < 0:
        return d
    if x == 0 and y == 0:
        return c
    result = 0
    for a, b in zip(a_list, b_list):
        result += f(x - a, y - b, a_list, b_list, c, d)
    return result + c

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    n = int(data[index])
    index += 1
    
    for _ in range(n):
        a_list = []
        b_list = []
        c, d = map(int, data[index].split())
        index += 1
        pairs = list(map(int, data[index].split()))
        index += 1
        
        for i in range(0, len(pairs), 2):
            a_list.append(pairs[i])
            b_list.append(pairs[i + 1])
        
        x_y_pairs = []
        while index < len(data):
            pairs = list(map(int, data[index].split()))
            index += 1
            x_y_pairs.extend(pairs)
        
        results = {}
        for x in range(100):
            for y in range(100):
                results[(x, y)] = f(x, y, a_list, b_list, c, d)
        
        for x in x_y_pairs:
            for y in x_y_pairs:
                print(results[(x, y)])
            if x_y_pairs.index((x, y)) < len(x_y_pairs) - 1:
                print()

if __name__ == "__main__":
    main()