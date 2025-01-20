def solve(n, wealths, min_wealths):
    total_wealth = sum(wealths)
    max_possible_poorest = min(wealths[i] - min_wealths[i] for i in range(n))
    return total_wealth - max_possible_poorest

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    C = int(data[index])
    index += 1
    results = []
    
    for _ in range(C):
        n = int(data[index])
        index += 1
        wealths = list(map(int, data[index:index + n]))
        index += n
        min_wealths = list(map(int, data[index:index + n]))
        index += n
        results.append(solve(n, wealths, min_wealths))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()