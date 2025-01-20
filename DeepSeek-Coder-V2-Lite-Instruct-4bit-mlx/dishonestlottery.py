def main():
    n = int(input())
    counts = {i: 0 for i in range(1, 51)}
    
    for _ in range(10 * n):
        numbers = list(map(int, input().split()))
        for number in numbers:
            counts[number] += 1
    
    result = [num for num, cnt in counts.items() if cnt > 2 * n]
    result.sort()
    if not result:
        print(-1)
    else:
        print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()