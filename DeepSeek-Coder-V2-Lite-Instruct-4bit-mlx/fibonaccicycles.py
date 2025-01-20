def find_first_repeat(k):
    fib = [1, 1]
    seen = {1}
    
    n = 2
    while True:
        next_fib = (fib[-1] + fib[-2]) % k
        if next_fib in seen:
            return n
        fib.append(next_fib)
        seen.add(next_fib)
        n += 1

def main():
    Q = int(input())
    for _ in range(Q):
        k = int(input())
        print(find_first_repeat(k))

if __name__ == "__main__":
    main()