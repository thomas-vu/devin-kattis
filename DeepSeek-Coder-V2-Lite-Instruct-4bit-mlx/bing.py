def count_prefixes(words):
    root = {}
    for word in words:
        node = root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
            yield from count_nodes(node)
        yield len(word.split())

def count_nodes(node):
    count = 0
    for key in node:
        if key == '$':
            continue
        count += 1
        count += len(node[key])
    yield count

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    N = int(data[0])
    words = data[1:]
    results = count_prefixes(words)
    for _ in range(N):
        print(next(results))

if __name__ == "__main__":
    main()