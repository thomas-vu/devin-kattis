def max_additional_friends(S, N, occupied):
    additional = 0
    for i in range(1, S + 1):
        if all((i not in occupied and (i - 1) % S not in occupied and (i + 1) % S not in occupied)):
            additional += 1
            occupied.append(i)
    return additional

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    while index < len(data):
        S = int(data[index])
        N = int(data[index + 1])
        occupied = list(map(int, data[index + 2: index + 2 + N]))
        index += 2 + N
        
        result = max_additional_friends(S, N, occupied)
        print(result)

if __name__ == "__main__":
    main()