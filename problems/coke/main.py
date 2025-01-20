def min_coins(C, n1, n5, n10):
    # Start with the minimum number of coins needed to buy one coke
    min_coins = C * 1
    
    # Try to use as many 10-crown coins as possible
    for i in range(min(C, n10) + 1):
        remaining_cokes = C - i
        total_coins = n1 + n5 * 5 + n10 * 10 - i * 10
        
        # Use as many 5-crown coins as possible for the remaining cokes
        five_coins_needed = max(0, remaining_cokes - n1)
        
        # If we have enough coins for the remaining cokes after using 10-crowns
        if five_coins_needed <= n5 + (i * 2):
            min_coins = min(min_coins, i + n1 + n5 + five_coins_needed)
    
    return min_coins

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    cases = []
    for i in range(1, T + 1):
        C = int(data[i].split()[0])
        n1 = int(data[i].split()[1])
        n5 = int(data[i].split()[2])
        n10 = int(data[i].split()[3])
        cases.append((C, n1, n5, n10))
    
    for case in cases:
        C, n1, n5, n10 = case
        print(min_coins(C, n1, n5, n10))

if __name__ == "__main__":
    main()