import sys

def find_pattern(pattern, text):
    positions = []
    start = 0
    while True:
        index = text.find(pattern, start)
        if index == -1:
            break
        positions.append(index + 1)  # Convert to 1-based index
        start = index + 1
    return positions

def main():
    while True:
        try:
            pattern = input().strip()
            text = input().strip()
            positions = find_pattern(pattern, text)
            print(' '.join(map(str, positions)))
        except EOFError:
            break

if __name__ == "__main__":
    main()