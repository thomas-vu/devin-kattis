def min_cost(N, M, A, B):
    cost = 0
    while N > M:
        if (N - M) % 2 == 0:
            cost += ((N - M) // 2) * B
            N = (N + 1) // 2
        else:
            cost += A
            N -= 1
    return cost

def main():
    T = int(input())
    for t in range(1, T + 1):
        N, M, L = map(int, input().split())
        agencies = {}
        for _ in range(L):
            agency_name, rates = input().split(':')
            A, B = map(int, rates.split(','))
            cost = min_cost(N, M, A, B)
            agencies[agency_name] = cost
        
        sorted_agencies = sorted(agencies.items(), key=lambda x: (x[1], x[0]))
        print(f"Case {t}")
        for name, cost in sorted_agencies:
            print(f"{name} {cost}")

if __name__ == "__main__":
    main()