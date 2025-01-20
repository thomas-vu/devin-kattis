import sys

def main():
    N, L, P = map(float, input().split())
    sides = list(map(int, [input() for _ in range(N)]))
    
    # Sort the sides to ensure we try licking from the shortest side to the longest
    sides.sort()
    
    # Initialize the maximum probability of avoiding inkage to 0
    max_prob = 0.0
    
    # Use dynamic programming to find the maximum probability of avoiding inkage
    prob = [0.0] * (N + 1)
    for i in range(N):
        # Probability of not getting inked by licking the current side i times
        prob[i + 1] = min(prob[i], sides[i] * (P ** i))
    
    # The maximum probability of avoiding inkage is the sum of probabilities for each side
    max_prob = sum(prob[:N])
    
    # Output the result with a precision of 7 decimal places
    print("{:.7f}".format(max_prob))

if __name__ == "__main__":
    main()