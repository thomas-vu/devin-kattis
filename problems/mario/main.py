def min_time_to_reach(N, W, boats):
    times = [0] * N
    for i in range(N):
        L, R = boats[i]
        period = R - L
        for j in range(N):
            if i != j:
                other_L, other_R = boats[j]
                overlap = min(R, other_R) - max(L, other_L)
                if overlap > 0:
                    period = min(period, (overlap * 2) - ((other_R - other_L) % overlap))
        times[i] = period + (R - L) * ((W - R) // (R - L))
    min_time = float('inf')
    for time in times:
        if time != 0:
            min_time = min(min_time, time)
    return min_time if min_time != float('inf') else 'IMPOSSIBLE'

def main():
    T = int(input())
    for _ in range(T):
        N, W = map(int, input().split())
        boats = [list(map(int, input().split())) for _ in range(N)]
        result = min_time_to_reach(N, W, boats)
        print(result)

if __name__ == "__main__":
    main()