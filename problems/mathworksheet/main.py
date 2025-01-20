def main():
    while True:
        n = int(input())
        if n == 0:
            break
        
        results = []
        for _ in range(n):
            x, op, y = input().split()
            x = int(x)
            y = int(y)
            
            if op == '+':
                result = x + y
            elif op == '-':
                result = x - y
            else:  # op == '*'
                result = x * y
            
            results.append(result)
        
        max_len = max(len(str(max(results, key=lambda x: len(str(x)))))
        max_len = max(max_len, 2)  # To account for negative signs
        
        for i, result in enumerate(results):
            print(f"{result:{max_len}}", end=" " if (i + 1) % (50 // (max_len + 1)) else "\n")
        print()

if __name__ == "__main__":
    main()