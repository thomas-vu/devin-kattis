def find_positions(s, queries):
    suffixes = sorted([s[i:] for i in range(len(s))])
    positions = []
    for query in queries:
        positions.append(suffixes[query])
    return positions

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    i = 0
    while i < len(data):
        s = data[i]
        n = int(data[i + 1])
        queries = list(map(int, data[i + 2: i + 2 + n]))
        positions = find_positions(s, queries)
        print(' '.join(map(str, positions)))
        i += n + 2

if __name__ == "__main__":
    main()