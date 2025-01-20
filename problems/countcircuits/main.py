def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def generate_subsets(vectors):
    N = len(vectors)
    count = 0
    
    for mask in range(1, 1 << N):
        subset = [vectors[j] for j in range(N) if (mask & (1 << j))]
        if is_circuit(subset):
            count += 1
    
    return count

def is_circuit(subset):
    x, y = 0, 0
    for vector in subset:
        x += vector[0]
        y += vector[1]
        if x == 0 and y == 0:
            return False
    return (x, y) == (0, 0)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    vectors = [(int(data[i*2+1]), int(data[i*2+2])) for i in range(N)]
    
    result = generate_subsets(vectors)
    print(result)

if __name__ == "__main__":
    main()