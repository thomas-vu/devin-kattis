from collections import defaultdict
votes = []
while True:
    line = input()
    if line == "***":
        break
    votes.append(line)

vote_counts = defaultdict(int)
for vote in votes:
    vote_counts[vote] += 1

max_votes = max(vote_counts.values())
winners = [candidate for candidate, count in vote_counts.items() if count == max_votes]

if len(winners) == 1 and winners[0] != "***":
    print(winners[0])
else:
    print("Runoff!")