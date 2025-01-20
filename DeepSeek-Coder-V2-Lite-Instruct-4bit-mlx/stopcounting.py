def calculate_maximum_payout(cards):
    n = len(cards)
    if n == 0:
        return 0.0
    
    total_sum = sum(cards)
    best_average = 0.0
    
    for stop in range(n):
        for start in range(stop, n):
            counted_sum = sum(cards[stop:start+1])
            counted_count = start - stop + 1
            average = counted_sum / counted_count if counted_count > 0 else 0.0
            best_average = max(best_average, average)
    
    return best_average

# Read input
N = int(input())
cards = list(map(int, input().split()))

# Calculate and output the maximum payout
maximum_payout = calculate_maximum_payout(cards)
print("{:.9f}".format(maximum_payout))