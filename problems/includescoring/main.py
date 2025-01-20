def calculate_scores(n, contestant_data):
    scores = []
    for data in contestant_data:
        s, p, f, o = data
        if f == 0 and o == 0:
            scores.append(0)
        else:
            rank = s * 1000000 + p * 100 + f
            if o == 1:
                scores.append(rank + 1)
            else:
                scores.append(rank)
    return scores

def main():
    n = int(input())
    contestant_data = [list(map(int, input().split())) for _ in range(n)]
    scores = calculate_scores(n, contestant_data)
    for score in scores:
        print(score)

if __name__ == "__main__":
    main()