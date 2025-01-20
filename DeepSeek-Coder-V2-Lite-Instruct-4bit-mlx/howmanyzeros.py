def count_zeros(m, n):
    count = 0
    for i in range(m, n + 1):
        count += str(i).count('0')
    return count

def main():
    while True:
        line = input()
        if line == "-1 -1":
            break
        m, n = map(int, line.split())
        print(count_zeros(m, n))

if __name__ == "__main__":
    main()