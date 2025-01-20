def find_smallest_gabonacci(n):
    if n == 1:
        return (1, 1)
    a, b = 1, 2
    while True:
        if n == a or n == b:
            return (a, b)
        a, b = b, a + b

def main():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        results.append(find_smallest_gabonacci(n))
    for result in results:
        print(result[0], result[1])

if __name__ == "__main__":
    main()