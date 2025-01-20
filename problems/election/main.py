def determine_outcome(N, V1, V2, W):
    total_votes = N
    needed_to_win = (total_votes // 2) + 1
    current_votes = V1
    remaining_votes = total_votes - V2
    probability_win = 0.5 ** remaining_votes
    
    for k in range(remaining_votes + 1):
        if V1 + k >= needed_to_win:
            probability_win += (0.5 ** k) * ((1 / (2 ** k)) - (1 / (2 ** (k + 1))))
    
    if probability_win * 100 > W:
        return "GET A CRATE OF CHAMPAGNE FROM THE BASEMENT!"
    elif probability_win * 100 < W:
        return "RECOUNT!"
    else:
        return "PATIENCE, EVERYONE!"

def main():
    T = int(input())
    results = []
    for _ in range(T):
        N, V1, V2, W = map(int, input().split())
        results.append(determine_outcome(N, V1, V2, W))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()