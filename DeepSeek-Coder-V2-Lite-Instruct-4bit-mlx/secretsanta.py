def calculate_probability(N):
    # The probability that a person does not give a gift to themselves is (N-1)/N
    # The probability that no one gives a gift to themselves is ((N-1)/N)^N
    # The probability that at least one person gives a gift to themselves is 1 - ((N-1)/N)^N
    probability = 1 - ((N - 1) / N) ** N
    return probability

# Read the number of citizens from input
N = int(input())

# Calculate and print the probability
probability = calculate_probability(N)
print("{:.8f}".format(probability))