def evaluate(expr):
    parts = expr.split('^')
    value = int(parts[0])
    for part in parts[1:]:
        value = int(value) ** int(part)
    return value

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    M = int(data[0])
    integers = []
    
    for i in range(1, M + 1):
        expr = data[i]
        integers.append((evaluate(expr), expr))
    
    integers.sort()
    
    print("Case 1:")
    for _, expr in integers:
        print(expr)

if __name__ == "__main__":
    main()