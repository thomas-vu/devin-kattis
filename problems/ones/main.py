def smallest_multiple(n):
    if n % 2 == 0 or n % 5 == 0:
        return -1
    num = 1
    count = 1
    while (num % n) != 0:
        num = num * 10 + 1
        count += 1
    return count

def main():
    while True:
        try:
            n = int(input())
            print(smallest_multiple(n))
        except EOFError:
            break

if __name__ == "__main__":
    main()