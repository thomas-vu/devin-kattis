import sys

def multiply_polynomials(poly1, poly2):
    n = len(poly1)
    m = len(poly2)
    result = [0] * (n + m - 1)
    
    for i in range(n):
        for j in range(m):
            result[i + j] += poly1[i] * poly2[j]
    
    return result

def main():
    input_data = sys.stdin.read().splitlines()
    T = int(input_data[0])
    index = 1
    
    for _ in range(T):
        n = int(input_data[index].split()[0])
        poly1 = list(map(int, input_data[index + 1].split()))
        m = int(input_data[index + 2].split()[0])
        poly2 = list(map(int, input_data[index + 3].split()))
        index += 4
        
        result = multiply_polynomials(poly1, poly2)
        print(len(result))
        print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()