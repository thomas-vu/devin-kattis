def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    test_cases = int(data[index])
    index += 1
    results = []
    
    for _ in range(test_cases):
        m, r = int(data[index]), int(data[index + 1])
        index += 2
        movies = list(range(1, m + 1))
        
        requests = [int(x) for x in data[index: index + r]]
        index += r
        
        positions = []
        for request in requests:
            movies.remove(request)
            movies.insert(0, request)
            positions.append(movies.index(request))
        
        results.append(' '.join(map(str, positions)))
    
    print('\n'.join(results))

if __name__ == "__main__":
    main()