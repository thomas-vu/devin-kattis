def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    weights = list(map(int, data[1:]))
    
    sorted_weights = sorted(weights)
    result = []
    
    for i in range(N):
        index = sorted_weights.index(weights[i])
        result.append(index)
    
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()