def calculate_score(a, b, c):
    min_tokens = min(a, b, c)
    return a**2 + b**2 + c**2 + 7 * min_tokens

def main():
    n = int(input())
    scores = []
    for _ in range(n):
        a, b, c, d = map(int, input().split())
        max_score = 0
        for i in range(4):
            if i <= d:
                tokens = [a + (i == 0), b + (i == 1), c + (i == 2)]
                max_score = max(max_score, calculate_score(*tokens))
        scores.append(max_score)
    for score in scores:
        print(score)

main()