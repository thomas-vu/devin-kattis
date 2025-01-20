def find_alone(guests):
    count = {}
    for guest in guests:
        if guest in count:
            count[guest] += 1
        else:
            count[guest] = 1
    for guest, cnt in count.items():
        if cnt % 2 != 0:
            return guest

def main():
    N = int(input().strip())
    for x in range(1, N + 1):
        G = int(input().strip())
        guests = list(map(int, input().split()))
        alone_guest = find_alone(guests)
        print("Case #{}: {}".format(x, alone_guest))

if __name__ == "__main__":
    main()