def determine_elected_candidate(C, P, parties):
    from collections import defaultdict
    
    votes = defaultdict(int)
    for party in parties:
        v, ranking = party
        for rank in ranking.split():
            votes[int(rank)] += v
    
    while True:
        total_votes = sum(votes.values())
        majority = total_votes // 2 + 1
        
        min_eliminated_vote = float('inf')
        candidates_to_eliminate = []
        
        for candidate, vote in votes.items():
            if vote < min_eliminated_vote:
                min_eliminated_vote = vote
                candidates_to_eliminate = [candidate]
            elif vote == min_eliminated_vote:
                candidates_to_eliminate.append(candidate)
        
        if min_eliminated_vote > majority:
            break
        
        for candidate in candidates_to_eliminate:
            del votes[candidate]
    
    elected_candidate = max(votes, key=lambda x: votes[x])
    return elected_candidate

# Read input
C, P = map(int, input().split())
parties = []
for _ in range(P):
    party_data = input().split()
    v = int(party_data[0])
    ranking = party_data[1]
    parties.append((v, ranking))

# Determine the elected candidate
elected_candidate = determine_elected_candidate(C, P, parties)
print(elected_candidate)