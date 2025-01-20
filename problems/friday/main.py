def count_friday_13ths(D, months):
    days = 0
    for month in months:
        days += month
        if days % 7 == 5:
            count = 1
    return count

def main():
    T = int(input())
    for _ in range(T):
        D, M = map(int, input().split())
        months = list(map(int, input().split()))
        count = count_friday_13ths(D, months)
        print(count)

if __name__ == "__main__":
    main()