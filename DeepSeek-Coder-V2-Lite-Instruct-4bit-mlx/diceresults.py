MOD = 998244353

def main():
    n = int(input())
    h_sides = list(map(int, input().split()))
    
    # Calculate the maximum possible sum of dice rolls
    max_sum = n * max(h_sides)
    
    # Initialize the number of ways to achieve each sum
    ways = [0] * (max_sum + 1)
    
    # Base case: one die with one side (only the sum of 1)
    ways[0] = 1
    
    # Calculate the number of ways to achieve each sum for all dice
    for die in h_sides:
        for i in range(max_sum, -1, -1):
            ways[i] = sum(ways[max(0, i - die):i]) % MOD
    
    # Output the number of ways for each possible sum from 1 to max_sum
    for i in range(1, max_sum + 1):
        print(ways[i])

if __name__ == "__main__":
    main()