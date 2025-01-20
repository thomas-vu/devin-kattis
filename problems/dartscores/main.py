def calculate_score(x, y):
    distance = (x**2 + y**2)**0.5
    if distance > 200:
        return 0
    for p in range(1, 11):
        if distance <= 20 * (11 - p):
            return p
    return 0

def main():
    T = int(input())
    results = []
    for _ in range(T):
        n = int(input())
        score_sum = 0
        for _ in range(n):
            x, y = map(int, input().split())
            score_sum += calculate_score(x, y)
        results.append(score_sum)
    for result in results:
        print(result)

main()