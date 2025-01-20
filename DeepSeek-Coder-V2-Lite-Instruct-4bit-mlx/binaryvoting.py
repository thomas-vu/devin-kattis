def expected_positions(k, v, probabilities, ballots):
    max_expected = 0
    best_ballots = 0
    
    for y in range(2**k):
        expected = 0
        for i in range(v - 1):
            if (y >> (i % k)) & 1 == 0:
                expected += probabilities[i] * (ballots[i][(y >> (k - 1)) & 1])
            else:
                expected += probabilities[i] * (ballots[i][((y >> (k - 1)) & 1) + 1])
        if expected > max_expected:
            max_expected = expected
            best_ballots = y
    return best_ballots

k, v = map(int, input().split())
probabilities = []
ballots = []
for _ in range(v - 1):
    p_i, b_i = map(float, input().split())
    probabilities.append(p_i)
    ballots.append([b_i, b_i + 1])

# Convert the number of ballots from binary to decimal for each voter
for i in range(v - 1):
    ballots[i][0] = int(bin(ballots[i][0])[2:].zfill(k), 2)
    ballots[i][1] = int(bin(ballots[i][1])[2:].zfill(k), 2)

best_ballots = expected_positions(k, v, probabilities, ballots)
print(int(bin(best_ballots)[2:].zfill(k), end='')