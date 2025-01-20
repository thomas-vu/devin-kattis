def decode_message(p, s):
    n = len(s)
    coefficients = [0] * (n + 1)
    
    for k in range(1, n + 1):
        value = 0
        for i in range(n):
            if s[i] == '*':
                coefficients[k] = (coefficients[k] * p + i) % 26
            else:
                value = (value * p + ord(s[i]) - ord('a') + 1) % 26
        if value == k:
            coefficients[k] = 0
    
    return [coefficients[i + 1] for i in range(n)]

def main():
    N = int(input())
    for _ in range(N):
        p, s = input().split()
        p = int(p)
        result = decode_message(p, s)
        print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()