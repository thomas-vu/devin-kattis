def count_outlets(power_strips):
    total_outlets = 1
    for strip in power_strips:
        total_outlets += (strip - 1)
    return total_outlets

def main():
    N = int(input())
    for _ in range(N):
        K, *outlets = map(int, input().split())
        print(count_outlets([K] + outlets))

if __name__ == "__main__":
    main()