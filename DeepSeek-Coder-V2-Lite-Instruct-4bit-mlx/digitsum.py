def digit_sum(a, b):
    total_sum = 0
    for num in range(a, b + 1):
        total_sum += sum([int(digit) for digit in str(num)])
    return total_sum

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    results = []
    for i in range(1, t + 1):
        a, b = map(int, data[i].split())
        results.append(digit_sum(a, b))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()