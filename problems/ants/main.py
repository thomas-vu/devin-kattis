def solve(l, positions):
    min_time = 0
    max_time = 0
    
    # Earliest time: the latest ant to start walking will take the longest
    min_time = max(positions)
    
    # Latest time: the sum of the distances to the ends minus the shortest distance to an end
    max_time = l - min(positions)
    
    return (min_time, max_time)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    cases = int(data[index])
    index += 1
    results = []
    
    for _ in range(cases):
        l = int(data[index])
        n = int(data[index + 1])
        positions = list(map(int, data[index + 2: index + 2 + n]))
        index += 2 + n
        
        earliest, latest = solve(l, positions)
        results.append((earliest, latest))
    
    for result in results:
        print(result[0], result[1])

main()