def calculate_probability(K, T, P, Q, X1):
    # Generate the sequence of integers 0, 1, 2, 3 based on the given rules
    sequence = [X1]
    for t in range(2, T + 1):
        sequence.append((sequence[-1] * P) % Q)
    for i in range(T):
        sequence[i] = sequence[i] % 4

    # Calculate the probabilities for each tournament
    probabilities = []
    for t in range(T):
        W = [0, 0, 0, 0]
        for i in range(4):
            W[i] = Q / (Q - P) * (1 - pow(P / Q, i + 1))
        probabilities.append(W[sequence[t]])
    
    # Calculate the probability that Jimmy's strategy correctly predicts at least K winners out of T tournaments
    prob = 0.0
    for i in range(2**T):
        bin_i = bin(i)[2:].zfill(T)
        wins = sum([int(bin_i[t]) for t in range(T)])
        if wins >= K:
            prob += pow(sum([probabilities[t] for t in range(T) if bin_i[t] == '1']), T)
    prob /= 2**T
    
    return prob

# Read input
K, T, P, Q, X1 = map(int, input().split())
weights = [list(map(int, input().split())) for _ in range(T)]

# Calculate and output the probability
probability = calculate_probability(K, T, P, Q, X1)
print("{:.12f}".format(probability))