def initial_passengers(k):
    n = 1
    for _ in range(k - 1):
        n = (n * 2) + 0.5
    return int(n)

def main():
    T = int(input())
    for _ in range(T):
        k = int(input())
        print(initial_passengers(k))

if __name__ == "__main__":
    main()