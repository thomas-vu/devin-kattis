def calculate_probability(n, m, d, your_minions, opponent_minions):
    from math import comb

    total_combinations = 0
    successful_combinations = 0

    for i in range(d + 1):
        for j in range(d - i + 1):
            if (i + j) % m == 0:
                total_combinations += comb(n + (i + j) // m, i + j) * comb(n, i)
                successful_combinations += comb(n + (i + j) // m, i + j) * comb(n, i)

    probability = successful_combinations / total_combinations
    return probability

def main():
    n, m, d = map(int, input().split())
    your_minions = list(map(int, input().split()))
    opponent_minions = list(map(int, input().split()))

    minion_healths = [your_minions, opponent_minions]
    probabilities = []

    for health in minion_healths:
        probability = calculate_probability(n, m, d, your_minions, opponent_minions)
        probabilities.append(probability)

    final_probability = 1 - (1 - probabilities[0]) * (1 - probabilities[1])
    print("{:.10f}".format(final_probability))

if __name__ == "__main__":
    main()