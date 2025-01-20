def find_largest_d(b, k):
    if b % (k + 1) == 0:
        return k
    else:
        return b % (k + 1) - 1

def main():
    T = int(input())
    for _ in range(T):
        b, k = map(int, input().split())
        print(find_largest_d(b, k))

if __name__ == "__main__":
    main()