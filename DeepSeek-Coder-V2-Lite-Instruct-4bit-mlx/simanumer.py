def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    phone_numbers = data[1:]
    Q = int(data[N+1])
    queries = data[N+2:]
    
    phone_numbers.sort()
    
    for query in queries:
        count = 0
        for number in phone_numbers:
            if number.startswith(query):
                count += 1
        print(count)

if __name__ == "__main__":
    main()