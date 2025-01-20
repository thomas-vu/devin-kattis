def read_input():
    n, m = map(int, input().split())
    candidates = [input().strip() for _ in range(m)]
    votes = [list(map(int, input().split())) for _ in range(n)]
    return n, m, candidates, votes

def find_winner(n, m, candidates, votes):
    from collections import defaultdict
    
    vote_counts = [0] * m
    for vote in votes:
        for pref in vote:
            vote_counts[pref - 1] += 1
    
    while True:
        min_votes = min(vote_counts)
        if min_votes > n / 2:
            break
        
        losers = [i for i, count in enumerate(vote_counts) if count == min_votes]
        for loser in losers:
            vote_counts[loser] = 0
        
        for vote in votes:
            for i, pref in enumerate(vote):
                if pref - 1 in losers:
                    vote[i] = m + 1
            while len(set(vote)) > len(candidates):
                vote.remove(max(vote, key=lambda x: (x != m + 1 and vote_counts[x - 1])))
    
    winner_index = max(range(m), key=lambda x: vote_counts[x])
    return candidates[winner_index]

n, m, candidates, votes = read_input()
winner = find_winner(n, m, candidates, votes)
print(winner)