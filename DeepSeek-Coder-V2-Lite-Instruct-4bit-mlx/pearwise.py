def read_input():
    n, m = map(int, input().split())
    ballots = [input().strip() for _ in range(m)]
    return n, m, ballots

def parse_ballots(ballots):
    parsed = []
    for ballot in ballots:
        count = int(ballot.split()[0])
        order = ballot.split()[1]
        parsed.append((count, list(order)))
    return parsed

def pairwise_contests(ballots):
    candidates = set()
    for _, order in ballots:
        candidates.update(order)
    contests = []
    for i in range(0, len(candidates), 2):
        if i + 1 < len(candidates):
            contests.append((candidates[i], candidates[i + 1]))
        else:
            contests.append((candidates[i], None))
    return contests

def evaluate_candidate(ballots, candidate):
    wins = 0
    losses = 0
    for _, order in ballots:
        if candidate in order:
            rank = order.index(candidate)
            for i in range(rank):
                if order[i] != candidate:
                    wins += 1
                    losses -= sum(order.count(c) for c in order[i + 1:])
                    break
            else:
                losses += sum(order.count(c) for c in order[rank + 1:])
        else:
            losses += sum(order.count(c) for c in order)
    return wins - losses

def main():
    n, m, ballots = read_input()
    parsed_ballots = parse_ballots(ballots)
    contests = pairwise_contests(parsed_ballots)
    
    for candidate in chr(65 + i) for i in range(n):
        result = evaluate_candidate(parsed_ballots, candidate)
        print(f"{chr(65 + i)}: {'can win' if result > 0 else 'can\'t win'}")

if __name__ == "__main__":
    main()