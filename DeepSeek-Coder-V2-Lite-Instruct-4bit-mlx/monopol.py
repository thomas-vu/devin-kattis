# Solution for the monopoly problem
N = int(input())
A = list(map(int, input().split()))
total_outcomes = 36.0
probabilities = [0] * (N)

for sum_of_dice in range(2, 13):
    if sum_of_dice in A:
        probabilities[A.index(sum_of_dice)] += 1

probability = sum(probabilities) / total_outcomes
print("{:.15f}".format(probability))