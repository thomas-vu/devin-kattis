def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    i = 0
    sets_count = 0
    while True:
        n = int(data[i])
        if n == 0:
            break
        sets_count += 1
        names = data[i+1:i+n+1]
        result = []
        for j in range(n//2):
            result.insert(0, names[j])  # Insert at the beginning
            result.append(names[n//2 + j])  # Append at the end
        if n % 2 == 1:
            result.insert(0, names[n//2])
        print("SET", sets_count)
        for name in result:
            print(name)
        i += n + 1

if __name__ == "__main__":
    main()