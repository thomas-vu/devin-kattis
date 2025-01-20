def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def count_relatively_prime(n):
    if n == 1:
        return 1
    count = 0
    for i in range(1, n):
        if gcd(i, n) == 1:
            count += 1
    return count

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        print(count_relatively_prime(n))

if __name__ == "__main__":
    main()