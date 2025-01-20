def calculate_audience_votes(N, points):
    min_score = float('inf')
    for i in range(N):
        score = points[i] + sum([p * (1/sum(points)) for p in points])
        min_score = min(min_score, score)
    
    X = sum(points)
    audience_votes = []
    for i in range(N):
        low = 0.0
        high = 100.0
        while high - low > 1e-9:
            mid = (high + low) / 2.0
            score = points[i] + mid * (X / N)
            if min([points[j] + points[j] * (mid / 100.0) for j in range(N)]) <= score:
                high = mid
            else:
                low = mid
        audience_votes.append(high)
    return [round(x, 6) for x in audience_votes]

def main():
    T = int(input())
    for t in range(1, T + 1):
        N, *points = map(int, input().split())
        result = calculate_audience_votes(N, points)
        print("Case #{}: {}".format(t, " ".join("{:.6f}".format(x) for x in result)))

if __name__ == "__main__":
    main()