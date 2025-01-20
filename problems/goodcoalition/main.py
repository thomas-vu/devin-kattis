# This code is written in Python 3 as requested and solves the given problem.
import itertools

def calculate_probability(coalition):
    prob = 1.0
    for party in coalition:
        prob *= (party[1] / 100.0)
    return prob * 100

def main():
    num_cases = int(input())
    for _ in range(num_cases):
        n = int(input())
        parties = []
        for _ in range(n):
            s_i, p_i = map(int, input().split())
            parties.append((s_i, p_i))
        
        max_prob = 0.0
        for r in range(1, n + 1):
            for coalition in itertools.combinations(parties, r):
                total_seats = sum([party[0] for party in coalition])
                if total_seats >= 76:
                    prob = calculate_probability(coalition)
                    max_prob = max(max_prob, prob)
        
        print("{:.6f}".format(max_prob))

if __name__ == "__main__":
    main()