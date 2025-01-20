import math
from scipy.special import comb

def probability_at_least_k_different(n, s, k):
    if k > s:
        return 0.0
    
    total_outcomes = pow(s, n)
    sum_prob = 0.0
    
    for i in range(k, s + 1):
        sum_prob += comb(s, i) * pow(i, n)
    
    return sum_prob / total_outcomes

def main():
    n, s, k = map(int, input().split())
    prob = probability_at_least_k_different(n, s, k)
    print("{:.9f}".format(prob))

if __name__ == "__main__":
    main()