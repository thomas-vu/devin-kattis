def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

def find_optimum_anniversary(N, events):
    min_diff = float('inf')
    for i in range(N):
        for j in range(i + 1, N):
            diff = events[j] - events[i]
            for k in range(j + 1, N):
                min_diff = min(min_diff, gcd_of_three(events[i], events[j], events[k]))
    return min_diff

def gcd_of_three(a, b, c):
    return gcd(gcd(a, b), c)

def main():
    C = int(input())
    for case_num in range(1, C + 1):
        N = int(input().split()[0])
        events = list(map(int, input().split()))
        y = find_optimum_anniversary(N, events)
        print(f"Case #{case_num}: {y}")

if __name__ == "__main__":
    main()