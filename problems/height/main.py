def calculate_steps(heights):
    steps = 0
    line = []
    for height in heights:
        pos = len(line)
        while pos > 0 and line[pos - 1] < height:
            pos -= 1
            steps += 1
        line.insert(pos, height)
    return steps

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    P = int(data[0])
    index = 1
    results = []
    
    for _ in range(P):
        K = int(data[index])
        heights = list(map(int, data[index + 1: index + 21]))
        steps = calculate_steps(heights)
        results.append((K, steps))
        index += 21
    
    for K, steps in results:
        print(f"{K} {steps}")

if __name__ == "__main__":
    main()