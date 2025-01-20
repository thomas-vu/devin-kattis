def last_digit_factorial(N):
    if N == 0 or N == 1:
        return 1
    result = 1
    for i in range(2, N + 1):
        result = (result * i) % 10
    return result

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(last_digit_factorial(N))

if __name__ == "__main__":
    main()