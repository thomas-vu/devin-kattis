import sys
from operator import itemgetter

# Read input
N = int(sys.stdin.readline().strip())
adventurers = []
for _ in range(N):
    name, S1, S2, S3 = sys.stdin.readline().strip().split()
    adventurers.append((name, int(S1), int(S2), int(S3)))

# Sort adventurers by the first skill, then second skill, and finally third skill
adventurers.sort(key=itemgetter(1, 2, 3))

# Keep track of selected adventurers and available adventurers
selected = [False] * N
available = list(range(N))

# Process to form teams
while len(available) >= 3:
    team = []
    for i in range(3):
        # Find the adventurer with the highest skill value for the current skill
        best_index = -1
        best_skill_value = -1
        for j in available:
            if not selected[j] and (best_index == -1 or adventurers[j][i + 1] > best_skill_value):
                best_index = j
                best_skill_value = adventurers[j][i + 1]
            elif not selected[j] and adventurers[j][i + 1] == best_skill_value:
                if adventurers[j][0] < adventurers[best_index][0]:
                    best_index = j
        # Add the selected adventurer to the team and mark them as selected
        team.append(adventurers[best_index][0])
        selected[best_index] = True
    # Output the team
    print(' '.join(sorted(team)))
    # Update available adventurers list
    available = [i for i in available if not selected[i]]