def max_ones(n):
    binary = bin(n)[2:]
    count = 0
    max_count = 0
    for bit in binary:
        if bit == '1':
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
    return max_count

def main():
    T = int(input())
    for _ in range(T):
        X = int(input())
        print(max_ones(X))

if __name__ == "__main__":
    main()