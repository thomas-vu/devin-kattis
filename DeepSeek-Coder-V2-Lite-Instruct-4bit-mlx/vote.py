def find_winner(votes):
    max_votes = max(votes)
    winners = [i + 1 for i, v in enumerate(votes) if v == max_votes]
    if len(winners) > 1:
        return "no winner"
    elif len(winners) == 1 and votes.count(max_votes) > sum(votes) / 2:
        return f"majority winner {winners[0]}"
    else:
        return f"minority winner {winners[0]}"

T = int(input())
for _ in range(T):
    n = int(input())
    votes = [int(input()) for _ in range(n)]
    print(find_winner(votes))