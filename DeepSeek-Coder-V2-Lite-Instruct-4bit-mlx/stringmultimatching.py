def find_all(pattern, text):
    positions = []
    start = 0
    while True:
        index = text.find(pattern, start)
        if index == -1:
            break
        positions.append(index + 1)  # Convert to 1-based index for output
        start = index + 1
    return positions

def main():
    while True:
        try:
            n = int(input())
            patterns = [input().strip() for _ in range(n)]
            text = input().strip()
            
            results = []
            for pattern in patterns:
                positions = find_all(pattern, text)
                results.append(' '.join(map(str, positions)))
            
            for result in results:
                print(result)
        except EOFError:
            break

if __name__ == "__main__":
    main()