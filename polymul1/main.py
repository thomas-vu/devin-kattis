def multiply_polynomials(p1, p2):
    result = [0] * (len(p1) + len(p2) - 1)
    for i in range(len(p1)):
        for j in range(len(p2)):
            result[i + j] += p1[i] * p2[j]
    return result

def main():
    T = int(input())
    for _ in range(T):
        # Read first polynomial
        n1 = int(input())
        p1 = list(map(int, input().split()))
        
        # Read second polynomial
        n2 = int(input())
        p2 = list(map(int, input().split()))
        
        # Multiply polynomials
        result = multiply_polynomials(p1, p2)
        
        # Output result
        print(len(result) - 1)
        print(*result)

if __name__ == "__main__":
    main()
