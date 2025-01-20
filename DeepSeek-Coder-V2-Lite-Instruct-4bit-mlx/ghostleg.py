def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n, m = int(data[0]), int(data[1])
    rungs = [int(data[i+2]) for i in range(m)]
    
    result = list(range(1, n+1))
    
    for rung in rungs:
        result[rung], result[rung+1] = result[rung+1], result[rung]
    
    for element in result:
        print(element)

if __name__ == "__main__":
    main()