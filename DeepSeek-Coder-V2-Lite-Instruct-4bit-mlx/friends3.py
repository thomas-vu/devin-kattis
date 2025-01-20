N, L, Q = map(int, input().split())
P = list(map(int, input().split()))
positions = [False] * L
for p in P:
    positions[p] = True
jumps = []
scores = []
for _ in range(Q):
    line = list(map(int, input().split()))
    if line[0] == 0:
        jumps.append((line[1], line[2]))
    elif line[0] == 1:
        scores.append(line[1])

for jump in jumps:
    A, B = jump
    if positions[A]:
        positions[A] = False
        positions[B] = True

def score():
    max_score = 0
    current_streak = 0
    for pos in positions:
        if pos:
            current_streak += 1
            max_score = max(max_score, current_streak)
        else:
            current_streak = 0
    return max_score

for s in scores:
    if s == 1:
        A, B = jumps.pop(0)
        positions[A] = False
        positions[B] = True
    else:
        print(score())