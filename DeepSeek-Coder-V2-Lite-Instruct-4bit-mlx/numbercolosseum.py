N = int(input())
contestants = list(map(int, input().split()))

teamNegatives = []
teamPositives = []
colosseum = []

for contestant in contestants:
    if contestant < 0:
        teamNegatives.append(contestant)
    else:
        teamPositives.append(contestant)

i, j = 0, 0
while i < len(teamNegatives) or j < len(teamPositives):
    if i < len(teamNegatives):
        if j < len(teamPositives):
            if abs(teamNegatives[i]) > teamPositives[j]:
                colosseum.append(teamPositives[j])
                j += 1
            elif abs(teamNegatives[i]) < teamPositives[j]:
                colosseum.append(teamNegatives[i])
                i += 1
            else:
                i += 1
                j += 1
        else:
            colosseum.append(teamNegatives[i])
            i += 1
    else:
        colosseum.append(teamPositives[j])
        j += 1

while i < len(teamNegatives) and j < len(teamPositives):
    if abs(teamNegatives[i]) > teamPositives[j]:
        colosseum.append(teamPositives[j])
        j += 1
    elif abs(teamNegatives[i]) < teamPositives[j]:
        colosseum.append(teamNegatives[i])
        i += 1
    else:
        i += 1
        j += 1

while i < len(teamNegatives):
    colosseum.append(teamNegatives[i])
    i += 1

while j < len(teamPositives):
    colosseum.append(teamPositives[j])
    j += 1

remaining_negatives = [x for x in teamNegatives if x not in colosseum]
remaining_positives = [x for x in teamPositives if x not in colosseum]

if sum(remaining_negatives) < sum(remaining_positives):
    print("Positives win!")
elif sum(remaining_negatives) > sum(remaining_positives):
    print("Negatives win!")
else:
    print("Tie!")

print(' '.join(map(str, colosseum)))