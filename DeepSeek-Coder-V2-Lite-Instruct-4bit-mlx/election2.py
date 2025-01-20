def main():
    n = int(input())
    candidates = {}
    
    for _ in range(n):
        name = input()
        party = input()
        candidates[name] = party
    
    m = int(input())
    votes = {}
    
    for _ in range(m):
        candidate_name = input()
        if candidate_name in candidates:
            if candidate_name not in votes:
                votes[candidate_name] = 0
            votes[candidate_name] += 1
    
    if not votes:
        print("tie")
        return
    
    max_votes = max(votes.values())
    winning_candidates = [name for name, count in votes.items() if count == max_votes]
    
    if len(winning_candidates) == 1:
        winning_name = winning_candidates[0]
        if candidates[winning_name] == "independent":
            print("independent")
        else:
            print(candidates[winning_name])
    else:
        print("tie")

if __name__ == "__main__":
    main()