def max_bishops(n):
    if n == 1:
        return 0
    elif n % 2 == 0:
        return n
    else:
        return n - 1

def main():
    while True:
        try:
            n = int(input())
            print(max_bishops(n))
        except EOFError:
            break

if __name__ == "__main__":
    main()