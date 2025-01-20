def calculate_sum_of_teams(N, P):
    P.sort()
    S = 0
    for i in range(N):
        team_score = P[3*i + 1]
        S += team_score
    return S

def main():
    num_datasets = int(input())
    for _ in range(num_datasets):
        N = int(input())
        P = list(map(int, input().split()))
        result = calculate_sum_of_teams(N, P)
        print(result)

if __name__ == "__main__":
    main()